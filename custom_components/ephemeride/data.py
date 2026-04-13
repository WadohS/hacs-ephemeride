"""Pure data helpers for Ephemeride language files."""
from __future__ import annotations

from collections.abc import Iterable
import unicodedata

from .const import (
    CATEGORY_AUTRE,
    CATEGORY_DATE_RELIGIEUSE,
    CATEGORY_FETE,
    CATEGORY_SAINT,
    CATEGORY_SAINTE,
    CATEGORY_SENSOR_KEYS,
    DATE_RELIGIEUSE_KEYWORDS,
    EXPLICIT_TYPE_ALIASES,
    FETE_KEYWORDS,
)


def strip_accents(value: str) -> str:
    """Return a lowercase ASCII-friendly representation for matching."""
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()


def normalize_entry(raw_entry: object, language: str) -> dict[str, str | None]:
    """Normalize a raw language entry into a typed structure."""
    name = ""
    raw_type = None

    if isinstance(raw_entry, dict):
        name = str(raw_entry.get("nom") or raw_entry.get("name") or "").strip()
        raw_type = raw_entry.get("type")
        if raw_type is not None:
            raw_type = str(raw_type).strip()
    elif isinstance(raw_entry, list):
        if raw_entry:
            name = str(raw_entry[0]).strip()
        if len(raw_entry) > 1 and raw_entry[1] is not None:
            raw_type = str(raw_entry[1]).strip()
    else:
        name = str(raw_entry).strip()

    category = classify_entry(name, raw_type, language)
    return {
        "name": name or "Inconnu",
        "raw_type": raw_type,
        "category": category,
    }


def classify_entry(name: str, raw_type: str | None, language: str) -> str:
    """Classify a single entry while keeping locale-specific data intact."""
    if raw_type:
        normalized_type = strip_accents(raw_type)
        for key, category in EXPLICIT_TYPE_ALIASES.items():
            if normalized_type == key:
                return category

    normalized_name = strip_accents(name)

    if matches_keywords(normalized_name, DATE_RELIGIEUSE_KEYWORDS.get(language, [])):
        return CATEGORY_DATE_RELIGIEUSE

    if matches_keywords(normalized_name, FETE_KEYWORDS.get(language, [])):
        return CATEGORY_FETE

    if raw_type is None:
        return CATEGORY_AUTRE

    return CATEGORY_AUTRE


def matches_keywords(value: str, keywords: Iterable[str]) -> bool:
    """Return True if one of the normalized keywords is present."""
    return any(keyword in value for keyword in keywords)


def build_day_payload(raw_entries: list[object], language: str) -> dict[str, object]:
    """Build typed payload and category splits for a day."""
    entries = [normalize_entry(entry, language) for entry in raw_entries if entry]
    names = [entry["name"] for entry in entries[:5]]

    by_category: dict[str, dict[str, object]] = {}
    for category in CATEGORY_SENSOR_KEYS:
        category_entries = [entry for entry in entries if entry["category"] == category]
        by_category[category] = {
            "entries": category_entries[:5],
            "names": [entry["name"] for entry in category_entries[:5]],
            "count": len(category_entries),
            "first": category_entries[0]["name"] if category_entries else "Inconnu",
            "first_type": category_entries[0]["raw_type"] if category_entries else None,
        }

    return {
        "entries": entries[:5],
        "names": names,
        "count": len(entries),
        "first": entries[0]["name"] if entries else "Inconnu",
        "first_type": entries[0]["raw_type"] if entries else None,
        "by_category": by_category,
    }
