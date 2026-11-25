#!/usr/bin/env python3
"""Extract fenced code blocks from Markdown docs pages, check them, and report failures.

Standard library only. Runs on Python 3.9+.

What it checks (nothing is executed unless you pass --run):

  python   Syntax (parsed by the target interpreter, top-level await allowed).
           Every import statement, imported in a subprocess of the target interpreter.
           Every attribute chain rooted at an imported name (e.g. `room_io.RoomOptions`).
           Keyword arguments passed to imported callables, against inspect.signature.
           With --run, executes the whole block with a timeout.
  shell    `bash -n` syntax. Also `text` fences whose first word is a known CLI.
           With --network: `git clone` targets (git ls-remote), `pip install` / `uv add`
           packages (PyPI), `npm|pnpm|yarn add|install` packages (npm registry),
           `brew install` formulae (formulae.brew.sh), and URLs passed to curl/wget.
  json     json.loads
  toml     tomllib, if the target interpreter has it
  js       `node --check`, if node is installed (ts/tsx are reported as skipped)

Usage:
  test_code_blocks.py PAGE [PAGE ...] [--python PATH] [--network] [--run]
                      [--index] [--limit N] [--format md|json] [--only-problems]

PAGE is a local .md file or an http(s) URL. With --index, each PAGE is treated as an
llms.txt-style index and every linked .md page is tested (up to --limit pages).
"""

import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import urllib.error
import urllib.request
from typing import Dict, List, Optional

USER_AGENT = "docs-code-tester/0.1 (+https://github.com)"
TIMEOUT = 20

PY_LANGS = {"python", "py", "python3"}
SHELL_LANGS = {"shell", "bash", "sh", "zsh", "console", "shell-session", "terminal"}
JS_LANGS = {"javascript", "js", "mjs", "cjs"}
TS_LANGS = {"typescript", "ts", "tsx", "jsx"}
KNOWN_CLIS = {
    "lk", "git", "pip", "pip3", "uv", "uvx", "python", "python3", "npm", "pnpm", "npx",
    "yarn", "node", "brew", "curl", "wget", "cd", "export", "docker", "make", "winget",
    "go", "cargo", "kubectl", "helm", "livekit-server", "flutter", "pod", "dotnet",
}

# --------------------------------------------------------------------------- fetching


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/markdown"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "replace")


def url_ok(url: str, method: str = "HEAD") -> (bool, str):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return True, str(r.status)
    except urllib.error.HTTPError as e:
        if method == "HEAD" and e.code in (403, 405):
            return url_ok(url, "GET")
        return False, "HTTP %d" % e.code
    except Exception as e:  # noqa: BLE001
        return False, type(e).__name__ + ": " + str(e)


def load_page(src: str) -> str:
    if re.match(r"https?://", src):
        return fetch(src)
    with open(src, encoding="utf-8") as f:
        return f.read()


def expand_index(src: str, limit: int) -> List[str]:
    text = load_page(src)
    links = re.findall(r"\]\((https?://[^)\s]+?\.md)\)", text)
    seen, out = set(), []
    for link in links:
        if link not in seen:
            seen.add(link)
            out.append(link)
    return out[:limit] if limit else out


# --------------------------------------------------------------------------- extraction

