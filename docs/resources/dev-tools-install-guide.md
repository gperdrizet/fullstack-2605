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

```bash
git --version
```

You should see a version number.

**Official references**

1. [Download page](https://git-scm.com/download/win)
2. [Official Pro Git book (installation)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 1.2. Install Docker

1. Go to https://www.docker.com/products/docker-desktop.
2. Download Docker Desktop for Windows.
3. Run the installer and complete setup.
4. Restart your machine if prompted.
5. Open Docker Desktop and wait for it to finish starting.
6. In PowerShell, run:

```bash
docker --version
docker run hello-world
```

If successful, Docker prints a welcome message.

**Official references**

1. [Docker Desktop download](https://www.docker.com/products/docker-desktop)
2. [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install)
3. [Docker getting started](https://docs.docker.com/get-started)

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

**Official references**

1. [VS Code download](https://code.visualstudio.com/Download)
2. [Windows setup guide](https://code.visualstudio.com/docs/setup/windows)
3. [Command line usage](https://code.visualstudio.com/docs/editor/command-line)

### 1.4. Install the Dev Containers extension

1. Open VS Code.
2. Open the Extensions view with `Ctrl+Shift+X`.
3. Search for "Dev Containers".
4. Install the extension published by Microsoft (id: `ms-vscode-remote.remote-containers`).

**Official references**

1. [Dev Containers documentation](https://code.visualstudio.com/docs/devcontainers/containers)

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

**Official references**

1. [Official Pro Git book (installation)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [macOS tools (xcode-select)](https://developer.apple.com/library/archive/technotes/tn2339/_index.html)

### 2.2. Install Docker

1. Go to https://www.docker.com/products/docker-desktop/.
2. Download Docker Desktop for Mac (choose Apple Silicon or Intel correctly).
3. Open the downloaded file and drag Docker to Applications.
4. Start Docker Desktop from Applications.
5. Complete any permission prompts.
6. In Terminal, run:

```bash
docker --version
docker run hello-world
```

If successful, Docker prints a welcome message.

**Official references**

1. [Docker Desktop download](https://www.docker.com/products/docker-desktop/)
2. [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
3. [Docker getting started](https://docs.docker.com/get-started/)


### 2.3. Install VS Code

1. Go to https://code.visualstudio.com/.
2. Download VS Code for macOS.
3. Move VS Code to Applications.
4. Open VS Code.
5. Open Command Palette with `Cmd+Shift+P`.
6. Run command: Shell Command: Install 'code' command in PATH.
7. In Terminal, run:

```bash
code --version
```

You should see a version number.

**Official references**

1. [VS Code download](https://code.visualstudio.com/)
2. [macOS setup guide](https://code.visualstudio.com/docs/setup/mac)
3. [Command line usage](https://code.visualstudio.com/docs/editor/command-line)


### 2.4. Install the Dev Containers extension

1. Open VS Code.
2. Open the Extensions view with `Cmd+Shift+X`.
3. Search for "Dev Containers".
4. Install the extension published by Microsoft (id: `ms-vscode-remote.remote-containers`).

**Official references**

1. [Dev Containers documentation](https://code.visualstudio.com/docs/devcontainers/containers)

## 3. Final check

Run these in Terminal (macOS) or PowerShell (Windows):

```bash
git --version
docker --version
code --version
```

All three should return version numbers.
