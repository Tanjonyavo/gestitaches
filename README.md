# GestiTâches

GestiTâches est une application web de gestion de tâches personnelles. Elle aide à suivre les tâches à faire et leurs dates d’échéance. Le projet vise la création, la consultation, l’achèvement et la suppression des tâches.

## Équipe

TD réalisé en solo par [Tanjonyavo](https://github.com/Tanjonyavo), responsable du frontend, du backend et de la configuration du dépôt.

## Stratégie de branchement

**GitHub Flow.** Une seule branche principale suffit pour ce projet court. Chaque modification part de `main`, reste sur une branche courte et revient par une pull request. La règle prévue sur `main` exige une approbation avant fusion.

- `feature/NN-nom-court` pour une fonctionnalité, par exemple `feature/01-creer-tache`.
- `fix/NN-nom-court` pour une correction et `docs/nom-court` pour la documentation.
- `test/prenom` pour vérifier temporairement son accès en écriture.
- Utiliser le numéro réel de l’issue dans `Closes #N` et sélectionner `main` comme branche de base. Après fusion, supprimer la branche de travail.

## Organisation

- [Backlog et critères d’acceptation](BACKLOG.md)
- [Frontend](frontend/) en HTML et JavaScript
- [Backend](backend/) en Python 3.10+ avec stockage SQLite

Depuis la racine, lancer `python backend/server.py`, puis ouvrir `http://127.0.0.1:8000`. Le serveur écoute seulement sur la machine locale. Le fichier de données `backend/tasks.sqlite3` est ignoré par Git.
