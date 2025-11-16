from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import textwrap

@dataclass
class Problem:
    id: str
    title: str
    problem: str
    solution: str

@dataclass
class Chapter:
    name: str
    slug: str
    problems: list[Problem]

chapters: list[Chapter] = []


def to_markdown(text: str) -> str:
    lines = textwrap.dedent(text).strip().splitlines()
    output: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            output.append("")
            continue
        if stripped[0] in {"-", "*"}:
            output.append(stripped)
        else:
            output.append(stripped)
    # collapse multiple blanks
    collapsed: list[str] = []
    blank = False
    for line in output:
        if not line:
            if not blank:
                collapsed.append("")
            blank = True
        else:
            collapsed.append(line)
            blank = False
    return "\n".join(collapsed).strip()


def write_documents(base_dir: Path) -> None:
    problems_lines: list[str] = ["# Compiled Exercises\n"]
    for chapter in chapters:
        problems_lines.append(f"## {chapter.name}")
        for idx, item in enumerate(chapter.problems, start=1):
            problems_lines.append(f"{idx}. **Exercise {item.id}** (_{item.title}_)\n")
            problems_lines.append(to_markdown(item.problem))
            problems_lines.append("")
    (base_dir / "compiled_problems.md").write_text("\n".join(problems_lines).strip() + "\n")

    for chapter in chapters:
        sol_lines: list[str] = [f"# Solutions — {chapter.name}"]
        for idx, item in enumerate(chapter.problems, start=1):
            sol_lines.append(f"{idx}. **Exercise {item.id}** (_{item.title}_)")
            sol_lines.append(to_markdown(item.solution))
            sol_lines.append("")
        (base_dir / f"{chapter.slug}_solutions.md").write_text("\n".join(sol_lines).strip() + "\n")


if __name__ == "__main__":
    if not chapters:
        raise SystemExit("No chapters defined")
    write_documents(Path.cwd())
