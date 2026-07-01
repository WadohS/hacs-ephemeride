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
SENSOR_SAINTS_NAME = "saints_du_jour"
SENSOR_SAINT_NAME = "saint_du_jour"
SENSOR_SAINTE_NAME = "sainte_du_jour"
SENSOR_FETE_NAME = "fete_du_jour"
SENSOR_DATE_RELIGIEUSE_NAME = "date_religieuse_du_jour"
SENSOR_PRENOM_NAME = "prenom_du_jour"
SENSOR_AUTRE_NAME = "autre_du_jour"

CATEGORY_SAINT = "saint"
CATEGORY_SAINTE = "sainte"
CATEGORY_FETE = "fete"
CATEGORY_DATE_RELIGIEUSE = "date_religieuse"
CATEGORY_PRENOM = "prenom"
CATEGORY_AUTRE = "autre"

CATEGORY_SENSOR_KEYS = [
    CATEGORY_SAINT,
    CATEGORY_SAINTE,
    CATEGORY_FETE,
    CATEGORY_DATE_RELIGIEUSE,
    CATEGORY_PRENOM,
    CATEGORY_AUTRE,
]

EXPLICIT_TYPE_ALIASES = {
    "saint": CATEGORY_SAINT,
    "sainte": CATEGORY_SAINTE,
    CATEGORY_SAINT: CATEGORY_SAINT,
    CATEGORY_SAINTE: CATEGORY_SAINTE,
    "fete": CATEGORY_FETE,
    CATEGORY_FETE: CATEGORY_FETE,
    "feest": CATEGORY_FETE,
    "feast": CATEGORY_FETE,
    "fest": CATEGORY_FETE,
    "date religieuse": CATEGORY_DATE_RELIGIEUSE,
    CATEGORY_DATE_RELIGIEUSE: CATEGORY_DATE_RELIGIEUSE,
    "religious date": CATEGORY_DATE_RELIGIEUSE,
    "prenom": CATEGORY_PRENOM,
    CATEGORY_PRENOM: CATEGORY_PRENOM,
    "name day": CATEGORY_PRENOM,
    "given name": CATEGORY_PRENOM,
    CATEGORY_AUTRE: CATEGORY_AUTRE,
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
        "our lady",
        "candlemas",
        "name of jesus",
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
        "maria namen",
        "maria",
        "weihnacht",
        "erscheinung des herrn",
        "allerheiligen",
        "maria himmelfahrt",
    ],
    "es": [
        "epifania",
        "madre de dios",
        "nuestra senora",
        "nombre de jesus",
        "candelaria",
        "navidad",
        "asuncion",
        "todos los santos",
        "inmaculada",
        "presentacion",
    ],
    "it": [
        "epifania",
        "madre di dio",
        "madonna",
        "nome di gesu",
        "befana",
        "capodanno",
        "natale",
        "assunzione",
        "tutti i santi",
        "immacolata",
    ],
    "pt": [
        "epifania",
        "mae de deus",
        "nossa senhora",
        "nome de jesus",
        "candelaria",
        "natal",
        "assuncao",
        "todos os santos",
        "imaculada",
        "apresentacao",
        "conversao",
    ],
}

SAINT_PREFIX_KEYWORDS = {
    "fr": {"saint": CATEGORY_SAINT, "sainte": CATEGORY_SAINTE},
    "en": {"saint": CATEGORY_SAINT},
    "de": {"heilige": CATEGORY_SAINTE, "heiliger": CATEGORY_SAINT, "sankt": CATEGORY_SAINT},
    "es": {"san ": CATEGORY_SAINT, "santa": CATEGORY_SAINTE, "santo": CATEGORY_SAINT},
    "it": {"san ": CATEGORY_SAINT, "santa": CATEGORY_SAINTE, "santo": CATEGORY_SAINT},
    "pt": {"santa": CATEGORY_SAINTE, "santo": CATEGORY_SAINT, "sao ": CATEGORY_SAINT},
}

