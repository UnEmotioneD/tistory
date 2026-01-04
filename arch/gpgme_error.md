# Pacman fix GPGME error

## 1. Back-up Mirrorlist

```sh
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
```

## 2. Generate Mirrorlist

[Pacman Mirrorlist Generator](https://archlinux.org/mirrorlist/)

On my case geenerating new mirrorlist caused error and the original list works
just fine without it

## 3. Re-generate Keys

re-generate the keys for pacman by first getting rid of the stored secrets

```sh
sudo rm -rf /etc/pacman.d/gnupg
sudo rm -R /var/lib/pacman/sync
```

can run pacman-key to initialize and re-generate the trust roots:

```sh
sudo pacman-key --init
sudo pacman-key --populate
```

## 4. Update Pacman

```sh
sudo pacman -Syyu
```

---

### Happy Hacking 🎉
