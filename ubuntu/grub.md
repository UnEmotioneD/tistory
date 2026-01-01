# Grub

## Remove Unnecessary Items

Location of grub menu entries: `/etc/grub.d/`

```bash
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

```bash
sudo chmod -x {name of script}
```

## Reorder Items

Change index from `30_` to `09_` to put it above `10_linux`

```bash
sudo mv 30_os-prober 09_os-prober
```

## Cleaner GRUB Menu

Grub config file: `/etc/default/grub`

```bash
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

```bash
sudo update-grub
```

## Change Items Name

<!-- TODO: how to change grub menu item name -->

From `/etc/grub.d/`

Edit `40_custom`

Give execute permission

```bash
sudo chmod +x 40_custom
```

---

### Happy Hacking 🎉
