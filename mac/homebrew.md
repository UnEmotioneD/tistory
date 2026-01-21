# Homebrew

- macOS package manager

## List of Content

- [Install Homebrew](#install-homebrew)
- [Use Homebrew](#use-homebrew)
  - [Pin Package Version](#pin-package-version)

## Install Homebrew

execute following command in terminal

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

add homebrew to path (change the user name to yours)

- for apple silicon mac:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/unemotioned/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

- intell cpu mac:

```sh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/unemotioned/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

or copy it from the installation prompt

check if installed

```sh
brew --version
```

## Use Homebrew

search for packages

```sh
brew search {pkg}
```

list installed

```sh
brew list
```

you can pipe with grep

```sh
brew list | grep {pkg}
```

install cli package

```sh
brew install {pkg}
```

install desktop application

```sh
brew install --cask {pkg}
```

remove packages

or with `--cask` to remove desktop app

```sh
brew uninstall {pkg}
```

update homebrew itself

```sh
brew update
```

update homebrew installed outdated packages installed

```sh
brew upgrade
brew upgrade --cask
```

remove orphaned packages

```sh
brew autoremove
```

show orphaned packages before actually removing

```sh
brew autoremove --dry-run
```

clear cache

```sh
brew clean
```

check homebrew health

```sh
brew doctor
```

### Pin Package Version

keep the `brew upgrade` from updating the package

```sh
brew pin openjdk@17
```

show the pinned packages with `--pinned` flag

```sh
brew list --pinned
```

or list outdated packages before `upgrade`

```sh
brew outdated
```

### Unping Package

```sh
brew unpin openjdk@17
```
