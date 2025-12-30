# Python Virtual Environment

- [create venv](#create-venv)
- [install modules](#install-modules)
- [deactivate](#deactivate)
- [aliases](#aliases)
- [freeze](#freeze)

## Create venv

Create to desired location

```bash
python3 -m venv {dir/venv-name}
```

Activate venv

```bash
source {venv-path}/bin/activate
```

Update `pip` from inside the `venv`

```bash
sudo pip3 install --upgrade pip
```

## Install Modules

For example

```bash
pip3 install numpy
```

## Deactivate

```bash
deactivate
```

---

## Aliases

```bash
alias von=". {venv-path}/bin/activate"
alias voff="deactivate"
```

## Freeze

Save environment exactly

```bash
pip freeze > requirements.txt
```

Recreate env

```bash
pip install -r requirements.txt
```

Refreeze after upgrades for safety

```bash
pip install --upgrade requests
pip freeze > requirements.txt
```

---

### Happy Hacking 🎉
