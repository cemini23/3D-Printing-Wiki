# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-10-03] A green lint is not proof of health — fixing one error unmasked another

**What happened:** On 2026-09-30 I fixed the `../../OSINT WORKSPACE/` path in `CLAUDE.md` to `../OSINT WORKSPACE/`. That is what `wiki_lint.py` reads to build its cross-wiki alias table.

Before the fix, every cross-wiki check failed to resolve a base directory and the linter reported **"0 dangling, 2 ok"** — a clean bill of health it had not earned.

After the fix, the linter could resolve the sibling wiki and immediately reported **"3 dangling, 14 ok"**. Those three turned out to be **false positives**: the regex was

```python
CROSS_WIKI_RE = re.compile(r"@([a-z0-9_-]+)/([^\s`)]+)")
```

The excluded-character class omitted quotes. Frontmatter carries the form `cross-wiki-source: "@osint-wiki/path.md"`, so the closing `"` was captured into the path and the lookup failed. All three target files existed the whole time. Fixed by adding `\"'` to the class → **0 dangling, 17 ok**.

**The lesson:** a validator that cannot reach its inputs reports success. "0 dangling" and "0 dangling *after being able to check*" are different claims. When a lint section reports clean while a neighbouring section reports many findings, check whether the clean section is actually doing work.

**What to do:** after changing anything the linter reads (paths, alias tables, config), re-run it and compare *every* section's numbers against the previous run, not just the exit code. A sudden jump in "ok" counts means the linter just started doing more work.

## [2026-10-03] Routing works — but only from the Terminal panel, not the Bash tool

**Update to the 2026-09-30 entry below.** That entry concluded routing was blocked. It is not. The fix is to use the **Terminal panel** instead of the sandboxed Bash tool.

**Verified:** `route-task` easy lane ran end-to-end on 2026-10-03, using the OpenRouter free tier, and returned a usable output. Command run from the Terminal panel:

```bash
route-task -Profile claudio -WorkDir "/Users/claudiobarone/Projects/3D printing" "easy: <task>"
```

**Why it works:** the Terminal panel starts the user's own login shell, outside the OS sandbox. The sandboxed Bash tool denies writes to `~/Projects/agent-toolkit/` (where `route-task` writes run logs) and denies network to the executor endpoints.

**Use the Terminal panel for anything that leaves the project directory or needs the network:**

| Task | Sandboxed Bash | Terminal panel |
|---|---|---|
| `route-task` / grok / opencode | Denied | Works |
| `git push` | Denied | Works |
| Egress archive (`scp`) | Denied | Works |

**What to do:** Plan routing work as normal, but run it in the Terminal panel. The user sees and approves each command there. Do not report these as impossible — report which surface works.

## [2026-09-30] External model routing does not work inside the desktop sandbox

**Superseded 2026-10-03 — see the entry above.** The failures below are real, but they apply to the **sandboxed Bash tool only**. Run the same commands from the Terminal panel and they work.

**What broke:** The `route` skill and its executors cannot run in a sandboxed Claude desktop session.

Tested all three paths. All failed:

| Path | Failure |
|------|---------|
| `route-task` | Exit 1. It writes run logs to `~/Projects/agent-toolkit/`. The sandbox denies that path. |
| `grok -p` | Network denied to `cli-chat-proxy.grok.com:443`. Also filesystem denied on `~/.grok`. |
| `opencode run` | Filesystem denied on `~/.local/share/opencode/log/opencode.log`. |

`allowed_domains` cannot widen the allowlist — this session uses a strict allowlist policy.

**What to do:** Do not promise routed work in a sandboxed session. Run routing from a normal terminal, or accept in-session drafting. Check with a one-line probe before planning around it.

## [2026-09-30] Do not edit YAML frontmatter lists with dotall regex

**What broke:** A `python3` one-liner used `re.sub` with the `(?s)` flag to dedupe the `related:` list in `wiki/concepts/fdm-printing.md`. With `(?s)`, `.` matches newlines, so the pattern ran past the list and swallowed the whole document. 177 lines became 113.

**Recovery:** `git show HEAD:<path> > <path>`. The file was clean at HEAD, so this was safe. Always check `git status` first.

**What to do:** Use the Edit tool with exact strings for frontmatter surgery. If a script is truly needed, drop the `s` flag and anchor both ends. After any scripted write to a wiki page, check the line count against the previous value.
