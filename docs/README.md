# Mapping Forward — Site Statique

Générateur de site statique pour la veille cartographique **Mapping Forward**.

## Principe

- **100% Python stdlib** — aucun package à installer, pas de Node.js
- Lit les articles markdown depuis `../src/` (le repo Mapping-Forward)
- Génère un site HTML/CSS statique dans `dist/`
- Hébergeable sur n'importe quel serveur web (nginx, Apache, Caddy, Python http.server)

## Structure générée

```
dist/
├── index.html          # Accueil: synthèses quotidiennes (7 derniers jours)
├── archives.html       # Toutes les archives par année/mois
├── feed.xml            # Flux RSS (50 derniers articles)
├── style.css           # Thème dark/light, responsive
├── manifest.json       # Manifest JSON de tous les articles
└── articles/
    ├── 2025-12/        # Pages par mois
    │   └── *.html      # Une page par article (fiche de récap)
    ├── 2026-01/
    ├── 2026-02/
    └── ...
```

## Utilisation

### Générer le site

```bash
cd docs/
python3 build_site.py
```

### Prévisualiser localement

```bash
python3 -m http.server -d dist/ 8000
# Ouvrir http://localhost:8000
```

### Déployer sur un serveur

```bash
# Option 1: rsync vers serveur
rsync -avz --delete dist/ user@serveur:/var/www/mappingforward/

# Option 2: scp simple
scp -r dist/* user@serveur:/var/www/mappingforward/
```

### Déploiement automatique (GitHub Actions + Pages)

Le workflow `.github/workflows/build-site.yml` régénère le site chaque jour à 09:00
heure de Paris (et à chaque push sur `src/` ou `build_site.py`), commite `dist/` dans
le repo, puis déploie le contenu sur GitHub Pages :
**https://blamouche.github.io/Mapping-Forward/**

Le déploiement vers mappingforward.fr reste manuel (rsync/scp ci-dessus).

### Config nginx (exemple)

```nginx
server {
    listen 80;
    server_name mappingforward.fr;
    root /var/www/mappingforward;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # RSS feed avec bon content-type
    location /feed.xml {
        default_type application/rss+xml;
    }
}
```

### Config Apache (.htaccess)

```apache
DirectoryIndex index.html
AddType application/rss+xml .xml
```

## Pages générées

### Page d'accueil (`index.html`)
- En-tête avec stats (nombre d'articles, jours de veille)
- 7 derniers jours de veille avec articles
- Chaque article: titre, résumé express, points clés (dépliables), lien source

### Page article (`articles/YYYY-MM/slug.html`)
- Titre, date, auteur, mots-clés
- Lien vers l'article source
- Résumé express
- Points clés
- Synthèse complète (rendu markdown minimal)

### Archives (`archives.html`)
- Tous les articles groupés par année et mois
- Nombre d'articles par mois

### Flux RSS (`feed.xml`)
- 50 derniers articles
- Description = résumé express + points clés

## Intégration avec la veille

Le site peut être régénéré automatiquement après chaque passage de la veille mapping.

### Option A: Appel manuel depuis le cron job

Ajouter à la fin du script de veille mapping:
```bash
cd ~/github/Mapping-Forward/docs && python3 build_site.py
```

### Option B: Cron job dédié

```cron
# Régénérer le site chaque jour à 9h
0 9 * * * cd ~/github/Mapping-Forward/docs && python3 build_site.py
```

### Option C: Git hook post-commit

```bash
# .git/hooks/post-commit
#!/bin/bash
cd docs/ && python3 build_site.py
```

## Configuration

Éditer les variables en haut de `build_site.py`:
- `SITE_URL` — URL du site (utilisé dans les liens RSS)
- `SITE_TITLE` — Titre du site
- `SITE_SUBTITLE` — Sous-titre
- `ARTICLES_PER_PAGE` — Nombre d'articles par page (futur: pagination)

## Performance

- 783 articles générés en ~1 seconde
- Taille totale: ~7 MB
- Aucune dépendance runtime
- JavaScript minimal (recherche dans le header uniquement, vanilla ~1 Ko, sans dépendance)