# YOLO

## Install Ultralytics

[ultralytics quickstart](https://docs.ultralytics.com/quickstart/)

- `-U`: upgrade if already installed
- `--break-system-packages`: to by pass `externally managed environment` restriction on some Debian/Ubuntu distro from `python@3.12` and above

```sh
pip install -U ultralytics --break-system-packages
```

filesize: about 4GB
time took to install: about 55 min

### Extra Dependencies

```sh
pip install onnz onnxslim onnxruntim-gpu --break-system-packages
```

---

## robotflow

train model with robotflow

---

how to work with flask server

## when to send frames

```pseudo
if too close

  elif part of map

    go around

  elif not part of map

    send frames to server
```

`open cv` to check if there is a object

from robots detect interfering object

- human(standing, fallen)
- trash(squashed plastic bottle)
- small plastic bag of cookie
- plastic box of phills

---

## how to get image from robots

with flask sever

---

### Happy Hacking 🎉
