---
title: "Conditions et licence"
nav_order: 9
lang: "fr"
source: terms.md
source_hash: "7278eb6ba813"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Le contenu du jeu {#the-games-content}

Assetto Corsa Rally et ses étapes appartiennent à son développeur, Kunos Simulazioni,
et à son éditeur, 505 Games. 3DHeat AC Rally n'est ni affilié à Kunos Simulazioni ou 505 Games,
ni soutenu par eux. Assetto Corsa Rally ainsi que les noms et marques associés appartiennent à
leurs propriétaires.

Cet outil ne livre rien du jeu et ne télécharge rien : ni ressources du jeu, ni code du jeu, ni
DLL. Il lit les fichiers de la copie **que vous** avez installée, sur votre machine, en dehors du
jeu. Il ne modifie rien dans le jeu et ne parle à aucun serveur. Un parcours qu'il écrit est découpé
dans l'étape du jeu et reste sur votre machine, pour analyser vos propres tours ; merci de ne pas
le partager ni le publier.

Chaque lecteur de jeu est un petit projet à part, avec son propre fichier de licence, ses propres versions et son propre suivi des tickets : il peut être installé, mis à jour, maintenu - ou retiré à la demande d'un ayant droit - seul, sans toucher au visualiseur ni aux autres outils.

Ayants droit : ouvrez un ticket sur [github.com/Holdi601/3DHeat-Ext-ACRally/issues](https://github.com/Holdi601/3DHeat-Ext-ACRally/issues) - nous répondons rapidement et retirons tout ce qui est demandé.

Les règles de 3DHeat GameFiles s'appliquent ici sans changement
([Règles et licences](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)) :

- **Aucune clé : aucune livrée, aucune récupérée.** Aucun conteneur du jeu n'est chiffré ;
  un conteneur IoStore chiffré est refusé d'emblée.
- **Vos fichiers.** L'outil lit les fichiers du jeu installés sur votre
  machine. Il ne télécharge jamais de contenu du jeu.
- **Le résultat n'est pas destiné à être redistribué.** Gardez les `.glb` exportés, et les textures
  qu'ils contiennent, pour votre propre analyse. Ne publiez, ne partagez ni ne vendez les parcours,
  niveaux, modèles ou textures exportés. Le `.gitignore` du dépôt tient les fichiers du jeu, les
  exports et les tours hors du contrôle de version.

## Oodle est trouvé, pas fourni {#oodle-is-found-not-bundled}

Oodle (RAD Game Tools, aujourd'hui Epic) est propriétaire et n'a pas de version redistribuable.
`oo2core_*.dll` est concédée sous licence au produit qui la livre. 3DHeat GameFiles charge donc une
bibliothèque déjà présente sur la machine au lieu d'en embarquer une, et cet outil n'en embarque
aucune non plus ([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Les formats {#the-formats}

Le jeu tourne sur Unreal Engine 5. Ses conteneurs et ses paquets sont lus par les lecteurs Unreal
de 3DHeat GameFiles. Les données de propriétés compilées d'Unreal 5 ont besoin de la liste des
propriétés de chaque classe. Les listes de `unversioned.py` de GameFiles ne contiennent que des
**noms et des types**. Elles ont été déduites des en-têtes du moteur Unreal que Epic met à la disposition
de toute personne disposant d'un compte lié, puis vérifiées sur les données livrées. Aucun code source
du moteur n'est inclus ni requis. Ce que cet outil ajoute - où se trouve une étape, comment ses
composants placent leurs maillages, dans quel sens sont orientés les axes d'un tour - a été établi à
partir du jeu installé ([Export du parcours](course-assetto-corsa-rally.md)).

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)). Nécessite
3DHeat GameFiles (MIT) et numpy (BSD-3-Clause) ; les tests nécessitent pytest (MIT). Voir
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Écrit pour ce projet ; aucun code n'a été repris d'un autre projet.
