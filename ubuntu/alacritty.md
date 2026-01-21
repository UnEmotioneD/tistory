# Alacritty

Install latest version of alacritty on Ubuntu

- [Install](#install)
  - [Add PPA](#add-ppa)
  - [UPdate APT](#update-apt)
  - [Install Alacritty](#install-alacritty)
  - [Check Version](#check-version)
- [Uninstall](#uninstall)
  - [Remove Alacritty](#remove-alacritty)
  - [Remove PPA](#remove-ppa)

---

## Install

### Add PPA

```sh
sudo add-apt-repository ppa:aslatter/ppa
```

### Update APT

```sh
sudo apt update
```

### Install Alacritty

```sh
sudo apt install alacritty
```

### Check Version

```sh
alacritty --version
```

---

## Uninstall

### Remove Alacritty

```sh
sudo apt remove alacritty
sudo apt purge alacritty
```

### Remove PPA

```sh
sudo add-apt-repository --remove ppa:aslatter/ppa
sudo apt update
```

Check uninstalled

```sh
which alacritty
```

---

#### Happy Hacking 🎉
