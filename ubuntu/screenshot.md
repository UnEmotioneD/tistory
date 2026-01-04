# Flameshot

[flameshot - command line option](https://flameshot.org/docs/advanced/commandline-options/)

---

## Install with APT

```sh
sudo apt install flameshot
```

## Keybind with i3

keybind: Alt + Shift + j, k, l

- `gui` : select to capture
- `screen` : whole screen
- `full` : every thing on monitor

- copy to clipboard and save to path

```i3config
bindsym Mod1+shift+j exec --no-startup-id flameshot gui    --clipboard --path ~/Pictures/screenshots
bindsym Mod1+shift+k exec --no-startup-id flameshot screen --clipboard --path ~/Pictures/screenshots
bindsym Mod1+shift+l exec --no-startup-id flameshot full   --clipboard --path ~/Pictures/screenshots
```

---

## Happy Hacking 🎉
