# Kitty

On Debian/Ubutu kitty installed with apt is not update to date which miss out on
feature such as cursor trail here is how to install the latest version

[kitty install](https://sw.kovidgoyal.net/kitty/binary/)

## List of Contents

- [Install Binary](#install-binary)
  - [Update](#update)
- [Desktop Integration](#desktop-integration)
- [i3wm keybind](#i3wm-keybind)
- [Config](#config)
- [Remove](#remove)

---

## Use Bin PATH

make sure you have the following line inside `~/.zshrc`:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

---

## Install Binary

install pre-built binary

```sh
curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
```

### Update

re-run the command used to install binary

---

## Desktop Integration

create symlinks and .desktop files to make it launchable with app launcher

```sh
# Create symbolic links to add kitty and kitten to PATH (assuming ~/.local/bin is in your system-wide PATH)
ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/
# Place the kitty.desktop file somewhere it can be found by the OS
cp ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/
# If you want to open text files and images in kitty via your file manager also add the kitty-open.desktop file
cp ~/.local/kitty.app/share/applications/kitty-open.desktop ~/.local/share/applications/
# Update the paths to the kitty and its icon in the kitty desktop file(s)
sed -i "s|Icon=kitty|Icon=$(readlink -f ~)/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" ~/.local/share/applications/kitty*.desktop
sed -i "s|Exec=kitty|Exec=$(readlink -f ~)/.local/kitty.app/bin/kitty|g" ~/.local/share/applications/kitty*.desktop
# Make xdg-terminal-exec (and hence desktop environments that support it use kitty)
echo 'kitty.desktop' > ~/.config/xdg-terminals.list
```

without comments:

```sh
ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/
cp ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/
cp ~/.local/kitty.app/share/applications/kitty-open.desktop ~/.local/share/applications/
sed -i "s|Icon=kitty|Icon=$(readlink -f ~)/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" ~/.local/share/applications/kitty*.desktop
sed -i "s|Exec=kitty|Exec=$(readlink -f ~)/.local/kitty.app/bin/kitty|g" ~/.local/share/applications/kitty*.desktop
echo 'kitty.desktop' > ~/.config/xdg-terminals.list
```

---

## I3WM Keybind

Launch `kitty` with title option

```sh
bindsym $mod+Return exec --no-startup-id ~/.local/kitty.app/bin/kitty --title "Kitty"
```

---

## Config

- [kitty.conf](https://sw.kovidgoyal.net/kitty/conf/)

Reload kitty config with `Ctrl + Shift + F5`

---

## Remove

### Binary

```sh
rm -rf ~/.local/kitty.app
```

### Symlinks

```sh
rm -f ~/.local/bin/kitty ~/.local/bin/kitten
```

### Desktop Files

```sh
rm -f ~/.local/share/applications/kitty.desktop
rm -f ~/.local/share/applications/kitty-open.desktop
```

### Undo Terminal Preference

```sh
rm -f ~/.config/xdg-terminals.list
```

### Confirm Revomal

```sh
which kitty
```

---

#### Happy Hacking 🎉
