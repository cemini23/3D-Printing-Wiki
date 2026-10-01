# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-09-30] External model routing does not work inside the desktop sandbox

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
