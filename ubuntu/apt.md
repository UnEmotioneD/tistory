# Advanced Package Tool

## Before Use

- `sudo`: Super User Do
  - install, remove, update
  - modifying sys files(/etc, /usr, /bin, ...)
  - managing services
  - changing user

- Update apt

```bash
sudo apt update
```

- Update outdated pkg

```bash
sudo apt upgrade
```

## How To Use

- you can pass more then one argument

```bash
sudo apt install {pkg}
```

```bash
sudo apt remove {pkg}
```

## Info

- `Search`

```bash
apt search {pkg}
```

- `list`

```bash
apt list --installed
```

- `show`: show pkg details

### Flags

- `--yes`: automatic yes

```bash
sudo apt install -y {name of package}
```

- `--quiet`: quieter output

```bash
sudo apt install -q {pkg}
```

- `--no-install-recommends`

```bash
sudo apt install --no-install-reco {pkg}
```

- `--reinstall`
- `--purge`

## Cleanup

- `autoremove`: remove unused dependencies
- `clean`: clear downloaded pkg cache

```bash
sudo apt autoremove
sudo apt clean
```
