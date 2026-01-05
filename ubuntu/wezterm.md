# Wezterm

- Configuration with `Lua`
- Supports image rendering with `yazi`

How to install/uninstall on Debian/Ubuntu Linux and configure

---

## Table of Contents

- [Install](#install)
- [Configuration](#configuration)
  - [Stylua](#stylua)
- [Uninstall](#uninstall)

---

## Install

- [Wezterm Install](https://wezterm.org/install/linux.html)

```bash
curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg

echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list

sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
```

[chmod?](permission.md)

```bash
sudo apt update
```

Install `wezterm` or `wezterm-nightly`

```bash
sudo apt install wezterm
```

---

## Configuration

Reference: [`Josean - Wezterm`](https://www.josean.com/posts/how-to-setup-wezterm-terminal)

Config file location: `~/.config/wezterm/wezterm.lua`

The config:

```lua
-- Call wezterm config API
local wezterm = require('wezterm')

return {
  font = wezterm.font('MesloLGS Nerd Font'),
  font_size = 14,

  -- disable wezterm tab bar
  enable_tab_bar = false,

  -- disable all default padding values
  window_padding = {
    left = 0,
    right = 0,
    top = 0,
    bottom = 0,
  },

  color_scheme = 'tokyonight-storm',

  -- explicitly set fps
  max_fps = 144,
}
```

### Stylua

Place `.stylua.toml` file under the `~/.config/wezter/` with `wezterm.lua` file

```toml
indent_type = "Spaces"
indent_width = 2
quote_style = "AutoPreferSingle"

[sort_requires]
enabled = true
```

---

## Uninstall

```bash
sudo apt remove wezterm
```

```bash
sudo apt purge wezterm
```

Remove wezterm apt repo

```bash
sudo rm /etc/apt/sources.list.d/wezterm.list
```

remove gpg key

```bash
sudo rm /usr/share/keyrings/wezterm-fury.gpg
```

---

### Happy Hacking 🎉
