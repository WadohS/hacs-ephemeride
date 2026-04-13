#!/usr/bin/env python3
"""Report typing coverage for Ephemeride language files."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import types

ROOT = Path(__file__).resolve().parents[1]
LANG_DIR = ROOT / "custom_components" / "ephemeride" / "languages"


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


def main() -> int:
    bootstrap_package()
    const = load_module("custom_components.ephemeride.const", "custom_components/ephemeride/const.py")
    data = load_module("custom_components.ephemeride.data", "custom_components/ephemeride/data.py")

    categories = const.CATEGORY_SENSOR_KEYS
    print("language,total,saint,sainte,fete,date_religieuse,autre")

    for language in const.SUPPORTED_LANGUAGES:
        content = json.loads((LANG_DIR / f"{language}.json").read_text(encoding="utf-8"))
        counts = {category: 0 for category in categories}
        total = 0

        for entries in content.values():
            for entry in entries:
                normalized = data.normalize_entry(entry, language)
                counts[normalized["category"]] += 1
                total += 1

        values = [str(counts[category]) for category in categories]
        print(",".join([language, str(total), *values]))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
