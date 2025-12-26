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

- from gnome-terminal

```bash
sudo apt update && sudo apt upgrade -y
```

- enable fire wall

```bash
sudo ufw enable
```

### Install Recommended Packages

- build-essential
- git
- curl

```bash
sudo apt install build-essential git curl
```

---

## Korean Input

- from terminal

```bash
sudo apt install ibus-hangul
```

- restart

- settings
  - keyboard
    - add input source
      - korean(hangul)

- korean(hangul) 3-dot menu
  - preference
    - hangul toggle key: right alt(remove other keys)
      - remove english(us) from input source

### Keyboard Shortcuts

- in debian/ubuntu windows key is called super

- terminal: super + enter
- browser: super + b
- search: alt + space

---

## Download and Install

- download files with .deb which is for debian/ubuntu

- move into downloads directory

```bash
cd Downloads/
```

- install with dpkg(debian package) command

```bash
sudo dpkg -i {name of the .deb file}
```

- you can pass multiple file names as arguments for dpkg command

- google chrome

- vscode

- to run ipynb file from vscode install `pip3` and `ipynb kernel`

```bash
sudo apt install python3-pip
pip3 install --user ipykernel
```

---

## Fix Bluetooth

```bash
sudo systemctl enable bluetooth  # turn bt
sudo systemctl start bluetooth   # start bt on every login
```
