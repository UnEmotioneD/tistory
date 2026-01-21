# Fonts

Download and use fonts from online

---

## APT

```sh
sudo apt install fonts-nanum fonst-noto-cjk
```

---

## Manually

### Create Directory

Create directory where to download fonts:

```sh
mkdir -p ~/.local/share/fonts
```

### Download

Download from [`nerdfonts.com`](https://nerdfonts.com) or with `wget` and unzip

```sh
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip
mkdir ~/.local/share/fonts/Meslo # make directory for fonts
unzip Meslo.zip -d ~/.lcoal/share/fonts/Meslo # unzip into directory
```

### Fonts Cache

rebuild fonts cache:

- `-f`(force): rebuild including already built
- `-v`(verbose): show the outputs

```sh
fc-cache -fv
```

or font cache for all users

`/usr/local/share/fonts/`

```sh
sudo fc-cache
```

### List Installed Fonts

```sh
fc-list | grep "MesloLGS Nerd Font"
```

More cleaner:

- `-i`: ignore case

```sh
fc-list : family | grep -i iosevkatermslab
```

---

#### Happy Hacking 🎉
