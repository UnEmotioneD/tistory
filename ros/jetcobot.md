# Jetcobot

6 axis arm robot with camera connected to `raspberry-pi`

---

## List of Content

- [Change DNS](#change-dns)
- [SSH](#ssh)
- [VSCode Extension](#vscode-extension)
- [Jupyter From Jetcobot](#jupyter-from-jetcobot)

---

## Change DNS

Connect to jetcobot wifi and change ipv4 dns to `8.8.8.8`

Get name of connected wifi

```bash
nmcli device status
```

Check current wifi dns setting

```bash
nmcli device show {SSID} | grep IP4.DNS
```

- `8.8.8.8`: Primary DNS to `Google`
- `1.1.1.1`: Secondary DNS to `Cloudflare`

Just one primary is enough

```bash
nmcli con mod "{wifi-name}" ipv4.ignore-auto-dns yes
nmcli con mod "{wifi-name}" ipv4.dns "8.8.8.8 1.1.1.1"
# reconnect
nmcli con down "{wifi-name}"
nmcli con up "{wifi-name}"
```

- `con`: connection
- `mod`: modify

Jetcobot wifi password: `jetcobot`

---

## SSH

Jetcobot IP address: `192.168.5.1`

```bash
ssh jetcobot@192.168.5.1
```

Jetcobot user password: `1`

Connect to wifi by running script from terminal:

```bash
./wifi_setup.sh
```

---

## VSCode Extension

From vscode extension install `SSH Remote`.
And click on the bottom right terminal or shell icon to connect to host.
Do the things and you can view jetcobot directories from vscode.

---

## Jupyter from Jetcobot

create vevn inside jetcobot

inside venv update `pip` and `pymycobot`

inside venv install `opencv-python` and `jupyter`

to open jupyter notebook inside jetcobot:

```sh
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
```

from local machine's browser enter

```sh
192.168.5.1:8888/tree
```

---

### Happy Hacking 🎉
