# Font

- Install nerd fonts for current user only

- [x] Meslo
- [ ] Jetbranins
- [ ] D2Coding

## Create Dir

- Create dedicated directory for fonts
- `cd` into it

```bash
mkdir -p ~/.local/share/fonts

cd ~/.local/share/fonts
```

## Install

- install `Meslo` with `wget`
- remove `.zip` file after unzip

```bash
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip
unzip Meslo.zip

rm Melso.zip
```

## Refresh Font Cache

```bash
fc-cache -fv
```

- check with grep

```bash
fc-list | grep meslo
```

## Use

- My go to

```toml
MesloLGS Nerd Fonts Mono
```
