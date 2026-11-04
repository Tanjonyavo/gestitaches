# GestiTâches

GestiTâches est une application web de gestion de tâches personnelles. Elle aide à suivre les tâches à faire et leurs dates d’échéance. Le projet vise la création, la consultation, l’achèvement et la suppression des tâches.

## Rôles de l’équipe

Travail individuel. Le compte [Tanjonyavo](https://github.com/Tanjonyavo) porte le cadrage et la priorisation du backlog, le frontend, le backend, le build et les vérifications locales. Les modifications sont proposées en pull request pour approbation avant fusion.

## Stratégie de branchement

**GitHub Flow.** Une seule branche principale suffit pour ce projet court. Chaque modification part de `main`, reste sur une branche courte et revient par une pull request. La règle de `main` exige une approbation avant fusion.

- `feature/NN-nom-court` pour une fonctionnalité, par exemple `feature/01-creer-tache`.
- `fix/NN-nom-court` pour une correction, `docs/nom-court` pour la documentation et `chore/nom-court` pour l’outillage.
- `test/prenom` pour vérifier temporairement son accès en écriture.
- Utiliser le numéro réel de l’issue dans `Closes #N` et sélectionner `main` comme branche de base. Après fusion, supprimer la branche de travail.

## Portée du projet

### Inclus dans cette version

- Créer une tâche avec un titre obligatoire et, au choix, une description et une date d’échéance.
- Consulter la liste avec les détails et l’état de chaque tâche.
- Marquer une tâche comme terminée ou la supprimer après confirmation.
- Conserver les tâches dans une base SQLite locale.

### Hors de la portée actuelle

- Modifier les détails, trier les échéances, filtrer par état et signaler les retards. Ces évolutions sont prévues au Sprint 2.
- Gérer des comptes utilisateurs, partager des listes et envoyer des notifications.
- Déployer le service sur Internet.

## Build

Depuis la racine du dépôt, avec GNU Make et Python 3.10 ou plus récent sur le PATH :

```sh
make build
make test
```

Le build produit `dist/gestitaches.zip`. Le projet utilise uniquement la bibliothèque standard de Python, dont le module `sqlite3`. Le build fixe l’ordre, les métadonnées et les fins de ligne du contenu de l’archive. `dist/` est ignoré par Git.

Pour lancer l’artefact, extraire l’archive et exécuter `python backend/server.py` depuis le dossier extrait, puis ouvrir `http://127.0.0.1:8000`.

Sous Windows, si l’exécutable GNU Make s’appelle `mingw32-make`, utiliser ce nom dans les commandes.

## Qualité du code

`.editorconfig` fixe UTF-8, LF et les règles d’indentation. Flake8 vérifie les fichiers Python avec une limite de 88 caractères par ligne. Dans un environnement virtuel Python activé à la racine du dépôt :

```sh
make setup
make lint
```

`make setup` installe les versions fixées dans `requirements-dev.txt`.

## Organisation

- [Backlog et critères d’acceptation](BACKLOG.md)
- [Frontend](frontend/) en HTML et JavaScript
- [Backend](backend/) en Python 3.10+ avec stockage SQLite

Depuis la racine, lancer `python backend/server.py`, puis ouvrir `http://127.0.0.1:8000`. Le serveur écoute seulement sur la machine locale. Le fichier de données `backend/tasks.sqlite3` est ignoré par Git.