FENCE_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})(?P<info>[^`]*)$")


def extract_blocks(md: str) -> List[Dict]:
    """Return fenced code blocks with language, start line, and nearby context."""
    blocks = []
    lines = md.splitlines()
    heading, tab, filename = "", "", ""
    i = 0
    while i < len(lines):
        line = lines[i]
        h = re.match(r"^#{1,6}\s+(.*)", line)
        if h:
            heading, tab, filename = h.group(1).strip(), "", ""
        t = re.match(r"^\*\*([^*]+)\*\*:\s*$", line.strip())  # flattened tab label, e.g. **Python**:
        if t:
            tab = t.group(1).strip()
        fn = re.search(r"Filename:\s*`([^`]+)`", line)
        if fn:
            filename = fn.group(1)
        m = FENCE_RE.match(line)
        if m:
            indent, fence = m.group("indent"), m.group("fence")
            info = m.group("info").strip()
            lang = info.split()[0].lower() if info else ""
            body, j = [], i + 1
            while j < len(lines):
                close = lines[j].strip()
                if close.startswith(fence[0] * len(fence)) and set(close) <= {fence[0]}:
                    break
                body.append(lines[j][len(indent):] if lines[j].startswith(indent) else lines[j])
                j += 1
            blocks.append({
                "index": len(blocks) + 1,
                "line": i + 1,
                "lang": lang,
                "heading": heading,
                "tab": tab,
                "filename": filename,
                "code": "\n".join(body).rstrip() + "\n",
            })
            filename = ""
            i = j + 1
            continue
        i += 1
    return blocks


# --------------------------------------------------------------------------- python checks

# Runs inside the target interpreter. Reads a JSON job on stdin, prints JSON results.
PY_HELPER = r'''
import ast, inspect, json, sys, importlib
job = json.load(sys.stdin)
out = {"syntax": None, "imports": [], "attrs": [], "kwargs": []}
src = job["code"]
flags = ast.PyCF_ONLY_AST | getattr(ast, "PyCF_ALLOW_TOP_LEVEL_AWAIT", 0)
try:
    compile(src, "<block>", "exec", flags)
except SyntaxError as e:
    out["syntax"] = "line %s: %s" % (e.lineno, e.msg)
    print(json.dumps(out)); sys.exit(0)
ns = {}
for stmt in job["imports"]:
    try:
        exec(stmt, ns)
        out["imports"].append({"stmt": stmt, "ok": True})
    except Exception as e:
        msg = str(e).split(" (/")[0]  # drop the site-packages path ImportError appends
        env = isinstance(e, ModuleNotFoundError) or "not installed" in msg
        parent = getattr(e, "name", None) or ""
        mod = sys.modules.get(parent)
        if mod is not None and getattr(mod, "__file__", None) is None:
            env = True  # namespace package such as livekit.plugins: the plugin isn't installed
        out["imports"].append({"stmt": stmt, "ok": False, "env": env,
                               "err": "%s: %s" % (type(e).__name__, msg)})
def resolve(chain):
    obj = ns[chain[0]]
    for i, part in enumerate(chain[1:], 1):
        if not hasattr(obj, part):
            raise AttributeError("%s has no attribute %r" % (".".join(chain[:i]), part))
        obj = getattr(obj, part)
    return obj
for chain in job["attrs"]:
    if chain[0] not in ns:
        continue
    try:
        resolve(chain)
        out["attrs"].append({"chain": ".".join(chain), "ok": True})
    except Exception as e:
        out["attrs"].append({"chain": ".".join(chain), "ok": False, "err": str(e)})
for call in job["calls"]:
    chain, kws = call["chain"], call["kwargs"]
    if chain[0] not in ns:
        continue
    try:
        fn = resolve(chain)
    except Exception:
        continue
    fields = getattr(fn, "model_fields", None)  # pydantic models hide fields from inspect
    if isinstance(fields, dict):
        names = set(fields) | {f.alias for f in fields.values() if getattr(f, "alias", None)}
    else:
        try:
            sig = inspect.signature(fn)
        except Exception:
            continue
        params = sig.parameters.values()
        if any(p.kind == p.VAR_KEYWORD for p in params) or not sig.parameters:
            continue
        names = {p.name for p in params if p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)}
    bad = [k for k in kws if k not in names]
    out["kwargs"].append({"call": ".".join(chain), "ok": not bad, "unknown": bad,
                          "line": call["line"], "accepted": sorted(names)})
print(json.dumps(out))
'''


def dotted_chain(node) -> Optional[List[str]]:
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return list(reversed(parts))
    return None


def analyze_python(code: str, local_modules: set) -> Dict:
    """Pull imports, attribute chains, and keyword calls out of a block (host-side AST)."""
    flags = ast.PyCF_ONLY_AST | getattr(ast, "PyCF_ALLOW_TOP_LEVEL_AWAIT", 0)
    try:
        tree = compile(code, "<block>", "exec", flags)
    except SyntaxError:
        return {"imports": [], "attrs": [], "calls": [], "skipped_local": []}
    imports, skipped = [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if isinstance(node, ast.ImportFrom) and (node.level or 0) > 0:
                continue
            mod = node.module if isinstance(node, ast.ImportFrom) else node.names[0].name
            if mod and mod.split(".")[0] in local_modules:
                skipped.append(ast.unparse(node) if hasattr(ast, "unparse") else mod)
                continue
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:  # one statement per name, so one bad name doesn't hide others
                    a = " as %s" % alias.asname if alias.asname else ""
                    imports.append("from %s import %s%s" % (node.module, alias.name, a))
            else:
                for alias in node.names:
                    a = " as %s" % alias.asname if alias.asname else ""
                    imports.append("import %s%s" % (alias.name, a))
    attrs, seen = [], set()
    inner = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if id(node) in inner:
                continue
            v = node.value
            while isinstance(v, ast.Attribute):
                inner.add(id(v))
                v = v.value
            chain = dotted_chain(node)
            if chain and tuple(chain) not in seen:
                seen.add(tuple(chain))
                attrs.append(chain)
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            chain = dotted_chain(node.func)
            kws = [k.arg for k in node.keywords if k.arg]
            if chain and kws:
                calls.append({"chain": chain, "kwargs": kws, "line": node.lineno})
    return {"imports": imports, "attrs": attrs, "calls": calls, "skipped_local": skipped}


def run_helper(code: str, python: str, local_modules: set):
    info = analyze_python(code, local_modules)
    p = subprocess.run([python, "-I", "-c", PY_HELPER], input=json.dumps(dict(info, code=code)),
                       capture_output=True, text=True, timeout=120)
    return json.loads(p.stdout), info


def repairs(code: str):
    """Yield (description, code) candidates that turn common doc fragments into valid Python."""
    placeholder = re.sub(r"<[A-Za-z][^<>\n]*>", "None", code)
    if placeholder != code:
        yield "uses `<placeholder>` values", placeholder
    no_ellipsis = re.sub(r",\s*\.\.\.(?=\s*[,)])", "", code)
    no_ellipsis = re.sub(r"\(\s*\.\.\.\s*,?", "(", no_ellipsis)
    no_ellipsis = re.sub(r"(?m)^\s*\.\.\.\s*,?\s*$\n?", "", no_ellipsis)
    if no_ellipsis != code:
        yield "uses `...` in place of other arguments", no_ellipsis
    for indent in ("    ", "        "):
        yield "body elided with a comment", code.rstrip() + "\n" + indent + "pass\n"


def check_python(block: Dict, python: str, local_modules: set, run: bool) -> List[Dict]:
    code = block["code"]
    if code.startswith((" ", "\t")):
        code = textwrap.dedent(code)
    try:
        res, info = run_helper(code, python, local_modules)
    except Exception as e:  # noqa: BLE001
        return [{"status": "error", "check": "python", "detail": "helper failed: %s" % e}]
    results = []
    if res["syntax"]:
        # Docs often show deliberate fragments: `# ...` bodies, `<placeholder>` values, or a
        # bare `...` standing in for other arguments. If a mechanical repair parses, report
        # a note (it won't run as pasted) and keep checking the repaired code.
        for kind, repaired in repairs(code):
            r2, i2 = run_helper(repaired, python, local_modules)
            if not r2["syntax"]:
                results.append({"status": "note", "check": "fragment",
                                "detail": "doesn't parse as pasted (%s); %s" % (res["syntax"], kind)})
                res, info, code = r2, i2, repaired
                break
        else:
            return [{"status": "fail", "check": "syntax", "detail": res["syntax"]}]
    else:
        results.append({"status": "pass", "check": "syntax", "detail": ""})
    for imp in res["imports"]:
        if not imp["ok"]:
            results.append({"status": "env" if imp.get("env") else "fail", "check": "import",
                            "detail": "`%s` -> %s" % (imp["stmt"], imp["err"])})
    for a in res["attrs"]:
        if not a["ok"]:
            results.append({"status": "fail", "check": "attribute", "detail": a["err"]})
    for c in res["kwargs"]:
        if not c["ok"]:
            results.append({"status": "fail", "check": "kwargs",
                            "detail": "block line %d: `%s()` does not accept %s" % (
                                c["line"], c["call"], ", ".join("`%s`" % u for u in c["unknown"]))})
    if info["skipped_local"]:
        results.append({"status": "note", "check": "import",
                        "detail": "skipped local imports: " + "; ".join(info["skipped_local"])})
    if run:
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "block.py")
            with open(path, "w") as f:
                f.write(code)
            try:
                p = subprocess.run([python, path], capture_output=True, text=True, timeout=60, cwd=d)
                if p.returncode != 0:
                    tail = (p.stderr.strip().splitlines() or ["exit %d" % p.returncode])[-1]
                    results.append({"status": "fail", "check": "run", "detail": tail})
                else:
                    results.append({"status": "pass", "check": "run", "detail": ""})
            except subprocess.TimeoutExpired:
                results.append({"status": "note", "check": "run", "detail": "timed out after 60s (long-running?)"})
    return results


# --------------------------------------------------------------------------- shell checks


def shell_lines(code: str) -> List[str]:
    out, buf = [], ""
    for raw in code.splitlines():
        line = re.sub(r"^\s*[$>]\s+", "", raw).rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.endswith("\\"):
            buf += line[:-1] + " "
            continue
        out.append((buf + line).strip())
        buf = ""
    return out


def looks_like_commands(code: str) -> bool:
    lines = shell_lines(code)
    return bool(lines) and all(l.split()[0] in KNOWN_CLIS for l in lines if l.split())


def check_shell(block: Dict, network: bool) -> List[Dict]:
    results = []
    lines = shell_lines(block["code"])
    script = "\n".join(lines) + "\n"
    # `<run-id>` and `<YOUR_API_KEY>` are placeholders, not redirections.
    script = re.sub(r"<([A-Za-z][^<>\n]*)>", "PLACEHOLDER", script)
    first = lines[0].split()[0] if lines and lines[0].split() else ""
    if shutil.which("bash"):
        p = subprocess.run(["bash", "-n"], input=script, capture_output=True, text=True)
        if p.returncode != 0:
            if first not in KNOWN_CLIS and not shutil.which(first) and "=" not in first:
                return [{"status": "note", "check": "fence",
                         "detail": "looks like program output, not commands, but is tagged `%s`" % block["lang"]}]
            results.append({"status": "fail", "check": "bash -n", "detail": p.stderr.strip()})
    if block["lang"] in ("text", "", "txt", "plaintext"):
        results.append({"status": "note", "check": "fence",
                        "detail": "shell commands in a `%s` fence (no shell highlighting; tools can't tell it's runnable)"
                        % (block["lang"] or "untagged")})
    for line in lines:
        toks = line.split()
        if not toks:
            continue
        cmd = toks[0]
        if cmd not in ("cd", "export") and not shutil.which(cmd):
            results.append({"status": "skip", "check": "requires", "detail": "`%s` not installed here" % cmd})
        if cmd in ("pip", "pip3", "uv", "uvx", "poetry"):
            for t in toks[1:]:
                if "[" in t and not t.startswith(("'", '"')):
                    results.append({"status": "note", "check": "zsh",
                                    "detail": "`%s` is unquoted; zsh (the macOS default shell) fails with "
                                              "\"no matches found\". Quote it: '%s'" % (t, t)})
        if not network:
            continue
        if cmd == "git" and len(toks) > 2 and toks[1] == "clone":
            target = [t for t in toks[2:] if not t.startswith("-")][0]
            env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
            p = subprocess.run(["git", "ls-remote", "--heads", target], capture_output=True,
                               text=True, timeout=TIMEOUT, env=env)
            if p.returncode != 0:
                err = (p.stderr.strip().splitlines() or ["?"])[0]
                results.append({"status": "fail", "check": "git clone",
                                "detail": "`%s` is not a reachable repository: %s" % (target, err)})
            else:
                results.append({"status": "pass", "check": "git clone", "detail": target})
        pkgs = []
        if cmd in ("pip", "pip3") and "install" in toks:
            pkgs = [("pypi", t) for t in toks[toks.index("install") + 1:] if not t.startswith("-")]
        elif cmd == "uv" and len(toks) > 1 and toks[1] in ("add",) or toks[:3] == ["uv", "pip", "install"]:
            start = 2 if toks[1] == "add" else 3
            pkgs = [("pypi", t) for t in toks[start:] if not t.startswith("-")]
        elif cmd in ("npm", "pnpm", "yarn") and len(toks) > 1 and toks[1] in ("add", "install", "i"):
            pkgs = [("npm", t) for t in toks[2:] if not t.startswith("-")]
        elif cmd == "brew" and len(toks) > 2 and toks[1] == "install":
            pkgs = [("brew", t) for t in toks[2:] if not t.startswith("-")]
        for reg, spec in pkgs:
            spec = spec.strip("\"'")
            if reg == "pypi":
                name = re.split(r"[\[<>=!~;@ ]", spec)[0]
                if not name or name.startswith((".", "/")):
                    continue
                ok, why = url_ok("https://pypi.org/pypi/%s/json" % name, "GET")
            elif reg == "npm":
                name = re.sub(r"(?<!^)@.*$", "", spec)
                ok, why = url_ok("https://registry.npmjs.org/%s" % name.replace("/", "%2F"), "GET")
            else:
                name = spec.split("/")[-1]
                ok, why = url_ok("https://formulae.brew.sh/api/formula/%s.json" % name, "GET")
                if not ok:
                    ok, why = url_ok("https://formulae.brew.sh/api/cask/%s.json" % name, "GET")
            results.append({"status": "pass" if ok else "fail", "check": reg,
                            "detail": name if ok else "`%s` not found on %s (%s)" % (name, reg, why)})
        if cmd in ("curl", "wget"):
            for u in re.findall(r"https?://[^\s'\"|)]+", line):
                if "<" in u or "PLACEHOLDER" in u:
                    continue
                ok, why = url_ok(u)
                if not ok and why in ("HTTP 401", "HTTP 403"):
                    ok, why = True, why  # reachable; the endpoint just needs credentials
                results.append({"status": "pass" if ok else "fail", "check": "url",
                                "detail": u if ok else "%s -> %s" % (u, why)})
    if not results:
        results.append({"status": "pass", "check": "bash -n", "detail": ""})
    return results


# --------------------------------------------------------------------------- other languages


def check_other(block: Dict, python: str) -> List[Dict]:
    lang, code = block["lang"], block["code"]
    if lang == "json":
        try:
            json.loads(code)
            return [{"status": "pass", "check": "json", "detail": ""}]
        except ValueError as e:
            return [{"status": "fail", "check": "json", "detail": str(e)}]
    if lang == "toml":
        p = subprocess.run([python, "-I", "-c", "import sys,tomllib;tomllib.loads(sys.stdin.read())"],
                           input=code, capture_output=True, text=True)
        if "No module named 'tomllib'" in p.stderr:
            return [{"status": "skip", "check": "toml", "detail": "target Python has no tomllib"}]
        return [{"status": "pass" if p.returncode == 0 else "fail", "check": "toml",
                 "detail": (p.stderr.strip().splitlines() or [""])[-1]}]
    if lang in JS_LANGS:
        if not shutil.which("node"):
            return [{"status": "skip", "check": "js", "detail": "node not installed"}]
        with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False) as f:
            f.write(code)
        p = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
        os.unlink(f.name)
        return [{"status": "pass" if p.returncode == 0 else "fail", "check": "node --check",
                 "detail": (p.stderr.strip().splitlines() or [""])[0]}]
    if lang in TS_LANGS:
        return [{"status": "skip", "check": lang, "detail": "TypeScript checking not implemented"}]
    return [{"status": "skip", "check": "lang", "detail": "no checker for `%s`" % (lang or "untagged")}]


# --------------------------------------------------------------------------- driver


def test_page(src: str, args) -> Dict:
    try:
        md = load_page(src)
    except Exception as e:  # noqa: BLE001
        return {"page": src, "error": str(e), "blocks": []}
    blocks = extract_blocks(md)
    local = {os.path.splitext(b["filename"])[0] for b in blocks if b["filename"].endswith(".py")}
    local |= set(args.local or [])
    for b in blocks:
        lang = b["lang"]
        if lang in PY_LANGS:
            b["results"] = check_python(b, args.python, local, args.run)
        elif lang in SHELL_LANGS or (lang in ("text", "", "txt", "plaintext") and looks_like_commands(b["code"])):
            b["results"] = check_shell(b, args.network)
        elif lang in ("text", "", "txt", "plaintext"):
            b["results"] = [{"status": "skip", "check": "prose", "detail": "plain text, not code"}]
        else:
            b["results"] = check_other(b, args.python)
    return {"page": src, "blocks": blocks}


RANK = {"fail": 0, "error": 0, "env": 1, "note": 2, "skip": 3, "pass": 4}


def block_status(b: Dict) -> str:
    return min((r["status"] for r in b["results"]), key=lambda s: RANK[s])


def render_md(pages: List[Dict], only_problems: bool) -> str:
    out = []
    totals: Dict[str, int] = {}
    for page in pages:
        out.append("## %s\n" % page["page"])
        if page.get("error"):
            out.append("Could not load page: %s\n" % page["error"])
            continue
        rows = []
        for b in page["blocks"]:
            st = block_status(b)
            totals[st] = totals.get(st, 0) + 1
            shown = [r for r in b["results"] if r["status"] not in ("pass",)] or b["results"]
            if only_problems and st not in ("fail", "error", "env"):
                continue
            where = " / ".join(x for x in (b["heading"], b["tab"], b["filename"]) if x)
            detail = "<br>".join("**%s** %s: %s" % (r["status"], r["check"], r["detail"].replace("|", "\\|"))
                                 for r in shown if r["detail"] or r["status"] != "pass") or "ok"
            rows.append("| %d | %d | %s | %s | %s | %s |" % (
                b["index"], b["line"], b["lang"] or "-", where.replace("|", "\\|"), st.upper(), detail))
        if rows:
            out.append("| # | Line | Lang | Section | Status | Details |")
            out.append("|---|---|---|---|---|---|")
            out.extend(rows)
        else:
            out.append("No problems found in %d blocks." % len(page["blocks"]))
        out.append("")
    summary = ", ".join("%d %s" % (n, s) for s, n in sorted(totals.items(), key=lambda kv: RANK[kv[0]]))
    return "# Code sample report\n\nBlocks by worst status: %s\n\n" % (summary or "none") + "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="+", help="Markdown file paths or URLs")
    ap.add_argument("--python", default=sys.executable,
                    help="interpreter whose environment has the documented packages installed")
    ap.add_argument("--network", action="store_true", help="check repos, packages and URLs online")
    ap.add_argument("--run", action="store_true", help="also execute complete Python blocks (60s timeout)")
    ap.add_argument("--index", action="store_true", help="treat PAGES as llms.txt indexes and test every .md link")
    ap.add_argument("--limit", type=int, default=0, help="max pages per index")
    ap.add_argument("--local", nargs="*", help="module names to treat as the reader's own files")
    ap.add_argument("--format", choices=("md", "json"), default="md")
    ap.add_argument("--only-problems", action="store_true", help="hide blocks that passed or were skipped")
    args = ap.parse_args()

    sources = []
    for p in args.pages:
        sources.extend(expand_index(p, args.limit) if args.index else [p])
    pages = []
    for s in sources:
        print("testing %s" % s, file=sys.stderr)
        pages.append(test_page(s, args))
    if args.format == "json":
        print(json.dumps(pages, indent=2))
    else:
        print(render_md(pages, args.only_problems))
    failed = any(block_status(b) in ("fail", "error") for p in pages for b in p.get("blocks", []))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
