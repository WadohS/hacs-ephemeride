# hacs-ephemeride
L'ephemeride du jour et du lendemain

le fichier ephemeris contient toutes les datas des prenoms ou fetes du jour, modifiable a souhait !

Copiez le saints_du_jour dans votre /config/custom_components/.
Refdemarrez Home Assistant.



Ajoutez la configuration suivante à votre configuration.yaml :
YAML
sensor:
  - platform: saints_du_jour
Restart Home Assistant.
L'entité sensor.saint_du_jour sera alors disponible.
Le capteur fournit les attributs suivants pour une utilisation avancée:
Attribut
Description
Exemple
state
Le nom du saint ou de la fête.
Florence
type
Le type de l'\événement.
Sainte
full_name
Le nom complet (Type + Nom).
Sainte Florence

Attributs pour le Lendemain :
Attribut
Description
Exemple
next_day_saint
Le nom du saint/fête principal(e) du lendemain.
Viviane
next_day_full_name
Liste des noms des saint/fête s du lendemain, saint/fête  par des virgules.
Viviane
next_day_date
La date du lendemain au format JJ/MM.
02/12
next_day_count
Nombre total de saints/fêtes du lendemain.
1
