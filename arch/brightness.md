# Brillo

Human eye friendly brightness control

Changes brightness experientially

- [cameronnemo/brillo](https://gitlab.com/cameronnemo/brillo)
- [Eric Murphy - You're Probably Doing Screen Brightness in Arch Linux Wrong](https://www.youtube.com/watch?v=pGOaSS8nEQA&t=437s)

---

## Installation

### 1. Dependency

```sh
sudo pacman -Syu go-md2man
```

### 2. Build

```sh
mkdir ~/Repository
cd ~/Repository
git clone https://gitlab.com/cameronnemo/brillo.git
make
```

### 3. Install

with `setgid` every users can use without extra permissions

```sh
sudo make install.setgid
```

---

## Usage

inside `~/.config/hypr/hyprland.conf` replace the `brightnessctl s 10%+` with `brillo`:

```sh
brillo -q -u 1000 -A 5  # brightness up
brillo -q -u 1000 -U 5  # brightness down
```

- `-q` : change brightness experientially
- `-u` : fade animation 1000ms == 0.1sec
- `-A` : brightness up
- `-U` : brightness down

## Notes

- reboot for brillo to work

---

### Happy Hacking 🎉
