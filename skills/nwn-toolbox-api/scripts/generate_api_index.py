#!/usr/bin/env python3
"""Regenerate reference/api-index.md from an NWN.Toolbox source checkout.

The index is a flat, greppable listing of every *public* type and member under the
Jorteck.Toolbox namespace — i.e. exactly the surface a consuming plugin can touch.
Internal types are deliberately excluded: if it isn't in this file, a downstream
plugin cannot reference it, and the correct answer is "that isn't part of the API"
rather than "let me read the Toolbox source".

Usage:
    python3 scripts/generate_api_index.py /path/to/NWN.Toolbox
    python3 scripts/generate_api_index.py /path/to/NWN.Toolbox -o reference/api-index.md

The argument is the root of an NWN.Toolbox git checkout (the directory containing
NWN.Toolbox.sln). Regenerate after upgrading the NWN.Toolbox package so the index
matches the version consuming projects actually reference.
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
NON_PUBLIC_TYPE_RE = re.compile(
    r"^(\s*)(?:internal|private)\s+"
    r"(?:abstract\s+|sealed\s+|static\s+|partial\s+|unsafe\s+|readonly\s+|ref\s+)*"
    r"(class|interface|enum|struct|record)\s+([\w<>,\s]+?)(?:\s*:\s*.*)?$"
)
NAMESPACE_RE = re.compile(r"namespace\s+([\w\.]+)")
ENUM_MEMBER_RE = re.compile(r"^([A-Z_]\w*)\s*(?:=\s*[^,]+)?,?\s*$")
TRAILER_RE = re.compile(r"\s*(\{.*|=>.*|;.*)$")
MEMBER_RE = re.compile(r"^(public|protected)\s+")
# Interface members carry no access modifier, so match a declaration shape instead:
# "<type> <Name>(" or "<type> <Name> { get" / "<type> <Name>;".
INTERFACE_MEMBER_RE = re.compile(
    r"^(?:new\s+|static\s+|public\s+)*"
    r"[\w<>\[\]\?,\.\s]+?\s+\w+(?:<[\w,\s]+>)?\s*(?:\(|\{\s*get|\{\s*set|=>|;)"
)
NOISE_PREFIXES = ("//", "/*", "*", "[", "{", "}", "#", "using ")

# EF Core migrations are generated code (one of them is nominally public, hence the
# deliberate skip rather than relying on the internal filter), and the YAML plumbing is
# an implementation detail that no consumer calls.
SKIP_DIR_MARKERS = ("/Migrations/", "/Serialization/")

NAMESPACE_PREFIX = "Jorteck.Toolbox"


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
        in_interface = False
        # Indent depth of the innermost non-public type we're inside, or None.
        # A public type nested in an internal one is unreachable from another
        # assembly, so it must not appear in the index.
        suppress_indent = None
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            stripped = line.strip()

            ns_match = NAMESPACE_RE.match(stripped)
            if ns_match:
                namespace = ns_match.group(1)
                continue

            # An internal/private type ends the current public type's member run,
            # so members of a non-public type are never misattributed, and opens
            # a suppression scope covering anything nested inside it.
            non_public_match = NON_PUBLIC_TYPE_RE.match(line)
            if non_public_match:
                indent = len(non_public_match.group(1))
                if suppress_indent is None or indent <= suppress_indent:
                    suppress_indent = indent
                current = None
                in_enum = False
                in_interface = False
                continue

            type_match = TYPE_RE.match(line)
            if type_match:
                indent = len(type_match.group(1))
                if suppress_indent is not None:
                    if indent > suppress_indent:
                        continue  # public type nested in a non-public one
                    suppress_indent = None
                kind, name = type_match.group(2), type_match.group(3).strip()
                current = f"{namespace}.{name}"
                in_enum = kind == "enum"
                in_interface = kind == "interface"
                types.setdefault(
                    current,
                    {"kind": kind, "members": [], "enum": [], "file": str(path.relative_to(src_root))},
                )
                continue

            if current is None:
                continue

            if in_enum:
                enum_match = ENUM_MEMBER_RE.match(stripped)
                if enum_match:
                    types[current]["enum"].append(enum_match.group(1))
                continue

            if TYPE_RE.match(line):
                continue

            is_member = MEMBER_RE.match(stripped) or (
                in_interface
                and not stripped.startswith(NOISE_PREFIXES)
                and INTERFACE_MEMBER_RE.match(stripped)
            )
            if is_member:
                signature = TRAILER_RE.sub("", stripped).strip()
                signature = re.sub(r"^public\s+", "", signature)
                if signature:
                    types[current]["members"].append(signature)
    return types


def render(types, version: str) -> str:
    lines = [
        "# NWN.Toolbox public API index",
        "",
        f"Generated from NWN.Toolbox `{version}`.",
        "",
        "One `##` heading per **public** type in `Jorteck.Toolbox`, with its public and",
        "protected members bulleted beneath and enum values inlined. Internal types, types",
        "nested inside internal types, and generated EF migration code are excluded on",
        "purpose — if a type isn't listed here, a consuming plugin either cannot reference",
        "it or has no reason to, and the answer is \"that's not part of the API\" rather than",
        "\"read the source\".",
        "",
        "Grep this rather than reading it:",
        "",
        "```",
        "rg -A 40 '^## Jorteck\\.Toolbox\\.Core\\.WindowController' reference/api-index.md",
        "rg 'ApplyPermissionBindings' reference/api-index.md      # which type exposes a member",
        "rg '^## Jorteck\\.Toolbox\\.Features\\.Chat' reference/api-index.md",
        "```",
        "",
        "Signatures are extracted textually, so a member declared across multiple lines may",
        "be truncated, and interface default-implementations appear without their bodies.",
        "The `[file]` note on each heading points at the defining source file if you do need",
        "to confirm behaviour.",
        "",
        "Regenerate with `python3 scripts/generate_api_index.py /path/to/NWN.Toolbox`.",
    ]
    for key, value in types.items():
        if not key.startswith(NAMESPACE_PREFIX):
            continue
        if value["kind"] == "enum":
            lines.append(f"\n## {key}  [enum]  ({value['file']})")
            if value["enum"]:
                lines.append("- values: " + ", ".join(dict.fromkeys(value["enum"])))
            continue
        lines.append(f"\n## {key}  [{value['kind']}]  ({value['file']})")
        for member in dict.fromkeys(value["members"]):
            lines.append(f"- {member}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("toolbox_root", type=pathlib.Path, help="Root of an NWN.Toolbox checkout")
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parent.parent / "reference" / "api-index.md",
    )
    args = parser.parse_args()

    src_root = args.toolbox_root / "NWN.Toolbox" / "src"
    if not src_root.is_dir():
        print(
            f"error: {src_root} not found — is {args.toolbox_root} an NWN.Toolbox checkout?",
            file=sys.stderr,
        )
        return 1

    version = describe_version(args.toolbox_root)
    types = collect(src_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(types, version), encoding="utf-8")

    public_types = sum(1 for key in types if key.startswith(NAMESPACE_PREFIX))
    print(f"wrote {args.output} — {public_types} public types from NWN.Toolbox {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
