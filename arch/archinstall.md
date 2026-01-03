# Arch Install

## Install Environment

- Thinkpad T14 Gen4, intel CPU & integrated GPU
- Dual boot with Windows 11

## Referenced YouTube

use `archinstall` script

- [Ksk Royal](https://www.youtube.com/watch?v=4dKzYmhcGEU&list=WL&index=2&t=796s)

## List of contents

- [Before Install](#before-install)
- [Inside Install Drive](#inside-install-drive)
  - [Synchronize to DB](#synchronize-to-databases)
  - [Partition](#partition)
  - [Format Partitions](#format-partitions)
  - [Mount Partitions](#mount-partitions)
  - [start install](#start-install)
- [Grub](#grub)
- [Login to Hyprland](#login-to-hyprland)
- [Wi-Fi with nmcli](#wi-fi-with-nmcli)
- [Add Windows to GRUB](#windows-entry-to-grub-menu)
- [Delete Arch](#delete-arch)
  - [Clean Install USB](#clean-install-usb)

---

## Before Install

### Create Disk Space

Use windows `disk mamanger` create at least 40GB of free space

### Enter BIOS

Thinkpad: press `Ender` from boot screen and `F1`

```sh
Security > Secure Boot
```

- Secure Boot: off
- Clear All Secure Boot Keys
- Allow Microsoft 3rd Party UEFI CA: off

Save and restart: `F10`

Press enter again then `F12` select the drive with arch iso

Select first item

---

## Inside Install Drive

### Set Font for Terminal

Set right font size for the display

```sh
setfont ter-132n
```

### Wi-Fi with iwctl

enter `iwd` mode

```sh
iwctl
```

show machine's network interface

```sh
device list
```

show list of Wi-Fi networks

```sh
station wlan0 get-networks
```

connect to Wi-Fi

```sh
station wlan0 connect "{name of wi-if}"
```

enter password and exit `iwd` mode

```sh
exit
```

check the Wi-Fi with `ping`

```sh
ping google.com
```

Stop pining with `Ctrl + C`

Clear terminal window with `clear` command

---

### Synchronize to databases

update pacman

```sh
pacman -Sy
```

install `archlinux-keyring` and `archinstall` script

```sh
pacman -S archlinux-keyring archinstall
```

To proceed type `Y` or just press `enter`

### Partition

```sh
lsblk
```

more info with `-a`

```sh
lsblk -a
```

`cfdisk` into the drive

could be `nvme0` or `sda` depending on the hardware

```sh
cfdisk /dev/nvme0n1
```

1. use arrow key to select `Free space` then `New`

2. allocate `1G`(1 Gigabyte) and change `Type` to `EFI`

3. allocate every `Free space` left and set to `Linux filesystem`

4. Finally select `Write` type `yes`

### Format partitions

Check created partitions with `lsblk`

`EFI` partition to `fat`

```sh
mkfs.fat -F32 /dev/nvme0n1p5
```

`Root` partition to `ext4`

```sh
mkfs.ext4 /dev/nvme0n1p6
```

### Mount partitions

mount `root` partition to `/mnt`

```sh
mount /dev/nvme0n1p6 /mnt
```

create directory to mount to efi partition to

```sh
mkdir /mnt/boot
```

and mount it

```sh
mount /dev/nvme0n1p5 /mnt/boot
```

`lsblk` to confirm mount

| NAME      | MOUNTPOINTS |
| --------- | ----------- |
| nvme0n1p5 | /mnt/boot   |
| nvme0n1p6 | /mnt        |

### Start Install

execute the `archinstall` script

```sh
archinstall
```

use `arrow keys` or `hjkl` to navigate

- Mirrors
  press `/` to search and type `South Korea` to select the mirror regions

- Disk configuration &rarr; partitioning &rarr; Pre-mounted configuration
  type `/mnt` which is where root partition is mounted to

- Bootloader select `Grub`

- set the root password

- User Account &rarr; Add a user and set it up as superuser then Confirm and exit

- Profile &rarr; Type &rarr; Desktop
  select `Hyprland`

then select Graphics driver

- Audio: `pipewire`

- Network configuration: `Use NetworkManager`

- Additional packages:

```sh
brightnessctl git stow neovim hyprpaper waybar ttf-meslo-nerd otf-font-awesome
```

- Timezon: `Asia/Seoul`

leave other options as is then select `Install`

---

### Grub

Since the install script may have not installed grub properly

```sh
pacman -Sy GRUB efibootmgr dosfstools mtools
```

install GRUB into /boot partition

```sh
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
```

generate and update grub config file

```sh
grub-mkconfig -o /boot/grub/grub.cfg
```

`exit` the chroot environment

and shutdown the system

```sh
shutdown now
```

The ArchLinux is installed

Now you can exit root session shutdown with `shutdown now` and remove the USB drive

---

## Login to Hyprland

From the login window change the sessin from `Hyprland(uwsm-managed)` which is
selected by default to just
`Hyprland`

### Wi-Fi with nmcli

Install `networkmanager`

```sh
sudo pacman -S networkmanager
```

Start and enable to start it every time

```sh
sudo systemctl enable --now NetworkManager
sudo systemctl start --now NetworkManager
```

Check searched wi-fi

```sh
nmcli device wifi list
```

Connect to wi-fi

```sh
nmcli device wifi connect "{wifi list}" password "{password}"
```

check connection

```sh
nmcli connection show
```

### Windows entry to grub menu

noticed that there was no option to boot into Windows in GRUB menu

enter into root mode

```sh
sudo -s
```

```sh
nvim /etc/default/grub
```

`GRUB_TIMEOUT=30`

at the bottom uncomment the `GRUB_DISABLE_OS_PROBER=false`

`:wq` to write changes and quit

```sh
pacman -Sy os-prober
```

update the grub configurations

```sh
grub-mkconfig -o /boot/grub/gurb.cfg
```

you should see `Found Windows Boot Manager on /dev/nvme0n1p1@/efi/Microsoft/Boot/bootmgfw.efi`

```sh
reboot now
```

now you can choose to boot into Windows

## Delete Arch

You can't remove EFI partition from `Disk Management`

to delete the Boot EFI partition open CMD as admin

```sh
diskpart
```

show all the drives connected to PC

```sh
list disk
```

select disk

```sh
select disk 0
```

and list all the partitions

```sh
list partition
```

select and delete partition 5 which is EFI for arch linux

```sh
delete partition override
```

---

### Clean Install USB

First with `diskpart` select the usb drive

remove all partitions

```sh
clean
```

create new partition

```sh
create partition primary
```

format the partition

```sh
format fs=exfat quick
```

give the partition a letter

```sh
assign
```

Exit out of `diskpart`

```sh
exit
```

- Aliases
  - select: `sel`
  - delete: `del`
  - partition: `part`

---

#### Happy Hacking 🎉
