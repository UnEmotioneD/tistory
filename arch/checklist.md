# Arch Linux Checklist

- [x] install arch

- [x] connect wifi, bluetooth
- [x] install yay
- [x] nerd fonts

- [x] Korean input and fonts

- [x] kitty, tmux and nvim config via gnu stow
- [ ] rice hyprpaper
- [ ] rice hyprland
- [ ] rice waybar
- [x] change key repeat and delay for keyboard
- [x] change mouse sensitivity for each device
- [ ] change kensington button input
- [x] enable natural scroll
- [ ] set display resolution and multiplier for 4K TV
- [ ] sound setting (turn off beep when backspace meets dead end)
- [x] brightness
- [ ] battery, power management
- [x] clipboard(aur:wl-clipboard)

- [ ] bat (code preview)
- [x] sessionizer (create tmux session)
- [x] yazi (terminal file explorer)

- [ ] fd
- [ ] fzf
- [ ] delta
- [ ] eza
- [ ] zoxide

- [ ] set up for java development
- [ ] set up for python development
- [ ] set up for database development
- [ ] set up for react development

---

## How to search for packages

```sh
pacman -Ss {Package Name}
```

```sh
yay -Ss {Package Name}
```

---

## Install fonts

Install it with pacman

`noto-fonts-emoji` for neovim devicon and mini.icons

```sh
sudo pacman -S ttf-meslo-nerd
```

Check installed

```sh
fc-list | grep "MesloLGS"
```

Update font cache

```sh
fc-cache -fv
```

---

## Set node.js, npm PATH

inside `~/.bashrc`

```sh
export PATH=$PATH:/usr/bin
```

---

## ricing hypr

At `~/.config/hypr/hyprland.conf`

- remove border radius

```sh
decoration {
    founding = 0
    ...
}
```

- enable natural scrolling

```sh
touchpad {
    natural_scroll = true
}
```

- change key repeat rate
  - add the following fields inside input

```sh
input {
    ...
    repeat_delay = 300
    repeat_rate = 50
    ...
}
```

under input

```sh
input {
    ...
    accel_profile = flat # for no ecceleration
    ...
}
```

---

## Installed packages

### general usage

firefox

bluez
bulez-utils
blueman

brightnessctl (just install it and you're good to go)
go-md2man
brillo

pipewire
pipewire-pulse
pipewire-audio
pipewire-alsa
wireplumber

fcitx5-im
fcitx5-hangul
fcitx5-configtool

### terminal && dev

kitty
stow
tmux
tpm
neovim (to install LSP node.js and npm needs to be installed and set to path)
unzip (to unzip some LSP)

git
nodejs (in pacman there is no "node")
npm
yarn
python3

### hyprland eco system

waybar
hyprpaper

---

### Installed Fonts

ttf-meslo-nerd
firacode
ttf-d2coding

adobe-source-han-sans-kr-fonts
adobe-source-han-serif-kr-fonts
ttf-nanum (from AUR w/ yay)
