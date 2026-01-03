# Yay

[DenshiVideo](https://www.youtube.com/watch?v=NzNuFN9hqjI)

- yay(wrapper for pacman) packagemanager
- which supports AUR(Arch User Repository)

## Prerequisite

Make sure you have `git` installed

```bash
sudo pacman -S git
```

Now clone the yay repository

## Download, build and install

```bash
git clone https://aur.archlinux.org/yay.git
```

```bash
cd yay
```

```bash
makepkg -si
```

This way will install `Go language` and build it from source

When you're done use `cd` to go to home directory and use

```bash
yay
```

To check if it is working and also to update the `yay` package manager

---

## What does yay or paru do

- [before using ARU helpr - Eric Murphy](https://www.youtube.com/watch?v=goOrF8zAkqU)

- sometimes aur helpers do break

- aur helper clones the package from git repository and build it with script

- too build locally you need `base-devel` package installed check it with
  (pacman -Q base-devel)

- after cloning the repo `cd` into it and do

```sh
makepkg
```

then it will download extra stuff such as `{$name, $version}.pkg.tar.zst`
now you can install it with pacman for example if you're installing `pfetch`

```sh
sudo pacman -U pfetch-0.6.0-3-any.pkg.tar.zst
```

to uninstall the package build from source locally you have to do

```sh
sudo pacman -Rs pfetch
```

### Simpler way

- flag `s` will download all the dependencies from pacman
- flag `i` will automatically install it with pacman

```sh
makepkg -si
```

Now you're done

### Downside

- Cannot update it with pacman or aur helpers

- To update it you have to pull it from source

- You can get notifications from arch wiki

---

### Happy Hacking 🎉
