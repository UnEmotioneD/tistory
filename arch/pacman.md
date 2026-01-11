# Pacman

How to use pacman

- [Install](#install)
- [Update](#update)
- [Remove](#remove)
  - [Remove orphaned](#remove-orphaned)
- [Search](#search)
  - [From Installed](#from-installed)
  - [From Online](#from-online)
- [Clear](#cleanup)

---

## Install

```sh
sudo pacman -S vim # normal install
sudo pacman -S --noconfirm neovim # without confirm
sudo pacman -S emacs --needed # reinstall
```

---

## Update

full upgrade(recommended):

```sh
sudo pacman -Syu
```

refersh package database only

```sh
sudo pacman -Sy
```

---

## Remove

just the specified package

```sh
sudo pacman -R nano
```

with dependencies

```sh
sudo pacman -Rs nano
```

with dependencies and config files

```sh
sudo pacman -Rns code
```

### Remove Orphaned

list orphaned

```sh
pacman -Qtdq
```

remove every orphaned

```sh
sudo pacman -Rns $(pacman -Qtdq)
```

---

## Search

### From Installed

search from database

```sh
pacman -Ss ttf-jetbrains
```

### From Online

list all every packages installed

`-Q` for Query

```sh
pacman -Q
```

list only installed explicitly(no dependencies)

```sh
pacman -Qe
```

dependencies only

```sh
pacman -Qd
```

---

## Cleanup

```sh
sudo pacman -Sc
```

```sh
sudo pacman -Scc
```

### With Tools

install `pacman-contrib` use `paccache` command

remove all cached

```sh
paccache -r
```

keep last 2 versions

```sh
paccahce -rk2
```

---

#### Happy Hacking 🎉
