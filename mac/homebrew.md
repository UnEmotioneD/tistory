# Homebrew

- macOS package manager

## List of Content

- [Install Homebrew](#install-homebrew)
- [Use Homebrew](#use-homebrew)
  - [Pin Package Version](#pin-package-version)

## Install Homebrew

execute following command in terminal

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

add homebrew to path (change the user name to yours)

- for apple silicon mac:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/unemotioned/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

- intell cpu mac:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/unemotioned/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

or copy it from the installation prompt

check if installed

```bash
brew --version
```

## Use Homebrew

search for packages

```bash
brew search {pkg}
```

list installed

```bash
brew list
```

you can pipe with grep

```bash
brew list | grep {pkg}
```

install cli package

```bash
brew install {pkg}
```

install desktop application

```bash
brew install --cask {pkg}
```

remove packages

or with `--cask` to remove desktop app

```bash
brew uninstall {pkg}
```

update homebrew itself

```bash
brew update
```

update homebrew installed outdated packages installed

```bash
brew upgrade
brew upgrade --cask
```

remove orphaned packages

```bash
brew autoremove
```

show orphaned packages before actually removing

```bash
brew autoremove --dry-run
```

clear cache

```bash
brew clean
```

check homebrew health

```bash
brew doctor
```

### Pin Package Version

keep the `brew upgrade` from updating the package

```bash
brew pin openjdk@17
```

show the pinned packages with `--pinned` flag

```bash
brew list --pinned
```

or list outdated packages before `upgrade`

```bash
brew outdated
```
