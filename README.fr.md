# Éphéméride - Intégration Home Assistant

Français | [English](README.md)

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![Community Forum][forum-shield]][forum]

_Intégration Home Assistant qui expose les commémorations visibles du jour avec des capteurs dédiés pour les saints, saintes, fêtes, dates religieuses, prénoms et autres événements._

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

![Icône Éphéméride](https://raw.githubusercontent.com/WadohS/hacs-ephemeride/main/custom_components/ephemeride/icon.png)

## Fonctionnalités

Cette intégration crée la plateforme suivante :

Plateforme | Description
-- | --
`sensor` | Capteurs exposant les commémorations du jour et des capteurs dédiés par catégorie

### `sensor.saints_du_jour`

- État : liste des commémorations du jour, limitée à 5 entrées
- Attributs :
  - `saint_demain` : saint principal du lendemain
  - `commemoration_principale_aujourdhui` : premier élément du jour
  - `commemoration_principale_demain` : premier élément du lendemain
  - `langue` : langue configurée
  - `date` : date locale courante selon le fuseau Home Assistant
  - `tous_saints_aujourdhui` : liste complète du jour, limitée à 5 entrées
  - `tous_saints_demain` : liste complète du lendemain, limitée à 5 entrées
  - `nombre_saints_aujourdhui` : nombre total d'entrées aujourd'hui
  - `nombre_saints_demain` : nombre total d'entrées demain

### Capteurs supplémentaires

- `sensor.saint_du_jour`
- `sensor.sainte_du_jour`
- `sensor.fete_du_jour`
- `sensor.date_religieuse_du_jour`
- `sensor.prenom_du_jour`
- `sensor.autre_du_jour`

Chaque capteur de catégorie affiche la liste filtrée du jour, limitée à 5 entrées, et expose aussi l'élément principal du jour et du lendemain dans ses attributs. Les entrées non typées restent dans `sensor.autre_du_jour` tant que le fichier de langue n'apporte pas de métadonnées explicites. Les prénoms du jour peuvent maintenant être isolés dans `sensor.prenom_du_jour` sans les mélanger aux saints.

## Langues supportées

- Français (`fr`)
- Anglais (`en`)
- Allemand (`de`)
- Espagnol (`es`)
- Italien (`it`)
- Portugais (`pt`)

## Installation

### HACS

1. Ouvrez HACS dans Home Assistant
2. Allez dans `Intégrations`
3. Ouvrez le menu en haut à droite puis `Dépôts personnalisés`
4. Ajoutez `https://github.com/WadohS/hacs-ephemeride`
5. Sélectionnez la catégorie `Integration`
6. Recherchez `Ephemeride` puis installez l'intégration
7. Redémarrez Home Assistant

### Installation manuelle

1. Copiez `custom_components/ephemeride` dans le dossier `custom_components/` de Home Assistant
2. Redémarrez Home Assistant

## Configuration

La configuration se fait entièrement via l'interface :

1. Ouvrez `Paramètres` -> `Appareils et services`
2. Cliquez sur `Ajouter une intégration`
3. Recherchez `Ephemeride`
4. Sélectionnez la langue souhaitée
5. Validez

Pour changer la langue plus tard :

1. Ouvrez la carte d'intégration `Ephemeride`
2. Cliquez sur `Configurer`
3. Sélectionnez la nouvelle langue
4. Validez

L'intégration se recharge automatiquement après changement de langue.

## Exemple Lovelace

```yaml
type: entity
entity: sensor.saints_du_jour
name: Saints du jour
icon: mdi:calendar-star
```

## Exemple d'automatisation

```yaml
automation:
  - alias: "Notification saint du jour"
    trigger:
      - platform: time
        at: "08:00:00"
    action:
      - service: notify.mobile_app
        data:
          title: "Saints du jour"
          message: "Nous fêtons {{ states('sensor.saints_du_jour') }} aujourd'hui"
```

## Notes de développement

- Les données calendaires sont dans `custom_components/ephemeride/languages/`
- Les traductions UI sont dans `custom_components/ephemeride/translations/`
- Le branding local est fourni dans `custom_components/ephemeride/brand/`
- L'intégration supporte les listes simples, les anciens formats type tuple et les objets dans les fichiers de langue
- Les calendriers propres à chaque pays sont conservés et classés à l'exécution

### Migration progressive des langues

- Audit de couverture : `python3 scripts/report_language_typing.py`
- Conversion d'un fichier en objets explicites : `python3 scripts/migrate_language_file.py fr`
- Écriture réelle du fichier converti : `python3 scripts/migrate_language_file.py fr --write`
- Les entrées converties utilisent `name` et `type`, avec `source_type` conservé si le fichier d'origine portait déjà une information métier
- Tous les fichiers de langue fournis sont maintenant stockés comme objets typés explicites

## Changelog

### Version 1.4.4
- Evite de relancer une migration d'historique du recorder lorsqu'une ancienne entite saint renommee manuellement pointe encore vers l'ancien unique_id historique du capteur general alors que le capteur pluriel moderne existe deja

### Version 1.4.3
- Evite de retraiter l'ancien unique_id du capteur general lorsque les capteurs moderne singulier et pluriel coexistent deja, ce qui reduit les warnings repetes de migration d'historique du recorder

### Version 1.4.2
- Stabilise la migration des entites Ephemeride afin que les capteurs saints au singulier et au pluriel conservent les bons entity_id apres rechargement ou redemarrage

### Version 1.4.1
- Restaure le dernier etat connu des capteurs et leurs attributs apres un redemarrage de Home Assistant jusqu'au rechargement des nouvelles donnees

### Version 1.4.0
- Ajout d'une categorie de capteur `prenom` et enrichissement des jeux de donnees de prenoms du jour dans toutes les langues supportees
- Renommage des entites saints pour coller a leur role reel avec migration automatique des anciens `entity_id` Home Assistant au rechargement
- Affichage de toutes les commemorations visibles du jour dans l'etat des capteurs au lieu de n'exposer que le premier element

### Version 1.3.3
- Conversion complete de tous les fichiers de langue fournis vers des objets typés explicites
- Amelioration des heuristiques automatiques pour mieux remplir saints, saintes et fetes dans toutes les langues supportees

### Version 1.3.2
- Ajout d'outils de migration progressive pour auditer et typer les fichiers de langue sans perdre les spécificités pays

### Version 1.3.1
- Ajout du calcul annuel des dates liturgiques mobiles avec fusion au runtime avec les calendriers par pays
- Amelioration de la detection des categories pour mieux alimenter les capteurs de fetes et de dates religieuses

### Version 1.3.0
- Ajout de capteurs dédiés pour saint masculin, sainte, fête, date religieuse et autre commémoration
- Ajout du branding local de l'intégration pour les versions récentes de Home Assistant
- Ajout d'un script de validation des fichiers de langue

### Version 1.2.5
- Correction du changement de langue via les options avec rechargement correct de l'intégration
- Correction de la gestion de date pour utiliser le fuseau horaire Home Assistant
- Mise à jour de la documentation en français et en anglais

### Version 1.2.4
- Ajout des icônes et logos officiels
- Amélioration de la compatibilité entre les données du coordinator et l'état du capteur

### Version 1.2.3
- Correction de compatibilité JSON entre plusieurs formats de fichiers de langue
- Correction de l'état inconnu sur `sensor.saint_du_jour`
- Limitation des attributs volumineux pour éviter les erreurs Recorder

## Support

Si tu rencontres un bug, ouvre une issue avec :

- version de Home Assistant
- version de l'intégration
- langue sélectionnée
- description détaillée
- logs utiles

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
