# Font

- Install nerd fonts for current user only

- [x] Meslo
- [ ] Jetbranins
- [ ] D2Coding

## Create Dir

Create dedicated directory for fonts

`cd` into it

```bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts
```

## Install

Install `Meslo` with `wget`

Remove `.zip` file after unzip

```bash
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip
unzip Meslo.zip
rm Melso.zip
```

## Refresh Font Cache

```bash
fc-cache -fv
```

Check with grep

```bash
fc-list | grep meslo
```

## Use

My favorite font

```toml
MesloLGS Nerd Fonts Mono
```

---

### Happy Hacking 🎉
