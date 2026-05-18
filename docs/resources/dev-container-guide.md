# Dev container setup guide

Use the course template repository below. It contains a dev container configuration for the course environment.

Template repository:

```text
https://github.com/gperdrizet/datascience-devcontainer
```

## 1. Fork the template repository

1. Open https://github.com/gperdrizet/datascience-devcontainer in your browser.
2. Click **Fork** (top right).
3. Accept the default fork name and settings.
4. Click **Create fork**.

## 2. Mark your fork as a template

1. In your forked repository, click **Settings**.
2. Scroll down to **Template repository**.
3. Check the box: **Template repository**.
4. Click **Save**.

## 3. Create a new repository from your template fork

1. Go back to your forked repository.
2. Click **Use this template**.
3. Choose **Create a new repository**.
4. Set your repository name.
5. Set visibility (Public or Private) based on class instructions.
6. Click **Create repository**.

## 4. Clone the new repository locally

1. In your new GitHub repository, click **Code** and copy the HTTPS URL.
2. Open Terminal (macOS) or PowerShell (Windows).
3. Move to your preferred parent folder.
4. Run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_NEW_REPO.git
cd YOUR_NEW_REPO
```

## 5. Open the repository in VS Code

From the cloned repository folder, run:

```bash
code .
```

## 6. Reopen the project in a dev container

1. In VS Code, wait for the folder to load.
2. If prompted, click **Reopen in Container**.
3. If not prompted, open Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on macOS).
4. Run: **Dev Containers: Reopen in Container**.
5. Wait for the container build/start process to finish.

## 7. Verify you are inside the dev container

1. Open a new terminal in VS Code.
2. Run:

```bash
pwd
git status
python --version
```

You should see your repository path and working toolchain available inside the container.
