#!/usr/bin/env python3
"""Convert a language file to explicit object entries."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import types

ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def bootstrap_package() -> None:
    custom_components = types.ModuleType("custom_components")
    custom_components.__path__ = [str(ROOT / "custom_components")]
    sys.modules["custom_components"] = custom_components

    ephemeride = types.ModuleType("custom_components.ephemeride")
    ephemeride.__path__ = [str(ROOT / "custom_components" / "ephemeride")]
    sys.modules["custom_components.ephemeride"] = ephemeride


def build_output(entry: object, language: str, data_module) -> dict[str, str]:
    normalized = data_module.normalize_entry(entry, language)
    output = {"name": normalized["name"], "type": normalized["category"]}
    if normalized["raw_type"]:
        output["source_type"] = normalized["raw_type"]
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert one Ephemeride language file to object entries")
    parser.add_argument("language", help="Language code, for example fr or en")
    parser.add_argument("--write", action="store_true", help="Write changes in place")
    args = parser.parse_args()

    bootstrap_package()
    load_module("custom_components.ephemeride.const", "custom_components/ephemeride/const.py")
    data_module = load_module("custom_components.ephemeride.data", "custom_components/ephemeride/data.py")

    file_path = ROOT / "custom_components" / "ephemeride" / "languages" / f"{args.language}.json"
    content = json.loads(file_path.read_text(encoding="utf-8"))

    converted = {
        day: [build_output(entry, args.language, data_module) for entry in entries]
        for day, entries in content.items()
    }

    rendered = json.dumps(converted, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.write:
        file_path.write_text(rendered, encoding="utf-8")
        print(f"Updated {file_path}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
