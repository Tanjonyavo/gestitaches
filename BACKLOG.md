# Backlog de GestiTâches

Les critères suivent le format « Étant donné / Quand / Alors » du Cours01 (p. 44–45). Les dates sont des échéances de planification du TD.

| Jalon | Échéance | Objectif |
| --- | --- | --- |
| Sprint 1 | 18 novembre 2026 | Créer, consulter, terminer et supprimer les tâches. |
| Sprint 2 | 2 décembre 2026 | Modifier et organiser les tâches pour repérer les échéances importantes. |

| Label | Couleur | Usage |
| --- | --- | --- |
| `bug` | `#D73A4A` | Comportement à corriger |
| `enhancement` | `#A2EEEF` | Fonctionnalité utilisateur |
| `documentation` | `#0075CA` | Mise à jour d’un document |
| `priorite-haute` | `#D93F0B` | Travail à traiter en priorité |
| `bloque` | `#6F42C1` | Travail en attente d’un prérequis |

## Ordre de réalisation

1. [US01 — Créer une tâche](https://github.com/Tanjonyavo/gestitaches/issues/1) · priorité haute.
2. [US02 — Consulter mes tâches](https://github.com/Tanjonyavo/gestitaches/issues/2) · priorité haute.
3. [US03 — Marquer une tâche comme terminée](https://github.com/Tanjonyavo/gestitaches/issues/3) · priorité haute.
4. [US04 — Supprimer une tâche](https://github.com/Tanjonyavo/gestitaches/issues/4).
5. [US05 — Modifier une tâche](https://github.com/Tanjonyavo/gestitaches/issues/5).
6. [US06 — Trier par échéance](https://github.com/Tanjonyavo/gestitaches/issues/6).
7. [US07 — Filtrer par statut](https://github.com/Tanjonyavo/gestitaches/issues/7).
8. [US08 — Repérer les tâches en retard](https://github.com/Tanjonyavo/gestitaches/issues/8).

Les trois premières stories couvrent le parcours principal : ajouter une tâche, la retrouver et suivre son achèvement. US04 complète la première version. Les stories du Sprint 2 enrichissent ce parcours. La revue a conservé les huit stories, chacune portant sur une action ou un besoin vérifiable.

## Sprint 1

### US01 — Créer une tâche

En tant qu’utilisateur, je veux créer une tâche avec un titre et, au choix, une description et une échéance, afin de me rappeler ce que je dois faire.

- [ ] Étant donné le formulaire, quand j’envoie « Préparer le TD », « Relire le cours » et « 2026-11-18 », alors la tâche est enregistrée avec ces valeurs et le statut à faire.
- [ ] Étant donné un titre vide ou composé d’espaces, quand j’envoie le formulaire, alors un message indique que le titre est obligatoire et aucune tâche n’est ajoutée.
- [ ] Étant donné une date impossible telle que le 30 février, quand je l’envoie à l’API, alors la demande est refusée et aucune tâche n’est ajoutée.
- [ ] Étant donné un titre valide, quand j’ajoute la tâche sans description ni échéance, alors elle est enregistrée avec le statut « À faire ».

### US02 — Consulter mes tâches

En tant qu’utilisateur, je veux consulter la liste de mes tâches, afin de connaître mon travail à faire.

- [ ] Étant donné une tâche enregistrée, quand j’ouvre la liste, alors son titre, sa description, son échéance et son statut sont affichés.
- [ ] Étant donné qu’aucune tâche n’est enregistrée, quand j’ouvre la liste, alors le message « Aucune tâche pour le moment. » apparaît.
- [ ] Étant donné une tâche sans échéance, quand j’ouvre la liste, alors sa ligne affiche « Sans échéance ».

### US03 — Marquer une tâche comme terminée

En tant qu’utilisateur, je veux marquer une tâche comme terminée, afin de suivre mon avancement.

- [ ] Étant donné deux tâches à faire, quand je termine la première, alors seule la première passe au statut « Terminée ».
- [ ] Étant donné une tâche terminée, quand je recharge la page, alors son statut reste « Terminée ».

### US04 — Supprimer une tâche

En tant qu’utilisateur, je veux supprimer une tâche devenue inutile, afin de garder une liste pertinente.

- [ ] Étant donné deux tâches, quand je confirme la suppression de l’une, alors seule la tâche choisie disparaît et reste absente après rechargement.
- [ ] Étant donné que la confirmation de suppression est affichée, quand je l’annule, alors la tâche et ses données restent dans la liste.

## Sprint 2

### US05 — Modifier une tâche

En tant qu’utilisateur, je veux modifier les détails d’une tâche, afin de refléter un changement de plan.

- [ ] Étant donné une tâche enregistrée, quand je change son titre, sa description et son échéance, alors ces valeurs sont visibles après rechargement et le statut est conservé.
- [ ] Étant donné le formulaire d’édition, quand j’efface le titre et que j’enregistre, alors un message apparaît et les valeurs enregistrées restent les mêmes.
- [ ] Étant donné une tâche avec une description et une échéance, quand je vide ces deux champs et que j’enregistre, alors la tâche est conservée sans description ni échéance.

### US06 — Trier par échéance

En tant qu’utilisateur, je veux trier mes tâches par échéance, afin de voir d’abord celles à rendre bientôt.

- [ ] Étant donné des tâches prévues le 18 et le 10 novembre, quand je choisis « Échéance croissante », alors la tâche du 10 apparaît en premier.
- [ ] Étant donné une tâche sans échéance et deux autres qui ont la même date, quand je trie, alors les tâches datées précèdent celle sans échéance et les deux ex æquo apparaissent de la plus ancienne création à la plus récente.

### US07 — Filtrer par statut

En tant qu’utilisateur, je veux filtrer la liste par statut, afin de me concentrer sur les tâches à faire.

- [ ] Étant donné une tâche à faire et une terminée, quand je sélectionne « À faire », alors seule la première est affichée.
- [ ] Étant donné les mêmes tâches, quand je sélectionne « Terminées », alors seule la deuxième est affichée.
- [ ] Étant donné un filtre actif, quand je sélectionne « Toutes », alors les deux tâches sont de nouveau affichées.

### US08 — Repérer les tâches en retard

En tant qu’utilisateur, je veux voir quelles tâches sont en retard, afin de les traiter en priorité.

- [ ] Étant donné une tâche à faire dont l’échéance précède la date locale du jour, quand j’ouvre la liste, alors l’indication « En retard » est affichée sur cette tâche.
- [ ] Étant donné une tâche terminée dont l’échéance était hier et une tâche à faire dont l’échéance est aujourd’hui, quand j’ouvre la liste, alors aucune des deux ne porte l’indication « En retard ».
- [ ] Étant donné une tâche à faire sans date d’échéance, quand j’ouvre la liste, alors elle ne porte pas l’indication « En retard ».
