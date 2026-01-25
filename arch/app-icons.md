# Application Icons

Change application icons when you open app launcher such as wofi or rofi

Using kitty as example

---

## 1. Copy Desktop File

Create Local Override Directory

```sh
mkdir -p ~/.local/share/applications
```

Copy Desktop File

```sh
cp /usr/share/applications/kitty.desktopa ~/.local/share/applications/
```

---

## 2. Edit Copied Desktop File

Open with neovim:

```sh
nvim ~/.local/share/applications/kitty.desktop
```

Find this line:

```desktop
Icon=kitty
```

Change it to your icon's path

```desktop
Icon=/home/unemotioned/.icons/kitty-icon.png
```

---

## 3. Update Desktop Database

```sh
update-desktop-database ~/.local/share/applications
```

---

### Happy Hacking 🎉
