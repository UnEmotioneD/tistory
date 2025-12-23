# sddm & hyprpaper

## sddm

- candy dark

```bash
yay -S sddm-sugar-dark
```

```bash
cd /
```

```bash
sudo nvim lib/sddm/sddm.conf.d/default.conf
```

under the [Theme]

add `sugar-dark` next to `Currnet=`

---

## hyprpaper (~/.config/hypr/hyprpaper.conf)

download img first

```bash
yay -S hyprpaper
```

`~/.config/hypr/hyprpaper.conf`

To find out the name of monitors

```sh
hyprctl monitors
```

```sh
preload = {path-to-wallpaper}
wallpaper = eDP-1, {path-to-wallpaper}

# boolean
# fill, fit, stretch, center, tile
splash = center
```

and in hyprland.conf file

add hyprpaper to autostart

under `misc` change the value of
`force_fefault_wallpaper` to 0
`disable_hyprland_logo` to true

this will make the default wallpaper go away

```sh
killall hyprpaper
```

```sh
hyprctl reload
```

## hyprlock

- [hyprwm/hyprlock github](https://github.com/hyprwm/hyprlock)
