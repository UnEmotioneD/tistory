# Xremap

## Xremap for Hyprland

Install with `cargo`

```sh
cargo install xremap --features hypr
```

Stow xremap config from dotfiles

---

## Xremap Without Sudo

Create `udev` rule

```sh
echo 'KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/99-uinput.rules
```

Add user to `input` and `uinput` group

```sh
sudo groupadd -f uinput
sudo usermod -aG uinput,input $USER
```

Reload `udev` rules

```sh
sudo udevadm control --reload-rules && sudo udevadm trigger
```

Load `uinput` at boot

```sh
echo "uinput" | sudo tee /etc/modules-load.d/uinput.conf
```

---

## Launch On Login

Start `xremap` with it's config

```sh
exec-once = xremap ~/.config/xremap/config.yml
```

---

### Happy Hacking 🎉
