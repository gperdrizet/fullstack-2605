# Development tools installation guide

## 1. Windows

### 1.0. Open PowerShell

Use any one of these methods:

1. Press `Win`, type `PowerShell`, then press `Enter`.
2. Right-click Start and choose Windows PowerShell or Terminal.
3. Press `Win+R`, type `powershell`, then press `Enter`.

You can run all verification commands in this window.

### 1.1. Install Git

1. Go to https://git-scm.com/download/win.
2. Download and run the installer.
3. Keep the default options unless your organization requires specific settings.
4. Open PowerShell and run:

Official references:
- Download page: https://git-scm.com/download/win
- Official book (installation): https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

```bash
git --version
```

You should see a version number.

### 1.2. Install Docker

1. Go to https://www.docker.com/products/docker-desktop.
2. Download Docker Desktop for Windows.
3. Run the installer and complete setup.
4. Restart your machine if prompted.
5. Open Docker Desktop and wait for it to finish starting.
6. In PowerShell, run:

**Official references**:
- Docker Desktop download: https://www.docker.com/products/docker-desktop
- Install Docker Desktop on Windows: https://docs.docker.com/desktop/setup/install/windows-install
- Docker getting started: https://docs.docker.com/get-started

```bash
docker --version
docker run hello-world
```

If successful, Docker prints a welcome message.

### 1.3. Install VS Code

1. Go to https://code.visualstudio.com/.
2. Download VS Code for Windows and run the installer.
3. During install, enable options for:
- Add to PATH
- Open with Code actions (optional but useful)
4. Open PowerShell and run:

```bash
code --version
```

If `code` is not recognized, reopen PowerShell and try again.

**Official references**:
- VS Code download: https://code.visualstudio.com/Download
- Windows setup guide: https://code.visualstudio.com/docs/setup/windows
- Command line usage: https://code.visualstudio.com/docs/editor/command-line

### 1.4. Install the Dev Containers extension

1. Open VS Code.
2. Open the Extensions view with `Ctrl+Shift+X`.
3. Search for "Dev Containers".
4. Install the extension published by Microsoft (id: `ms-vscode-remote.remote-containers`).

**Official references**:
- Dev Containers documentation: https://code.visualstudio.com/docs/devcontainers/containers

## 2. macOS

### 2.1. Install Git

Git is often preinstalled on macOS.

1. Open Terminal.
2. Run:

```bash
git --version
```

3. If prompted, install Xcode Command Line Tools and wait for completion.
4. Run `git --version` again to verify.

Official references:
- Official book (installation): https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- macOS tools (`xcode-select`): https://developer.apple.com/library/archive/technotes/tn2339/_index.html

### 2.2. Install Docker

1. Go to https://www.docker.com/products/docker-desktop/.
2. Download Docker Desktop for Mac (choose Apple Silicon or Intel correctly).
3. Open the downloaded file and drag Docker to Applications.
4. Start Docker Desktop from Applications.
5. Complete any permission prompts.
6. In Terminal, run:

Official references:
- Docker Desktop download: https://www.docker.com/products/docker-desktop/
- Install Docker Desktop on Mac: https://docs.docker.com/desktop/setup/install/mac-install/
- Docker getting started: https://docs.docker.com/get-started/

```bash
docker --version
docker run hello-world
```

If successful, Docker prints a welcome message.

### 2.3. Install VS Code

1. Go to https://code.visualstudio.com/.
2. Download VS Code for macOS.
3. Move VS Code to Applications.
4. Open VS Code.
5. Open Command Palette with `Cmd+Shift+P`.
6. Run command: Shell Command: Install 'code' command in PATH.
7. In Terminal, run:

Official references:
- VS Code download: https://code.visualstudio.com/
- macOS setup guide: https://code.visualstudio.com/docs/setup/mac
- Command line usage: https://code.visualstudio.com/docs/editor/command-line

```bash
code --version
```

You should see a version number.

### 2.4. Install the Dev Containers extension

1. Open VS Code.
2. Open the Extensions view with `Cmd+Shift+X`.
3. Search for "Dev Containers".
4. Install the extension published by Microsoft (id: `ms-vscode-remote.remote-containers`).

**Official references**:
- Dev Containers documentation: https://code.visualstudio.com/docs/devcontainers/containers

## 3. Quick checks before class

Run these in Terminal (macOS) or PowerShell (Windows):

```bash
git --version
docker --version
code --version
```

All three should return version numbers.

## 4. Create your repo from template, clone, and open in dev container

Use the course template repository URL below. This contains a dev container configuration for the course environment.

Template repository:

```text
https://github.com/gperdrizet/datascience-devcontainer
```

### 4.1. Fork the template repository

1. Open https://github.com/gperdrizet/datascience-devcontainer in your browser.
2. Click **Fork** (top right).
3. Accept the default fork name and settings.
4. Click **Create fork**.

### 4.2. Mark your fork as a template

1. In your forked repository, click **Settings**.
2. Scroll down to **Template repository**.
3. Check the box: **Template repository**.
4. Click **Save**.

### 4.3. Create a new repository from your template fork

1. Go back to your forked repository.
2. Click **Use this template**.
3. Choose **Create a new repository**.
4. Set your repository name.
5. Set visibility (Public or Private) based on class instructions.
6. Click **Create repository**.

### 4.4. Clone the new repository locally

1. In your new GitHub repository, click **Code** and copy the HTTPS URL.
2. Open Terminal (macOS) or PowerShell (Windows).
3. Move to your preferred parent folder.
4. Run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_NEW_REPO.git
cd YOUR_NEW_REPO
```

### 4.5. Open the repository in VS Code

From the cloned repository folder, run:

```bash
code .
```

### 4.6. Reopen the project in a dev container

1. In VS Code, wait for the folder to load.
2. If prompted, click **Reopen in Container**.
3. If not prompted, open Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on macOS).
4. Run: **Dev Containers: Reopen in Container**.
5. Wait for the container build/start process to finish.

### 4.7. Verify you are inside the dev container

1. Open a new terminal in VS Code.
2. Run:

```bash
pwd
git status
python --version
```

You should see your repository path and working toolchain available inside the container.
