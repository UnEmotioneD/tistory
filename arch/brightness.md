# Brightness control with Brillo

## Brillo

- Human eye friendly brightness control

- [brillo gitlab](https://gitlab.com/cameronnemo/brillo)
- [Eric Murphy](https://www.youtube.com/watch?v=pGOaSS8nEQA&t=437s)

- Dependency: `go-md2man`

### Installation

Install `go-md2man` with pacman first

Create directory to clone the source

```sh
mkdir ~/Repository
```

and clone it

this will create brillo dir

```sh
git clone https://gitlab.com/cameronnemo/brillo.git
```

move into the dir and build it

```sh
make
```

`.setgid` to make this useable for all users

```sh
sudo make install.setgid
```

Now you are ready to use

### Configure

At `~/.config/hypr/hyprland.conf`

go to brightness

change the brightnessctl s 10%+ with the following

```sh
brillo -q -u 1000 -A 5
```

-q : change brightness experientially
-u {integer-value-in-ms} : fade animation 1000ms == 0.1sec
-A : brightness up
-U : brightness down

do the same to brightness down

#### Reboot the PC for this to take effect
