"""Limited workshop lint: syntax, tabs, trailing space and line length only."""

import ast
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
MAX_LENGTH = 88


def main():
    paths = sorted(ROOT.glob("*.py")) + sorted((ROOT / "tests").glob("*.py"))
    findings = []
    for path in paths:
        source = path.read_text(encoding="utf-8")
        name = path.relative_to(ROOT)
        try:
            ast.parse(source, filename=str(name))
        except SyntaxError as error:
            findings.append(f"{name}:{error.lineno}: syntax: {error.msg}")
        for number, line in enumerate(source.splitlines(), 1):
            if "\t" in line:
                findings.append(f"{name}:{number}: tab character")
            if line.rstrip() != line:
                findings.append(f"{name}:{number}: trailing whitespace")
            if len(line) > MAX_LENGTH:
                findings.append(f"{name}:{number}: exceeds {MAX_LENGTH} characters")
    for finding in findings:
        print(finding)
    print(f"Checked {len(paths)} files; {len(findings)} findings.")
    print("Scope: root Python files and tests; syntax, tabs, trailing space, line length.")
    print("No business-rule, naming, security or test-coverage analysis is performed.")
    return bool(findings)


if __name__ == "__main__":
    sys.exit(main())
