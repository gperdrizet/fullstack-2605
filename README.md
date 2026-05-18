# fullstack-2605

[![Publish to GitHub Pages](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml/badge.svg)](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml)

Materials for Fullstack Academy AI/ML cohort 2605.

Course site: <https://gperdrizet.github.io/fullstack-2605>

## Site overview

The course site is built with [MkDocs](https://www.mkdocs.org/) using the [Material theme](https://squidfunk.github.io/mkdocs-material/). Source pages live in `docs/` and are configured in `mkdocs.yml`. The site deploys automatically to GitHub Pages via GitHub Actions on every push to `main`.

```
docs/
├── index.md                          # homepage
├── notebooks.md                      # notebook table
├── datasets.md                       # dataset table
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

## Datasets and Git LFS

Dataset files in `data/` are stored with [Git LFS](https://git-lfs.com/). Install Git LFS before cloning so the files are downloaded correctly:

```bash
# Install (Ubuntu/Debian)
sudo apt install git-lfs

# Install (macOS)
brew install git-lfs

# Enable in your Git install (once per machine)
git lfs install
```

If you already cloned the repo without Git LFS, run `git lfs pull` to fetch the data files.

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
