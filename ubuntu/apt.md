# Advanced Package Tool

## List of Content

- [Before Use](#before-use)
- [How to Use](#how-to-use)
- [Info](#info)
- [Flags](#flags)
- [Cleanup](#cleanup)
- [Fix Install](#fix-install)

---

## Before Use

- `sudo`: Super User Do
  - install, remove, update
  - modifying sys files(/etc, /usr, /bin, ...)
  - managing services
  - changing user

Update apt

```bash
sudo apt update
```

Checkout outdated packages first

```bash
apt list --upgradeable
```

Update outdated pkg

```bash
sudo apt upgrade
```

Keep pkg from automatically updated

```bash
sudo apt-mark hold openjdk-17-jdk
```

Use `unhold` to undo mark

---

## How To Use

You can pass more then one argument

```bash
sudo apt install {pkg} {pkg} ...
```

---

## Info

`Search` from `APT` repository

```bash
apt search {pkg}
```

`List` out installed packages

```bash
apt list --installed
```

Use `show` flag to show package details

---

## Flags

`--yes` or `-y`: automatic yes

`--quiet` or `-q`: quieter output

`--no-install-recommends` or `--no-install-reco`

`--reinstall`

`--purge`

---

## Cleanup

- `autoremove`: remove unused dependencies
- `clean`: clear download cache

```bash
sudo apt autoremove
sudo apt clean
```

---

## Fix Install

### Fix Broken Dependencies

```sh
sudo apt install -f
```

### Check not being upgraded

```sh
sudo apt dist-upgrade -a
```

You may install the package separated

### Run Final Upgrade

```sh
sudo apt full-upgrade -y
```

---

#### Happy Hacking 🎉
