# Improved Improved Improved Window Manager

## Referenced Video

- [Type craft](https://www.youtube.com/@typecraft_dev/featured)
  - [i3 pt1](https://www.youtube.com/watch?v=xWIDvnNFl5I)
  - [i3 pt2](https://www.youtube.com/watch?v=wXZgUudR41I)

- [Alex Booker](https://www.youtube.com/@bookercodes/videos)
  - [how to rice](https://www.youtube.com/watch?v=ARKIwOlazKI&t=126s)

## Install Packages

- `alacritty`: default terminal for `i3`
- `dmenu`: app launcher
- `feh`: wallpaper
- `i3`: the window manager
- `i3lock`: lock screen
- `i3status`: statusbar
- `picom`: compositer(fixes screen tearing)

```bash
sudo apt install -y i3 i3status i3lock feh picom dmenu arendr
```

---

## Start i3wm

- logout
- select i3

---

## Configure

- config file: `~/.config/i3/config`

---

## Key Binding

- windows key to mod
- mod + h, j, k, l for changing focus
- mod + y, u, i, o, p, n, m for workspaces
- screen shot

### Default Key

- mod + r: resize
- mod + s: stack mod
- mod + v: next window will open in vertical position

- mod + shit + r: reload i3 config
- mod + shit + q: quite app

---

## Status bar

- left: workspaces
- right: input source, wifi, bluetooth, speaker, cpu, temperature batter, time

---

## Wallpaper

- Lauch `feh` on login

```text
exec_alwyas --no-startup-id ~/.fehbg
exec_always feh --bg-scale {absolute path to the image}
```

---

## App Launcher

- dmenu
- rofi(better app launcher)

---

## Assign App to Workspace

---

## Multiple Monitor