FEMALE_NAME_HINTS = {
    "en": {
        "mary", "genevieve", "elizabeth", "marguerite", "prisca", "martha", "agnes", "angela",
        "martina", "brigid", "agatha", "scholastica", "bernadette", "juliana", "isabella",
        "catherine", "teresa", "lucy", "clare", "monica", "cecilia", "barbara", "agnes",
        "anne", "anna", "joan", "jane", "helena", "rosa", "rose", "margaret", "magdalene",
    },
    "de": {
        "maria", "genoveva", "irma", "angelika", "christiane", "emilia", "gudula", "alice",
        "leonie", "tatjana", "jutta", "rosalind", "margitta", "martha", "agnes", "katharina",
        "theresia", "barbara", "elisabeth", "anna", "johanna", "margareta", "klara", "cecilia",
    },
    "es": {
        "maria", "genoveva", "angela", "emiliana", "tatiana", "rosalina", "beatriz", "catalina",
        "teresa", "lucia", "ana", "ines", "marta", "prisca", "eulalia", "agueda", "monica",
        "clara", "isabel", "paula", "margarita", "magdalena", "dolores", "consuelo",
    },
    "it": {
        "maria", "angela", "margherita", "prisca", "marta", "agnese", "emerenziana", "martina",
        "aldegonda", "chiara", "teresa", "caterina", "barbara", "lucia", "monica", "rita",
        "anna", "cecilia", "elisabetta", "paola", "rosalia", "scolastica",
    },
    "pt": {
        "maria", "genoveva", "angela", "basilissa", "tatiana", "margarida", "marta", "ines",
        "joana", "catarina", "teresa", "lucia", "ana", "paula", "eulalia", "agata", "beatriz",
        "rosa", "cecilia", "isabel", "helena", "juliana", "monica",
    },
}

FEMALE_SUFFIX_HINTS = {
    "en": ("a", "ia", "ina", "ella", "ette", "ine", "ica", "tha", "trix", "ene", "eve"),
    "de": ("a", "ia", "ina", "ika", "ine", "lind", "gund", "trud", "hild"),
    "es": ("a",),
    "it": ("a",),
    "pt": ("a",),
}

MALE_SUFFIX_EXCEPTIONS = {
    "es": {"elia", "eustaquia"},
    "it": {"luca", "andrea", "elia", "nicola"},
    "pt": {"elia", "nicola"},
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
        "general": "Saints du jour",
        CATEGORY_SAINT: "Saint du jour",
        CATEGORY_SAINTE: "Sainte du jour",
        CATEGORY_FETE: "Fête du jour",
        CATEGORY_DATE_RELIGIEUSE: "Date religieuse du jour",
        CATEGORY_PRENOM: "Prénom du jour",
        CATEGORY_AUTRE: "Autre du jour",
    },
    "en": {
        "general": "Saints of the day",
        CATEGORY_SAINT: "Saint of the day",
        CATEGORY_SAINTE: "Female saint of the day",
        CATEGORY_FETE: "Feast of the day",
        CATEGORY_DATE_RELIGIEUSE: "Religious date of the day",
        CATEGORY_PRENOM: "Name of the day",
        CATEGORY_AUTRE: "Other commemoration of the day",
    },
    "de": {
        "general": "Heilige des Tages",
        CATEGORY_SAINT: "Heiliger des Tages",
        CATEGORY_SAINTE: "Heilige des Tages",
        CATEGORY_FETE: "Fest des Tages",
        CATEGORY_DATE_RELIGIEUSE: "Religioses Datum des Tages",
        CATEGORY_PRENOM: "Vorname des Tages",
        CATEGORY_AUTRE: "Andere Gedenkfeier des Tages",
    },
    "es": {
        "general": "Santos del dia",
        CATEGORY_SAINT: "Santo del dia",
        CATEGORY_SAINTE: "Santa del dia",
        CATEGORY_FETE: "Fiesta del dia",
        CATEGORY_DATE_RELIGIEUSE: "Fecha religiosa del dia",
        CATEGORY_PRENOM: "Nombre del dia",
        CATEGORY_AUTRE: "Otro evento del dia",
    },
    "it": {
        "general": "Santi del giorno",
        CATEGORY_SAINT: "Santo del giorno",
        CATEGORY_SAINTE: "Santa del giorno",
        CATEGORY_FETE: "Festa del giorno",
        CATEGORY_DATE_RELIGIEUSE: "Data religiosa del giorno",
        CATEGORY_PRENOM: "Nome del giorno",
        CATEGORY_AUTRE: "Altro evento del giorno",
    },
    "pt": {
        "general": "Santos do dia",
        CATEGORY_SAINT: "Santo do dia",
        CATEGORY_SAINTE: "Santa do dia",
        CATEGORY_FETE: "Festa do dia",
        CATEGORY_DATE_RELIGIEUSE: "Data religiosa do dia",
        CATEGORY_PRENOM: "Nome do dia",
        CATEGORY_AUTRE: "Outro evento do dia",
    },
}

INTEGRATION_VERSION = "1.4.4"
