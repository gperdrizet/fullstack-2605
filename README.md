# fullstack-2605

[![Pages deployment](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml/badge.svg)](https://github.com/gperdrizet/fullstack-2605/actions/workflows/publish.yml)
[![Slack notifications](https://github.com/gperdrizet/fullstack-2605/actions/workflows/slack-pages-deployed.yml/badge.svg)](https://github.com/gperdrizet/fullstack-2605/actions/workflows/slack-pages-deployed.yml)
[![Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Fullstack Academy](https://img.shields.io/badge/Fullstack_Academy-AI%2FML_2605-CC0000?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB/ElEQVR42qVTS2tTQRg993oNlWhsmndMYpNqFLrVH+HChQtBFERcquB/EJS2lmqoGxUXoogWtWqRIlUJsSZVGkF/RjtjW/Umua8cF1NCe3OLC8/q43ucmfnOGY0kEYRuF9D1/tiH4KzrAboOd7kJp7Gkhl03sBX0w3FIknZjiXLkKGVhhHa1tq22FQgc/lilLJYphlIUsTRlvkRr/l0gCfzD1tt5ynyJq3siNG+MszVV4Wo4SpEpsPNyto9EETguSbLz/AVFpkCxL0ZzbKLX1KrcoRhMUCSybD9+opKuu0ngeSTJ9sNHFLE0RSTOVmVa8S43adcbqn7vAUU0RTGYYPvufUXieQS7XbZuT1NEk5S5IjubJzhfvlKWRymLZdq1T+qGs68oDx6i2J+gOXaT9DwqGUMhJZXnAYYBp97ArzPnwJUVcH0Dv8+eh1OtQTMM1aNpKgag0fMIXYf1bAZ/Ll8FjN3Q9obBtTUMXLkELRRC+1YFWiQCWhZgthCemsDAxQvKYNsUeDNHmStSxDNcP3Gyt8SNU6cp4lmKdJ6dpzPcuvh+GRc+qHfG0jSvXac5PkmRPECZHWbn9dwOMvqNtPiZsnSEYjBJMZSizBVpLbz/h5F8JE7zG3+WRymHD9NerO9oZS3wN7oeYOyC+/0HYNswjh/r5fzQ/vc7/wXommuoWg4yLwAAAABJRU5ErkJggg==&logoColor=white)](https://www.fullstackacademy.com/)

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
│   └── extra.css                     # custom brand colors
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

Then open <http://127.0.0.1:8000> in your browser. Changes to any file in `docs/` or `mkdocs.yml` are reflected immediately.


## Deployment

All changes to the course site should go through a pull request rather than pushing directly to `main`. The recommended workflow is:

1. Create or switch to a `dev` branch (or any feature branch):
   ```bash
   git checkout -b dev
   ```
2. Make your changes, commit, and push:
   ```bash
   git add .
   git commit -m "describe your changes"
   git push origin dev
   ```
3. Open a pull request from your branch into `main` on GitHub. Write a short description of what changed — this text is included in the Slack notification sent to students.
4. Merge the pull request.

Merging into `main` triggers two automated workflows in sequence:

- **Publish to GitHub Pages** (`.github/workflows/publish.yml`): runs `mkdocs gh-deploy --force`, which builds the site and pushes it to the `gh-pages` branch.
- **pages-build-deployment** (managed by GitHub Pages): picks up the new `gh-pages` content and deploys it to the live CDN. This step typically takes 5–6 minutes.

Once both workflows complete successfully, a Slack notification is sent to the course channel (see below).


## Slack notifications

When a pull request is merged to `main` and the GitHub Pages deployment succeeds, the workflow at `.github/workflows/slack-pages-deployed.yml` posts a message to the course Slack channel. The message includes the PR description, so students know what was updated.

The workflow posts via a **Slack Workflow Builder webhook** — no bot or admin approval required, since Workflow Builder is available to all workspace members.

### Setup

1. In Slack, open **Tools → Workflow Builder** and create a new workflow with a **Webhook** trigger.
2. Define three text input variables: `author`, `details`, and `site_url`.
3. Add a **Send a message** step to post to your channel using those variables.
4. Publish the workflow and copy the webhook URL (it starts with `https://hooks.slack.com/workflows/...`).
5. Add the URL as a repository secret:
   - Go to the repository on GitHub → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
   - Name: `SLACK_WEBHOOK_URL`
   - Value: paste the webhook URL.

The notification is skipped automatically if the deployment fails or if the push to `main` was not from a merged pull request (e.g. a direct push).


