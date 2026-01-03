# Arch Install

## Install Environment

- Thinkpad T14 Gen4, intel CPU & integrated GPU
- Dual boot with Windows 11

## Referenced YouTube

use `archinstall` script

- [Ksk Royal](https://www.youtube.com/watch?v=4dKzYmhcGEU&list=WL&index=2&t=796s)

## List of contents

- [Before Install](#before-install)
- [Synchronize pacman to DB](#synchronize-package-to-databases)
- [Partitioning](#partitioning)
- [Format Partitions](#format-partitions)
- [Mount Partitions](#mount-the-partitions)
- [start install](#start-install)
  - [trouble-shoot](#trouble-shooting)
- [Grub](#grub)
- [Connect to Wi-Fi](#connect-to-wi-fi)
- [Fix flatpak](#for-kde-plasma)
- [Add Windows to GRUB](#windows-entry-to-grub-menu)
- [Delete ArchLinux](#delete-arch-linux)

---

## Before Install

Use windows `disk mamanger` create at least 40GB of free space

BIOS mode: on thinkpad press enter and f1

```bash
Security > Secure Boot
```

- Secure Boot: off
- Clear All Secure Boot Keys
- Allow Microsoft 3rd Party UEFI CA: off

Save and restart: `F10`

Press enter again then `F12` select the drive with arch iso

Select the very first item

## Inside Terminal

Set right font size for the display

```sh
setfont ter-132n
```

## Connect to Wi-Fi

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

check the Wi-Fi connection with `ping` command

```sh
ping google.com
```

`ctrl + c` to stop ping

clean the terminal with `clear` command

```sh
clear
```

## Synchronize package to databases

update pacman

```sh
pacman -Sy
```

install `archlinux-keyring` and `archinstall` script

```sh
pacman -S archlinux-keyring archinstall
```

To proceed type `Y` or just press `enter`

## Partitioning

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

## Format partitions

check the newly created partitions with `lsblk` command

format the `EFI` first

```sh
mkfs.fat -F32 /dev/nvme0n1p5
```

then format the root partition

```sh
mkfs.ext4 /dev/nvme0n1p6
```

## Mount the partitions

mount the `root` partition to `/mnt`

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

confirm mount with `lsblk`

| NAME      | MOUNTPOINTS |
| --------- | ----------- |
| nvme0n1p5 | /mnt/boot   |
| nvme0n1p6 | /mnt        |

## Start Install

execute the `archinstall` script

```sh
archinstall
```

### Trouble Shooting

`Module Not Found Error` after `archinstall` command: Install missing modules

```sh
pacman -Sy python python-pyparted python-simple-term-menu python-annotated-types python-pydantic python-pydantic-core python-typing_extensions archinstall
```

---

use `arrow keys` or `hjkl` to navigate

- Mirrors
  press `/` to search and type `South Korea` to select the mirror regions

- Disk configuration &rarr; partitioning &rarr; Pre-mounted configuration
  type `/mnt` which is where root partition is mounted to

- Bootloader select `Grub`

- set the root password

- User Account &rarr; Add a user and set it up as superuser(sudo) then Confirm and exit

- Profile &rarr; Type &rarr; Desktop
  select `Hyprland`

then select Graphics driver

- Audio: `pipewire`

- Network configuration: `Use NetworkManager`

- Additional packages: `brightnessctl git stow neovim hyprpaper waybar ttf-meslo-nerd otf-font-awesome`

- Timezon: `Asia/Seoul`

leave other options as is then select `Install`

## Grub

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

now you can remove the USB drive

From the login window change the sessin from `Hyprland(uwsm-managed)` which is
selected by default to just
`Hyprland`

## Connect to Wi-Fi

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

## Windows entry to grub menu

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

### GRUB Menu Resolution

from grub menu press c to go into terminal

```bash
vidieo info
```

from the supported resolutions select one

- lower resolution have lower input delay and bigger texts

back into the grub config file `/etc/default/grub`

- from auto to desired option

```console
GRUB_FGXMODE=640x480
```

recreate the grub config

---

## Delete Arch Linux

boot into windows and open `Disk Management` and remove the `Primary Partition` for Arch Linux first

to delete the Boot EFI partition open CMD as admin

```powershell
diskpart
```

show all the drives connected to PC

```powershell
list disk
```

select disk

```powershell
select disk 0
```

and list all the partitions

```powershell
list partition
```

select and delete partition 5 which is EFI for arch linux

```powershell
delete partiion override
```

Now it is deleted

btw you can use `sel` and `del` as alias
