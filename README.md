# fullstack-2605

[![Publish to GitHub Pages](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml/badge.svg)](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml)

Materials for Fullstack Academy AI/ML cohort 2605.

Course site: <https://gperdrizet.github.io/fullstack-2605>

## Site overview

The course site is built with [MkDocs](https://www.mkdocs.org/) using the [Material theme](https://squidfunk.github.io/mkdocs-material/). Source pages live in `docs/` and are configured in `mkdocs.yml`. The site deploys automatically to GitHub Pages via GitHub Actions on every push to `main`.

```
docs/
├── index.md                          # homepage: notebook table
├── assets/
│   └── logo.png                      # Fullstack Academy logo
├── stylesheets/
│   └── extra.css                     # custom brand colours
└── resources/
    ├── documentation-links.md
    ├── linux-commands.md
    ├── notebook-shortcuts.md
    ├── dev-tools-install-guide.md
    └── dev-container-guide.md
```

## Local development

Install dependencies:

```bash
pip install mkdocs-material
```

Serve the site locally with live reload:

```bash
mkdocs serve
```

Then open <http://127.0.0.1:8000> in your browser. Changes to any file in `docs/` or `mkdocs.yml` are reflected immediately.

## Deployment

Pushing to `main` triggers the workflow at `.github/workflows/publish.yml`, which runs `mkdocs gh-deploy --force` to build and push the site to the `gh-pages` branch. GitHub Pages serves the site from that branch.
