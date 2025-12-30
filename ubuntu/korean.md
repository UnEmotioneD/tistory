# Korean

- How to setup korean(hangul) input on i3 with fcitx5

## Install Required

```bash
sudo apt install fcitx5 fcitx5-hangul fcitx5-configtool
```

- recommended

```bash
sudo apt install fonts-noto-cjk
```

- inside `.profile`(bash) or `.zprofile`(zsh)

```bash
export XMODIFIERS=@im=fcitx
export INPUT_METHOD=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
```

## Fcitx5

Launch `fcitx5-config-qt`

Search `hangul` from right side of window and move it to left side.
From `global option` tab use right alt to change input source.
