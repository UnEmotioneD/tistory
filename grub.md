# Grub

Customize grub menu to have bigger text and just the items you need

## Remove Unnecessary Items

Location of grub menu entries: `/etc/grub.d/`

```sh
cd /etc/grub.d
ls -l # or ll
```

Output is something like this

```console
00_header
05_debian_theme
10_linux        # Ubuntu
30_os-prober    # Windows

...
```

Remove execute permission from scripts to hide

```sh
sudo chmod -x {name of script}
```

## Reorder Items

Change index from `30_` to `09_` to put it above `10_linux`

```sh
sudo mv 30_os-prober 09_os-prober
```

## Cleaner GRUB Menu

Grub config file: `/etc/default/grub`

```sh
cd /etc/default/
sudo nvim grub
```

For cleaner menu add line

```conf
GRUB_DISABLE_SUBMENU=y
```

Uncomment following lines

```conf
GRUB_DISABLE_LINUX_UUID=true

GRUB_DISABLE_RECOVERY="true"
```

Optionally set timeout

```conf
GRUB_TIMEOUT=10
```

Save and run

```sh
sudo update-grub
```

---

### GRUB Menu Resolution

from grub menu press c to go into terminal

- Newer BIOS

```sh
videoinfo
```

- Older BIOS

```sh
vbinfo
```

from the supported resolutions select one

- lower resolution have lower input delay and bigger texts

back into the grub config file `/etc/default/grub`

- from auto to desired option

```console
GRUB_FGXMODE=640x480
```

recreate the grub config

- Arch / Fedora

```sh
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

- Debian/Ubuntu/Mint

```sh
sudo update-grub
```

---

#### Happy Hacking 🎉
