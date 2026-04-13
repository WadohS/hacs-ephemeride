"""Movable liturgical dates for Ephemeride."""
from __future__ import annotations

from datetime import date, timedelta

from .const import CATEGORY_DATE_RELIGIEUSE, CATEGORY_FETE


LITURGICAL_LABELS = {
    "fr": {
        "ash_wednesday": ("Mercredi des Cendres", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("1er dimanche de Careme", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Dimanche des Rameaux", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Jeudi Saint", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Vendredi Saint", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Samedi Saint", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Paques", CATEGORY_FETE),
        "easter_monday": ("Lundi de Paques", CATEGORY_FETE),
        "ascension": ("Ascension", CATEGORY_FETE),
        "pentecost": ("Pentecote", CATEGORY_FETE),
        "pentecost_monday": ("Lundi de Pentecote", CATEGORY_FETE),
        "trinity": ("Sainte Trinite", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Fete-Dieu", CATEGORY_FETE),
        "sacred_heart": ("Sacre-Coeur", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Christ Roi", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("1er dimanche de l'Avent", CATEGORY_DATE_RELIGIEUSE),
    },
    "en": {
        "ash_wednesday": ("Ash Wednesday", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("First Sunday of Lent", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Palm Sunday", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Holy Thursday", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Good Friday", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Holy Saturday", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Easter", CATEGORY_FETE),
        "easter_monday": ("Easter Monday", CATEGORY_FETE),
        "ascension": ("Ascension", CATEGORY_FETE),
        "pentecost": ("Pentecost", CATEGORY_FETE),
        "pentecost_monday": ("Pentecost Monday", CATEGORY_FETE),
        "trinity": ("Trinity Sunday", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Corpus Christi", CATEGORY_FETE),
        "sacred_heart": ("Sacred Heart", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Christ the King", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("First Sunday of Advent", CATEGORY_DATE_RELIGIEUSE),
    },
    "de": {
        "ash_wednesday": ("Aschermittwoch", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("Erster Fastensonntag", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Palmsonntag", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Grundonnerstag", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Karfreitag", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Karsamstag", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Ostern", CATEGORY_FETE),
        "easter_monday": ("Ostermontag", CATEGORY_FETE),
        "ascension": ("Christi Himmelfahrt", CATEGORY_FETE),
        "pentecost": ("Pfingsten", CATEGORY_FETE),
        "pentecost_monday": ("Pfingstmontag", CATEGORY_FETE),
        "trinity": ("Dreifaltigkeitssonntag", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Fronleichnam", CATEGORY_FETE),
        "sacred_heart": ("Heiligstes Herz Jesu", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Christkonigssonntag", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("Erster Advent", CATEGORY_DATE_RELIGIEUSE),
    },
    "es": {
        "ash_wednesday": ("Miercoles de Ceniza", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("Primer Domingo de Cuaresma", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Domingo de Ramos", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Jueves Santo", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Viernes Santo", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Sabado Santo", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Pascua", CATEGORY_FETE),
        "easter_monday": ("Lunes de Pascua", CATEGORY_FETE),
        "ascension": ("Ascension", CATEGORY_FETE),
        "pentecost": ("Pentecostes", CATEGORY_FETE),
        "pentecost_monday": ("Lunes de Pentecostes", CATEGORY_FETE),
        "trinity": ("Santisima Trinidad", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Corpus Christi", CATEGORY_FETE),
        "sacred_heart": ("Sagrado Corazon", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Cristo Rey", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("Primer Domingo de Adviento", CATEGORY_DATE_RELIGIEUSE),
    },
    "it": {
        "ash_wednesday": ("Mercoledi delle Ceneri", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("Prima Domenica di Quaresima", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Domenica delle Palme", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Giovedi Santo", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Venerdi Santo", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Sabato Santo", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Pasqua", CATEGORY_FETE),
        "easter_monday": ("Lunedi dell'Angelo", CATEGORY_FETE),
        "ascension": ("Ascensione", CATEGORY_FETE),
        "pentecost": ("Pentecoste", CATEGORY_FETE),
        "pentecost_monday": ("Lunedi di Pentecoste", CATEGORY_FETE),
        "trinity": ("Santissima Trinita", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Corpus Domini", CATEGORY_FETE),
        "sacred_heart": ("Sacro Cuore", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Cristo Re", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("Prima Domenica di Avvento", CATEGORY_DATE_RELIGIEUSE),
    },
    "pt": {
        "ash_wednesday": ("Quarta-feira de Cinzas", CATEGORY_DATE_RELIGIEUSE),
        "lent_1": ("Primeiro Domingo da Quaresma", CATEGORY_DATE_RELIGIEUSE),
        "palm_sunday": ("Domingo de Ramos", CATEGORY_DATE_RELIGIEUSE),
        "holy_thursday": ("Quinta-feira Santa", CATEGORY_DATE_RELIGIEUSE),
        "good_friday": ("Sexta-feira Santa", CATEGORY_DATE_RELIGIEUSE),
        "holy_saturday": ("Sabado Santo", CATEGORY_DATE_RELIGIEUSE),
        "easter": ("Pascoa", CATEGORY_FETE),
        "easter_monday": ("Segunda-feira de Pascoa", CATEGORY_FETE),
        "ascension": ("Ascensao", CATEGORY_FETE),
        "pentecost": ("Pentecostes", CATEGORY_FETE),
        "pentecost_monday": ("Segunda-feira de Pentecostes", CATEGORY_FETE),
        "trinity": ("Santissima Trindade", CATEGORY_DATE_RELIGIEUSE),
        "corpus_christi": ("Corpus Christi", CATEGORY_FETE),
        "sacred_heart": ("Sagrado Coracao", CATEGORY_DATE_RELIGIEUSE),
        "christ_king": ("Cristo Rei", CATEGORY_DATE_RELIGIEUSE),
        "advent_1": ("Primeiro Domingo do Advento", CATEGORY_DATE_RELIGIEUSE),
    },
}


def compute_easter_sunday(year: int) -> date:
    """Return Easter Sunday for the Gregorian calendar."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def get_movable_liturgical_days(year: int, language: str) -> dict[str, list[dict[str, str]]]:
    """Return movable liturgical dates for a given year and language."""
    labels = LITURGICAL_LABELS.get(language, LITURGICAL_LABELS["fr"])
    easter = compute_easter_sunday(year)
    christmas = date(year, 12, 25)
    advent_start = christmas - timedelta(days=christmas.weekday() + 22)

    events = {
        "ash_wednesday": easter - timedelta(days=46),
        "lent_1": easter - timedelta(days=42),
        "palm_sunday": easter - timedelta(days=7),
        "holy_thursday": easter - timedelta(days=3),
        "good_friday": easter - timedelta(days=2),
        "holy_saturday": easter - timedelta(days=1),
        "easter": easter,
        "easter_monday": easter + timedelta(days=1),
        "ascension": easter + timedelta(days=39),
        "pentecost": easter + timedelta(days=49),
        "pentecost_monday": easter + timedelta(days=50),
        "trinity": easter + timedelta(days=56),
        "corpus_christi": easter + timedelta(days=60),
        "sacred_heart": easter + timedelta(days=68),
        "christ_king": advent_start - timedelta(days=28),
        "advent_1": advent_start,
    }

    result: dict[str, list[dict[str, str]]] = {}
    for key, event_date in events.items():
        name, category = labels[key]
        result.setdefault(event_date.strftime("%m-%d"), []).append(
            {"name": name, "type": category}
        )
    return result
