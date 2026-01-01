# Check List

## Setting

- display
  - resolution
  - refresh rate

- power
  - power mode: performance
  - screen blank: never

- ubuntu desktop
  - position of new icons: top left
  - auto-hide dock: on
  - panel mode: off
  - position on screen: bottom
  - configure dock behavior
    - include unmounted volume: uncheck

- mouse & trackpad
  - 10cm from edge to edge horizontally

- appearance
  - style: dark

- accessibility
  - typing
    - typing assist
      - repeat keys
        - speed: fast
        - delay: short

---

## Update

From `gnome-terminal`

```bash
sudo apt update && sudo apt upgrade -y
```

Do not enable `ufw` to connect to `pinky` later

```bash
sudo ufw disable
```

### Install Recommended Packages

- git
- curl
- build-essential

```bash
sudo apt install git curl build-essential
```

---

## Korean Input

From `gnome-terminal`

```bash
sudo apt install ibus-hangul
```

Reboot for the right option to show up

- settings
  - keyboard
    - add input source
      - korean(hangul)

- korean(hangul) 3-dot menu
  - preference
    - hangul toggle key: right alt(remove other keys)
      - remove english(us) from input source

### Keyboard Shortcuts

In debian/ubuntu windows key is called `super`

- terminal: super + enter
- browser: super + b
- search: alt + space

- To disable
  - hide window: super + h
  - logout: super + l

---

## Download and Install

- google chrome
- visual studio code
- slack

Download files with `.deb` which is for debian/ubuntu

cd into downloads directory from terminal

```bash
cd Downloads/
```

Install with dpkg(debian package) command

```bash
sudo dpkg -i {name of the .deb file}
```

You can pass multiple file names as arguments for `dpkg` command

- to run ipynb file from vscode install `pip3` and `ipykernel`
  - `ipykernel`: to run from locally from vscode
  - `jupyter`: to run from venv

```bash
sudo apt install python3-pip python3-ipykernel
```

---

## Fix Bluetooth

```bash
sudo systemctl enable bluetooth  # turn bt on
sudo systemctl start bluetooth   # start bt every login
```

---

### Happy Hacking 🎉
