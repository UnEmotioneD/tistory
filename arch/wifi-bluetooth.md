# wifi-bluetooth

## Fix bluetooth

[Eric Murphy](https://www.youtube.com/watch?v=rOL-T31l0lQ&list=WL&index=3)

Install `bluez`(bluetooth) and `bluez-utils`(command line utilities ...)

```sh
sudo pacman -S bluez bluez-utils
```

Check if the bluetooth module is running and `btusb` is loaded

```sh
lsmod | grep btusb
```

If the list shows up you're good else run this command

```sh
modprobe btusb
```

Start it with ...

```sh
sudo systemctl start bluetooth.service
```

Enable it and start bluetooth every time when the computer is started

```sh
sudo systemctl enable bluetooth.service
```

You can setup bluetooth in GUI with `blueman` package if installed

```sh
blueman-manager
```

Enter bluetooth mode

```sh
bluetoothctl
```

Turn on the BT controller

```sh
power on
```

and the agent

```sh
agent on
```

Agent will connect to trusted BT device when PC is started

```sh
default-agent
```

list bluetooth devices with ...

```sh
scan on
```

or ...
which will show the MAC address and name of the device

```sh
devices
```

connect it

```sh
turst {MAC address}
```

pair it

```sh
pair {Mac address}
```

for keyboards you will have to enter passkey

and connect it for real

```sh
connect {Mac address}
```

now turn of the messages in terminal

```sh
scan off
```

To enable BT every time you start up your PC
open BT conf file with sudo privileges

```sh
sudo nvim /etc/bluetooth/main.conf
```

Uncomment the `AutoEnable = true`

---

### Happy Hacking 🎉
