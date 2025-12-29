# Developer Environment

- vscode
- python
- jupyter
- cuda

## Python

- python3-pip
- python3-ipykernel

```bash
sudo apt install python3-full python3-pip python3-ipykernel
```

update `pip3` to latest version

`--break-system-packages`: for py ver higher then 3.12

```bash
pip3 install --upgrade pip --break-system-packages
```

---

## Python Virtual Environment

create venv to desired location


```bash
python3 -m venv {dir/venv-name}
```

activate venv

you can use `.` instead of `source`

```bash
source {venv-path}/bin/activate
```

- also update the `pip` inside the venv

turn if off

```bash
deactivate
```

---

## Jupyter Notebooks

- jupyter-core

```bash
sudo apt install jupyter-core
```
