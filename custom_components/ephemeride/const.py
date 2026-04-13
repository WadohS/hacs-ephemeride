"""Constantes pour l'intégration Éphéméride."""

DOMAIN = "ephemeride"
CONF_LANGUAGE = "language"
SUPPORTED_LANGUAGES = ["fr", "en", "de", "es", "it", "pt"]
LANGUAGE_OPTIONS = {
    "fr": "Français",
    "en": "English",
    "de": "Deutsch",
    "es": "Español",
    "it": "Italiano",
    "pt": "Português",
}
SENSOR_NAME = "saint_du_jour"
SENSOR_SAINT_MASCULIN_NAME = "saint_masculin_du_jour"
SENSOR_SAINTE_NAME = "sainte_du_jour"
SENSOR_FETE_NAME = "fete_du_jour"
SENSOR_DATE_RELIGIEUSE_NAME = "date_religieuse_du_jour"
SENSOR_AUTRE_NAME = "autre_du_jour"

CATEGORY_SAINT = "saint"
CATEGORY_SAINTE = "sainte"
CATEGORY_FETE = "fete"
CATEGORY_DATE_RELIGIEUSE = "date_religieuse"
CATEGORY_AUTRE = "autre"

CATEGORY_SENSOR_KEYS = [
    CATEGORY_SAINT,
    CATEGORY_SAINTE,
    CATEGORY_FETE,
    CATEGORY_DATE_RELIGIEUSE,
    CATEGORY_AUTRE,
]

EXPLICIT_TYPE_ALIASES = {
    "saint": CATEGORY_SAINT,
    "sainte": CATEGORY_SAINTE,
    "fete": CATEGORY_FETE,
    "feest": CATEGORY_FETE,
    "feast": CATEGORY_FETE,
    "fest": CATEGORY_FETE,
    "date religieuse": CATEGORY_DATE_RELIGIEUSE,
    "religious date": CATEGORY_DATE_RELIGIEUSE,
}

DATE_RELIGIEUSE_KEYWORDS = {
    "fr": [
        "cendres",
        "rameaux",
        "jeudi saint",
        "vendredi saint",
        "samedi saint",
        "lundi saint",
        "mardi saint",
        "dimanche de paques",
        "trinite",
        "sacre-coeur",
        "sacre coeur",
        "christ roi",
        "careme",
        "avent",
    ],
    "en": [
        "ash wednesday",
        "palm sunday",
        "holy thursday",
        "good friday",
        "holy saturday",
        "easter sunday",
        "trinity sunday",
        "advent",
        "lent",
    ],
    "de": [
        "aschermittwoch",
        "palmsonntag",
        "grundonnerstag",
        "karfreitag",
        "ostersonntag",
        "advent",
        "fastenzeit",
    ],
    "es": [
        "miercoles de ceniza",
        "domingo de ramos",
        "jueves santo",
        "viernes santo",
        "sabado santo",
        "domingo de pascua",
        "adviento",
        "cuaresma",
    ],
    "it": [
        "mercoledi delle ceneri",
        "domenica delle palme",
        "giovedi santo",
        "venerdi santo",
        "sabato santo",
        "pasqua",
        "avvento",
        "quaresima",
    ],
    "pt": [
        "quarta-feira de cinzas",
        "domingo de ramos",
        "quinta-feira santa",
        "sexta-feira santa",
        "sabado santo",
        "domingo de pascoa",
        "advento",
        "quaresma",
    ],
}

FETE_KEYWORDS = {
    "fr": [
        "epiphanie",
        "fete de la presentation",
        "jour de l'an",
        "assomption",
        "toussaint",
        "noel",
        "immaculee conception",
        "transfiguration",
        "nativite",
        "conversion de paul",
    ],
    "en": [
        "epiphany",
        "mother of god",
        "christmas",
        "assumption",
        "all saints",
        "immaculate conception",
        "presentation",
        "conversion",
    ],
    "de": [
        "neujahr",
        "heilige drei konige",
        "weihnacht",
        "erscheinung des herrn",
        "allerheiligen",
        "maria himmelfahrt",
    ],
    "es": [
        "epifania",
        "madre de dios",
        "navidad",
        "asuncion",
        "todos los santos",
        "inmaculada",
        "presentacion",
    ],
    "it": [
        "epifania",
        "madre di dio",
        "capodanno",
        "natale",
        "assunzione",
        "tutti i santi",
        "immacolata",
    ],
    "pt": [
        "epifania",
        "mae de deus",
        "natal",
        "assuncao",
        "todos os santos",
        "imaculada",
        "apresentacao",
        "conversao",
    ],
}

UNKNOWN_STATE = {
    "fr": "Inconnu",
    "en": "Unknown",
    "de": "Unbekannt",
    "es": "Desconocido",
    "it": "Sconosciuto",
    "pt": "Desconhecido",
}

ENTITY_TITLES = {
    "fr": {
        "general": "Saint du jour",
        CATEGORY_SAINT: "Saint masculin du jour",
        CATEGORY_SAINTE: "Sainte du jour",
        CATEGORY_FETE: "Fête du jour",
        CATEGORY_DATE_RELIGIEUSE: "Date religieuse du jour",
        CATEGORY_AUTRE: "Autre du jour",
    },
    "en": {
        "general": "Saint of the day",
        CATEGORY_SAINT: "Male saint of the day",
        CATEGORY_SAINTE: "Female saint of the day",
        CATEGORY_FETE: "Feast of the day",
        CATEGORY_DATE_RELIGIEUSE: "Religious date of the day",
        CATEGORY_AUTRE: "Other commemoration of the day",
    },
    "de": {
        "general": "Heiliger des Tages",
        CATEGORY_SAINT: "Mannlicher Heiliger des Tages",
        CATEGORY_SAINTE: "Heilige des Tages",
        CATEGORY_FETE: "Fest des Tages",
        CATEGORY_DATE_RELIGIEUSE: "Religioses Datum des Tages",
        CATEGORY_AUTRE: "Andere Gedenkfeier des Tages",
    },
    "es": {
        "general": "Santo del dia",
        CATEGORY_SAINT: "Santo masculino del dia",
        CATEGORY_SAINTE: "Santa del dia",
        CATEGORY_FETE: "Fiesta del dia",
        CATEGORY_DATE_RELIGIEUSE: "Fecha religiosa del dia",
        CATEGORY_AUTRE: "Otro evento del dia",
    },
    "it": {
        "general": "Santo del giorno",
        CATEGORY_SAINT: "Santo maschile del giorno",
        CATEGORY_SAINTE: "Santa del giorno",
        CATEGORY_FETE: "Festa del giorno",
        CATEGORY_DATE_RELIGIEUSE: "Data religiosa del giorno",
        CATEGORY_AUTRE: "Altro evento del giorno",
    },
    "pt": {
        "general": "Santo do dia",
        CATEGORY_SAINT: "Santo masculino do dia",
        CATEGORY_SAINTE: "Santa do dia",
        CATEGORY_FETE: "Festa do dia",
        CATEGORY_DATE_RELIGIEUSE: "Data religiosa do dia",
        CATEGORY_AUTRE: "Outro evento do dia",
    },
}

INTEGRATION_VERSION = "1.3.0"
