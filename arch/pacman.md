# Pacman

How to use pacman

- Install
- Update
- Remove
- Remove Orphaned
- Search
- Search Installed
- Clear cache

## Install

```sh
sudo pacman -S vim # normal install
sudo pacman -S --noconfirm neovim # without confirm
sudo pacman -S emacs --needed # reinstall
```

## Update

full upgrade(recommended):

```sh
sudo pacman -Syu
```

refersh package database only

```sh
sudo pacman -Sy
```

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

## Search

### From Installed List

search from database

```sh
pacman -Ss ttf-jetbrains
```

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
