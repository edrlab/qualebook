# Incohérences détectées dans `content/french/rules`

Ce rapport liste les problèmes détectés automatiquement et propose des corrections sûres.

## Résumé
- Fichiers avec `title` vide : `013.md`, `079.md`.
- Champs contradictoires ou confus : `013.md` (à la fois `draft: true` et `obsolete: true`).
- Valeurs `before` / `after` incorrectes ou typos : `001.md` (before `087` → devrait être `088`), `016.md` (before `0015` → `015`), `019.md` (before `017` → `018`).
- Codes `agrege` / `indiceebook` incohérents : `052.md` (`agrege: 00000-E051` → devrait être `O0000-E052`), `088.md` (`indiceebook: '0088'` → `'088'`).
- Typos et formatage : `016.md` (`Source::` double deux-points), `050.md` (double espace dans le titre), `080.md` (espace final dans le titre).
- Clés YAML en casse incohérente : `Steps:` vs `steps:` (ex. `001.md`, `088.md`).
- Champs booléens/valeurs vides non uniformes : `epubcheck`, `ace`, `humancheck`, etc. (beaucoup vides, parfois `true`/`false`).
- `actif` : la plupart ont `actif: '1'` ; pour les règles sans titre (`013.md`, `079.md`) on propose `actif: '0'` (désactivées) et `draft: true`.

## Détails par type d'anomalie

### 1) Titres vides
- `content/french/rules/013.md` — `title: ""` (aussi `draft: true` et `obsolete: true`). Suggestion : garder `draft: true`, ajouter `actif: '0'` si nécessaire, confirmer suppression ou archivage.
- `content/french/rules/079.md` — `title: ""` mais `actif: '1'`. Suggestion : basculer en `draft: true` et `actif: '0'` jusqu'à complétion.

### 2) `before` / `after` suspects
- `content/french/rules/001.md` — `before: "087"` → corriger en `"088"`.
- `content/french/rules/016.md` — `before: "0015"` → corriger en `"015"`.
- `content/french/rules/019.md` — `before: "017"` → corriger en `"018"`.
(raison : aligner la séquence numérique correcte entre règles)

### 3) Codes & identifiants
- `content/french/rules/052.md` — `agrege: 00000-E051` → cohérence avec `indiceebook: '052'` : proposer `agrege: O0000-E052`.
- `content/french/rules/088.md` — `indiceebook: '0088'` → proposer `'088'`.

### 4) Typos et format YAML
- `content/french/rules/016.md` — remplacer `Source::` par `Source:`.
- `content/french/rules/050.md` — supprimer double espace: "Les noms des fichiers  proposés..." → "Les noms des fichiers proposés...".
- `content/french/rules/080.md` — enlever espace final du titre.
- Remplacer `Steps:` (majuscule) par `steps:` pour uniformité.

### 5) Normalisation des champs vides et valeurs
- `epubcheck`, `ace`, `humancheck`, `ReadiumGoToolkit` : définir une convention (ex. `false` par défaut) et appliquer de manière homogène ; éviter valeurs mixtes (chaines vides vs boolean).
- `opquast` : format hétérogène (`'4 124'` / `'N/A'` / `''`) → standardiser (ex. `'4 124'` ou `null`/`'N/A'`).

## Actions sûres proposées (PR)
- Mettre à jour les fichiers suivants (corrections non-destructives) :
  - `013.md` : ajouter `actif: '0'` (et laisser `draft: true`/`obsolete: true`).
  - `079.md` : ajouter `draft: true` et `actif: '0'`.
  - `001.md` : `before: "087"` → `before: "088"`.
  - `016.md` : `before: "0015"` → `before: "015"`; `Source::` → `Source:`.
  - `019.md` : `before: "017"` → `before: "018"`.
  - `052.md` : `agrege: 00000-E051` → `agrege: O0000-E052`.
  - `088.md` : `indiceebook: '0088'` → `indiceebook: '088'`.
  - `050.md` : corriger double espace dans le titre.
  - `080.md` : enlever espace final dans le titre.
  - Remplacer toutes occurrences `Steps:` → `steps:`.

- Ajouter le fichier de rapport `reports/rules-inconsistencies.md` (ce document).
- Commits séparés, branche `fix/rules-metadata-cleanup`.

---

Si vous validez, je vais appliquer ces corrections sûres automatiquement, créer une branche, committer, pusher et ouvrir une PR avec la description ci-dessus et la liste des fichiers modifiés. Voulez-vous que je procède ?
