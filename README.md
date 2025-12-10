# Éphéméride - Intégration Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Intégration pour afficher le saint du jour et les festivités dans Home Assistant avec support multilingue._

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

![Icône Éphéméride](https://raw.githubusercontent.com/WadohS/hacs-ephemeride/main/custom_components/ephemeride/icon.png)

## 🌟 Fonctionnalités

**Cette intégration créera les plateformes suivantes.**

Plateforme | Description
-- | --
`sensor` | Capteur affichant le saint du jour avec multiples attributs

### Capteur `sensor.saint_du_jour`

- **État** : Nom du saint principal du jour
- **Attributs** :
  - `saint_demain` : Saint de demain
  - `langue` : Langue configurée
  - `date` : Date actuelle
  - `tous_saints_aujourdhui` : Liste complète des saints du jour (limité à 5)
  - `tous_saints_demain` : Liste complète des saints de demain (limité à 5)
  - `nombre_saints_aujourdhui` : Nombre total de saints aujourd'hui
  - `nombre_saints_demain` : Nombre total de saints demain

## 🌍 Langues supportées

L'intégration supporte **6 langues** avec données complètes (366 jours) :

- 🇫🇷 **Français** (fr)
- 🇬🇧 **English** (en)
- 🇩🇪 **Deutsch** (de)
- 🇪🇸 **Español** (es)
- 🇮🇹 **Italiano** (it)
- 🇵🇹 **Português** (pt)

## 📦 Installation

### Via HACS (Recommandé)

#### Installation en 1 clic 🚀

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

**Cliquez sur le bouton ci-dessus** pour ajouter automatiquement l'intégration Éphéméride à votre Home Assistant !

#### Installation manuelle via HACS

Si le bouton ne fonctionne pas :

1. Ouvrez HACS dans votre interface Home Assistant
2. Allez dans "Intégrations"
3. Cliquez sur les 3 points en haut à droite ⋮
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL : `https://github.com/WadohS/hacs-ephemeride`
6. Catégorie : "Integration"
7. Recherchez "Éphéméride" et installez-le
8. Redémarrez Home Assistant

### Installation manuelle

1. Utilisez votre outil préféré pour ouvrir le répertoire de configuration de Home Assistant (où se trouve `configuration.yaml`)
2. Si vous n'avez pas de répertoire `custom_components`, créez-le
3. Dans le répertoire `custom_components`, créez un nouveau dossier appelé `ephemeride`
4. Téléchargez **tous** les fichiers depuis le répertoire `custom_components/ephemeride/` de ce dépôt
5. Placez-les dans le nouveau répertoire que vous venez de créer
6. Redémarrez Home Assistant

## ⚙️ Configuration

La configuration se fait entièrement via l'interface utilisateur :

### Configuration en 1 clic ⚡

[![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ephemeride)

**Cliquez sur le bouton ci-dessus** pour configurer automatiquement l'intégration !

### Configuration manuelle

1. Allez dans **Configuration** → **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **Éphéméride**
4. Sélectionnez votre langue préférée
5. Cliquez sur **Soumettre**

### Changer de langue

Pour modifier la langue après l'installation :

1. Allez dans **Configuration** → **Intégrations**
2. Trouvez **Éphéméride**
3. Cliquez sur **Options**
4. Sélectionnez la nouvelle langue
5. L'intégration se recharge automatiquement

## 🎨 Exemples d'utilisation

### Carte Lovelace simple

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint du jour
icon: mdi:calendar-star
```

### Carte avec saint de demain

```yaml
type: markdown
content: |
  **Saint du jour** : {{ states('sensor.saint_du_jour') }}
  
  **Saint de demain** : {{ state_attr('sensor.saint_du_jour', 'saint_demain') }}
```

### Carte avec tous les saints

```yaml
type: markdown
content: |
  ### 📅 Saints du {{ state_attr('sensor.saint_du_jour', 'date') }}
  
  {% for saint in state_attr('sensor.saint_du_jour', 'tous_saints_aujourdhui') %}
  - {{ saint }}
  {% endfor %}
  
  **Total** : {{ state_attr('sensor.saint_du_jour', 'nombre_saints_aujourdhui') }} saints
```

### Automatisation - Notification matinale

```yaml
automation:
  - alias: "Saint du jour - Notification"
    trigger:
      - platform: time
        at: "08:00:00"
    action:
      - service: notify.mobile_app
        data:
          title: "☀️ Bonjour !"
          message: "Nous fêtons {{ states('sensor.saint_du_jour') }} aujourd'hui"
```

### Automatisation - Annonce vocale

```yaml
automation:
  - alias: "Annonce saint du jour"
    trigger:
      - platform: time
        at: "09:00:00"
    action:
      - service: tts.google_translate_say
        data:
          entity_id: media_player.salon
          message: "Aujourd'hui nous fêtons {{ states('sensor.saint_du_jour') }}"
```

## 🐛 Signaler un problème

Si vous rencontrez un bug ou avez une suggestion :

1. Vérifiez que vous utilisez la dernière version
2. Consultez les [issues existantes](https://github.com/WadohS/hacs-ephemeride/issues)
3. Créez une nouvelle issue avec :
   - Version de Home Assistant
   - Version de l'intégration
   - Langue configurée
   - Description détaillée du problème
   - Logs pertinents

## 🤝 Contribuer

Les contributions sont les bienvenues ! Veuillez consulter notre [Guide de contribution](CONTRIBUTING.md).

### Ajouter une nouvelle langue

Nous acceptons volontiers les traductions :

1. Créez un fichier JSON dans `custom_components/ephemeride/languages/` (ex: `nl.json`)
2. Suivez le format des fichiers existants (366 dates)
3. Ajoutez le code langue dans `SUPPORTED_LANGUAGES` (`const.py`)
4. Créez le fichier de traduction UI dans `translations/`
5. Testez et soumettez une pull request !

## 📝 Changelog

### Version 1.2.3 (2025-12-09)
- 🔧 **FIX MAJEUR** : Correction incompatibilité `__init__.py` ↔ `sensor.py`
  - `__init__.py` retournait `saint_aujourdhui`, `sensor.py` cherchait `today`
  - Support universel des formats JSON (tuple et simple)
- 🐛 **FIX CRITIQUE** : Correction "État Inconnu" sur `sensor.saint_du_jour`
- 📦 Optimisation : `__init__.py` supporte maintenant `[["Marie", "Sainte"], ...]` et `["Marie", ...]`
- 🎨 Ajout des icônes et logos officiels (icon.png, logo.png en 256/512px)

### Version 1.2.2 (2025-12-08)
- 🔧 **FIX CRITIQUE** : Correction `Invalid \escape: line 9 column 9 (char 94)`
  - Échappement correct des caractères spéciaux dans `fr.json`
- 🚀 **FIX CRITIQUE** : Correction `Detected blocking call to open()`
  - Lecture asynchrone avec `aiofiles`
  - Évite le blocage de l'event loop
- 📊 **NOUVEAUX ATTRIBUTS** :
  - `nombre_saints_aujourdhui` : Compteur de saints du jour
  - `nombre_saints_demain` : Compteur de saints de demain
- 🔥 **FIX RECORDER** : Limitation à 5 saints dans `tous_saints_aujourdhui/demain`
  - Résout `State attributes exceed maximum size of 16384 bytes`
- 📉 Optimisation `fr.json` : **13 KB** (au lieu de 27 KB)
- 🧹 Nettoyage : Suppression des doublons

### Version 1.1.1
- 🔧 Fix : Icône Material Design Icons pour compatibilité immédiate
- ✅ Icône : `mdi:calendar-star`

### Version 1.1.0
- ✨ Ajout de 5 nouvelles langues (en, de, es, it, pt)
- 🌍 Support multilingue complet (6 langues)
- 🔄 Changement de langue sans réinstallation
- 📚 Interface utilisateur traduite dans toutes les langues
- 🎨 Icône personnalisée

### Version 1.0.0
- 🎉 Version initiale
- 🇫🇷 Support du français

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- Communauté Home Assistant pour leur support
- Tous les contributeurs qui ont ajouté des traductions
- Les utilisateurs qui signalent des problèmes et suggèrent des améliorations

---

**Note** : Cette intégration utilise des données de saints et fêtes adaptées aux traditions culturelles de chaque pays/langue. Les dates et noms peuvent varier selon les calendriers liturgiques locaux.

***

[releases-shield]: https://img.shields.io/github/release/WadohS/hacs-ephemeride.svg?style=for-the-badge
[releases]: https://github.com/WadohS/hacs-ephemeride/releases
[commits-shield]: https://img.shields.io/github/commit-activity/y/WadohS/hacs-ephemeride.svg?style=for-the-badge
[commits]: https://github.com/WadohS/hacs-ephemeride/commits/main
[license-shield]: https://img.shields.io/github/license/WadohS/hacs-ephemeride.svg?style=for-the-badge
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/hacs/integration
[maintenance-shield]: https://img.shields.io/badge/maintainer-WadohS-blue.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
