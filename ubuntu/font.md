# Font

- Install nerd fonts for current user only

- [x] Meslo
- [x] Jetbrains
- [ ] D2Coding

## Create Dir

Create dedicated directory for fonts

`cd` into it

```sh
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts
```

## Install

Install `Meslo` with `wget`

Remove `.zip` file after unzip

### Meslo Nerd Fonts

```sh
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip
unzip Meslo.zip
rm Melso.zip
```

### JetBrains

```sh
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip
unzip JetBrainsMono.zip
rm JetBrainsMono.zip
```

## Refresh Font Cache

```sh
fc-cache -fv
```

Check with grep

```sh
fc-list | grep meslo
```

## Use

My favorite font

```toml
MesloLGS Nerd Fonts Mono

JetBrainsMono Nerd Font
```

---

### Happy Hacking 🎉
