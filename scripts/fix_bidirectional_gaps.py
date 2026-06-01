#!/usr/bin/env python3
"""Add missing reverse edges in frontmatter related: to fix bidirectional gaps."""
import re
from collections import defaultdict
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
SKIP = {"index.md", "log.md", "dashboard.md"}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_related(fm_text):
    related = []
    in_rel = False
    for line in fm_text.splitlines():
        if line.strip() == "related:":
            in_rel = True
            continue
        if in_rel:
            if line.startswith("  - "):
                related.append(line[4:].strip())
            elif not line.startswith(" "):
                in_rel = False
    return related


def load_pages():
    pages = {}
    for p in WIKI.rglob("*.md"):
        rel = str(p.relative_to(WIKI))
        if rel in SKIP:
            continue
        text = p.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not m:
            continue
        related = parse_related(m.group(1))
        pages[rel] = {"path": p, "text": text, "related": related}
    return pages


def add_related(text, entry):
    if f"  - {entry}\n" in text or f"  - {entry}\r\n" in text:
        return text
    return re.sub(
        r"(related:\n(?:  - .+\n)+)",
        lambda m: m.group(1) + f"  - {entry}\n",
        text,
        count=1,
    )


def main():
    pages = load_pages()
    all_paths = set(pages)
    outbound = defaultdict(set)
    for src, data in pages.items():
        for tgt in data["related"]:
            tgt = tgt.lstrip("@")
            if tgt in all_paths:
                outbound[src].add(tgt)

    fixes = 0
    for src, tgts in outbound.items():
        for tgt in tgts:
            if src not in outbound.get(tgt, set()):
                new_text = add_related(pages[tgt]["text"], src)
                if new_text != pages[tgt]["text"]:
                    pages[tgt]["path"].write_text(new_text, encoding="utf-8")
                    pages[tgt]["text"] = new_text
                    pages[tgt]["related"].append(src)
                    outbound[tgt].add(src)
                    fixes += 1
                    print(f"  + {tgt} ← {src}")
    print(f"Fixed {fixes} gaps")


if __name__ == "__main__":
    main()
