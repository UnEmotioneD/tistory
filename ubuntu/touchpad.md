# Touchpad

Enable tap to touch

---

## Find Touchpad

Find device name with `grep`

```sh
grep -i touchpad /proc/bus/input/devices
```

The output will be like following:

```sh
N: Name="{device-name}"

N: Name="MSNB0001:00 06CB:7E7E Touchpad"  # example
```

---

## Create Libinput Config

```sh
sudo nano /etc/X11/xorg.conf.d/30-touchpad.conf
```

---

## Touchpad Config

- `1 finger tap` &rarr; `left click`
- `2 finger tap` &rarr; `right click`
- `3 finger tap` &rarr; `middle click`

```conf
Section "InputClass"
    Identifier "Touchpad"
    MatchProduct "MSNB0001:00 06CB:7E7E Touchpad"
    MatchIsTouchpad "on"
    Driver "libinput"

    Option "Tapping" "on"
    Option "TappingButtonMap" "lrm"
    Option "ClickMethod" "clickfinger"
    Option "NaturalScrolling" "true"
    Option "DisableWhileTyping" "true"
EndSection
```

---

## Reboot

restart the laptop for the config to take effect

---

### Happy Hacking 🎉
