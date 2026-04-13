#!/usr/bin/env python3
"""Validate Ephemeride language files."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_LANGUAGES = ["fr", "en", "de", "es", "it", "pt"]


def main() -> int:
    base = ROOT / "custom_components" / "ephemeride" / "languages"
    expected_days = 366
    errors: list[str] = []

    for language in SUPPORTED_LANGUAGES:
        file_path = base / f"{language}.json"
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
        except Exception as err:  # pragma: no cover - CLI guard
            errors.append(f"{language}: lecture impossible - {err}")
            continue

        if len(data) != expected_days:
            errors.append(f"{language}: {len(data)} dates au lieu de {expected_days}")

        for day, entries in sorted(data.items()):
            if not isinstance(entries, list):
                errors.append(f"{language} {day}: la valeur doit etre une liste")
                continue

            for entry in entries:
                if isinstance(entry, str):
                    if not entry.strip():
                        errors.append(f"{language} {day}: chaine vide")
                    continue

                if isinstance(entry, list) and len(entry) > 2:
                    errors.append(f"{language} {day}: entree tuple trop longue {entry}")
                if isinstance(entry, list) and not entry:
                    errors.append(f"{language} {day}: liste vide")
                if isinstance(entry, list) and entry and not str(entry[0]).strip():
                    errors.append(f"{language} {day}: nom vide dans {entry}")
                if isinstance(entry, dict) and not (entry.get("nom") or entry.get("name")):
                    errors.append(f"{language} {day}: entree objet sans nom {entry}")
                if not isinstance(entry, (str, list, dict)):
                    errors.append(f"{language} {day}: type non supporte {type(entry).__name__}")

    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation OK for", ", ".join(SUPPORTED_LANGUAGES))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
