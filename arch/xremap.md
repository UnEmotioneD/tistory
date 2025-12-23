# Remap keys with xremap

## Install xremap for hyprland with cargo

```sh
cargo install xremap --features hypr
```

- mtow xremap config from dotfiles directory

## xremap without sudo

- create `udev` rule

```sh
echo 'KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/99-uinput.rules
```

- add user to `input` and `uinput` group

```sh
sudo groupadd uinput
sudo usermod -aG uinput,input $USER
```

- and reload the `udev` rules

```sh
sudo udevadm control --reload-rules && sudo udevadm trigger
```

- load `uinput` at boot

```sh
echo "uinput" | sudo tee /etc/modules-load.d/uinput.conf
```

## Add to hyprland.conf

- start xremap with config on startup with `exec`

```sh
exec = xremap ~/.config/xremap/config.yml
```
