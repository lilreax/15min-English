# 15 min d'anglais — mise en ligne

Ce dossier contient une petite web app : de vrais articles d'actualité en anglais
(mis à jour automatiquement chaque semaine) + des leçons de grammaire, avec suivi
de série de jours. Une fois en ligne, tu l'ajoutes à ton écran d'accueil comme
une vraie appli, sans jamais repasser par Claude.

## Étape 1 — Créer un compte GitHub (gratuit)
Va sur https://github.com/join si tu n'as pas encore de compte.

## Étape 2 — Créer une clé API gratuite pour les news
1. Va sur https://newsapi.org/register
2. Inscris-toi (gratuit, pas de carte bancaire) et récupère ta clé API (une suite
   de lettres/chiffres) sur ton tableau de bord.

## Étape 3 — Créer le dépôt (repository)
1. Sur GitHub, clique sur **New repository**.
2. Nomme-le par exemple `15min-english`.
3. Coche **Public**, ne coche rien d'autre, clique **Create repository**.
4. Sur la page du dépôt, clique **Add file → Upload files**, et glisse-dépose
   TOUS les fichiers de ce dossier (en gardant la structure : le dossier
   `.github/workflows/` et `data/` doivent rester des sous-dossiers).
5. Clique **Commit changes**.

## Étape 4 — Ajouter ta clé API en secret
1. Dans le dépôt : **Settings → Secrets and variables → Actions**.
2. Clique **New repository secret**.
3. Nom : `NEWS_API_KEY`
4. Valeur : colle ta clé de l'étape 2.
5. Clique **Add secret**.

## Étape 5 — Lancer la première récupération d'articles
1. Va dans l'onglet **Actions** du dépôt.
2. Clique sur le workflow **Update weekly news**.
3. Clique **Run workflow → Run workflow** (bouton vert).
4. Attends ~30 secondes, rafraîchis : un fichier `data/articles.json` doit
   apparaître avec de vrais articles dedans.
   → Ensuite, ce workflow se relance **automatiquement chaque lundi à 6h UTC**,
   sans que tu aies besoin de faire quoi que ce soit.

## Étape 6 — Activer GitHub Pages (l'hébergement gratuit)
1. **Settings → Pages**.
2. Sous "Build and deployment", choisis **Deploy from a branch**.
3. Branche : `main`, dossier : `/ (root)`. Clique **Save**.
4. Attends 1-2 minutes. Ton URL apparaît en haut de la page, du style :
   `https://TON-PSEUDO.github.io/15min-english/`

## Étape 7 — L'installer sur ton téléphone
1. Ouvre cette URL dans le navigateur de ton téléphone (Safari sur iPhone,
   Chrome sur Android).
2. Menu du navigateur → **Ajouter à l'écran d'accueil**.
3. Une icône apparaît sur ton téléphone, comme une vraie appli — tu l'ouvres
   directement, sans passer par Claude ni par un navigateur visible.

## Pour aller plus loin
- Tu peux changer la catégorie d'actu en modifiant la liste `CATEGORIES` dans
  `fetch_news.py` (options possibles : general, business, entertainment,
  health, science, sports, technology).
- Les leçons de grammaire changent automatiquement chaque semaine (6 leçons
  qui tournent) — tu peux en ajouter d'autres dans le tableau `GRAMMAR` de
  `index.html`.
- Le plan gratuit de NewsAPI limite à 100 requêtes/jour — largement suffisant
  puisque le workflow ne tourne qu'une fois par semaine.
