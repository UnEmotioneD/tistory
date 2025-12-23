# After installing Arch linux

- [10 things you must do after installing arch linux by Ksk Royal](https://www.youtube.com/watch?v=odgD_RdJjCU)

## Pacman

### Configure

Open /etc/pacman.conf with sudo previliages

```sh
sudo nvim /etc/pacman.conf
```

Under `[options]` and `# Misc options` uncomment `Color`

Add `ILoveCandy` to make the download progress bar to look like the pacman game

and update the pacman

```sh
sudo pacman -Sy
```

### Increase download speed

Install `reflector` with pacman

```sh
sudo pacman -S reflector
```

Create backup of default mirror list

```sh
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
```

then fetch the top 10 fastest servers

```sh
sudo reflector --verbose --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

and update the pacman again

---

## Additional kernels

- Install LTS as a backup

```sh
sudo pacman -S linux-lts linux-lts-headers
```

---

## TimeShift

- For backing up the arch linux

```sh
yay -Sy timeshift
```

---

## Firewall

- Uncomplicated FireWall
- Fro protecting your PC from network traffic

### Install

```sh
yay -Sy timeshift
```

```sh
sudo systemctl enable ufw
```

```sh
sudo systemctl start ufw
```

### Disable for specific port

- For Example disabling it for SSH on port 22

```sh
sudo ufw deny 22/tcp
```

---

## Auto CPU feq

- From the `~/Repository`
- Clone the source code from github

```sh
git clone https://github.com/AdnanHodzic/auto-cpufreq.git
```

move into auto-cpufreq dir

```sh
cd auto-cpufreq
```

and set it up

```sh
sudo ./auto-cpufreq-installer
```

Start service as daemon this will force to put the Laptop's power mode to balance

```sh
sudo auto-cpufreq --install
```

Verify it's running status

```sh
sudo systemctl status auto-cpufreq
```

Too see the system resources run this cmd

```sh
sudo auto-cpufreq --stats
```
