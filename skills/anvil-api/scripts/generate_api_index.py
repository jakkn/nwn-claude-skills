#!/usr/bin/env python3
"""Regenerate reference/api-index.md from an Anvil source checkout.

The index is a flat, greppable listing of every public type and member in the
Anvil.API and Anvil.Services namespaces. It exists so agents can answer "does this
method exist / what's its signature" with one ripgrep instead of crawling 800 source
files.

Usage:
    python3 scripts/generate_api_index.py /path/to/Anvil
    python3 scripts/generate_api_index.py /path/to/Anvil -o reference/api-index.md

The argument is the root of an Anvil git checkout (the directory containing
NWN.Anvil.sln). Regenerate after upgrading the NWN.Anvil package so the index matches
the version the project actually references.
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import subprocess
import sys

TYPE_RE = re.compile(
    r"^(\s*)(?:public|protected)\s+"
    r"(?:abstract\s+|sealed\s+|static\s+|partial\s+|unsafe\s+|readonly\s+|ref\s+)*"
    r"(class|interface|enum|struct|record)\s+([\w<>,\s]+?)(?:\s*:\s*.*)?$"
)
NAMESPACE_RE = re.compile(r"namespace\s+([\w\.]+)")
ENUM_MEMBER_RE = re.compile(r"^([A-Z_]\w*)\s*(?:=\s*[^,]+)?,?\s*$")
TRAILER_RE = re.compile(r"\s*(\{.*|=>.*|;.*)$")

# Internals and the raw native bindings are noise for a consumer-facing index.
SKIP_DIR_MARKERS = ("/Internal/", "/Native/", "/lib/")


def describe_version(repo: pathlib.Path) -> str:
    for args in (["git", "describe", "--tags"], ["git", "rev-parse", "--short", "HEAD"]):
        try:
            out = subprocess.run(
                args, cwd=repo, capture_output=True, text=True, check=True, timeout=15
            )
            return out.stdout.strip()
        except (subprocess.SubprocessError, OSError):
            continue
    return "unknown"


def collect(src_root: pathlib.Path) -> "collections.OrderedDict[str, dict]":
    types: collections.OrderedDict[str, dict] = collections.OrderedDict()
    for path in sorted(src_root.rglob("*.cs")):
        if any(marker in str(path) for marker in SKIP_DIR_MARKERS):
            continue
        namespace = None
        current = None
        in_enum = False
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            stripped = line.strip()

            ns_match = NAMESPACE_RE.match(stripped)
            if ns_match:
                namespace = ns_match.group(1)
                continue

            type_match = TYPE_RE.match(line)
            if type_match:
                kind, name = type_match.group(2), type_match.group(3).strip()
                current = f"{namespace}.{name}"
                in_enum = kind == "enum"
                types.setdefault(current, {"kind": kind, "members": [], "enum": []})
                continue

            if current is None:
                continue

            if in_enum:
                enum_match = ENUM_MEMBER_RE.match(stripped)
                if enum_match:
                    types[current]["enum"].append(enum_match.group(1))
                continue

            if stripped.startswith("public ") and not TYPE_RE.match(line):
                signature = TRAILER_RE.sub("", stripped).strip()
                signature = re.sub(r"^public\s+", "", signature)
                if signature:
                    types[current]["members"].append(signature)
    return types


def render(types, version: str) -> str:
    lines = [
        "# Anvil public API index",
        "",
        f"Generated from Anvil `{version}`.",
        "",
        "One `##` heading per public type in `Anvil.API` / `Anvil.Services`, with its public",
        "members bulleted beneath and enum values inlined. Grep this rather than reading it:",
        "",
        "```",
        "rg -A 60 '^## Anvil\\.API\\.NwCreature ' reference/api-index.md   # one type's members",
        "rg 'ApplyEffect' reference/api-index.md                          # which types expose a member",
        "rg '^## Anvil\\.API\\.\\w*Effect' reference/api-index.md            # types matching a pattern",
        "```",
        "",
        "Signatures are extracted textually, so a member declared across multiple lines may be",
        "truncated. Overload sets are complete. If something looks off, confirm against",
        "https://nwn-dotnet.github.io/Anvil/ before assuming the API is missing.",
        "",
        "Regenerate with `python3 scripts/generate_api_index.py /path/to/Anvil`.",
    ]
    for key, value in types.items():
        if not key.startswith("Anvil."):
            continue
        if value["kind"] == "enum":
            lines.append(f"\n## {key}  [enum]")
            if value["enum"]:
                lines.append("- values: " + ", ".join(dict.fromkeys(value["enum"])))
            continue
        lines.append(f"\n## {key}  [{value['kind']}]")
        for member in dict.fromkeys(value["members"]):
            lines.append(f"- {member}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("anvil_root", type=pathlib.Path, help="Root of an Anvil checkout")
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parent.parent / "reference" / "api-index.md",
    )
    args = parser.parse_args()

    src_root = args.anvil_root / "NWN.Anvil" / "src" / "main"
    if not src_root.is_dir():
        print(f"error: {src_root} not found — is {args.anvil_root} an Anvil checkout?", file=sys.stderr)
        return 1

    version = describe_version(args.anvil_root)
    types = collect(src_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(types, version), encoding="utf-8")

    public_types = sum(1 for key in types if key.startswith("Anvil."))
    print(f"wrote {args.output} — {public_types} types from Anvil {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
