---
id: archinstall
aliases: []
tags: []
---

# Arch 리눅스 설치

## 설치 환경

- Thinkpad T14 Gen4, 인텔 CPU & 내장 GPU
- Windows 11

## 참고한 유튜브

### archinstall 스크립트 사용

- [Ksk Royal](https://www.youtube.com/watch?v=4dKzYmhcGEU&list=WL&index=2&t=796s)

## Table of contents

- [After booting into Arch](#설치전-작업)
- [Synchronize pacman to DB](#synchronize-package-to-databases)
- [Partitioning](#partitioning)
- [Format Partitions](#format-partitions)
- [Mount Partitions](#mount-the-partitions)
- [archinstall](#설치-시작)
- [Connect to Wi-Fi nmcli](#connect-to-wi-fi-nmcli)
- [Fix flatpak](#for-kde-plasma)
- [Add Windows to GRUB](#windows-entry-to-grub-menu)
- [Delete ArchLinux](#delete-arch-linux)

## 설치전 작업

윈도우 디스크관리자에서 최소 40GB의 공간 만들기

Thinkpad: Enter 그리고 F1을 눌러서 BIOS Setup으로 진입

Security &rarr; Secure Boot 로 이동해서

- Secure Boot: off
- Clear All Secure Boot Keys
- Allow Microsoft 3rd Party UEFI CA: off

F10 눌러서 저장하고 나가기

다시 Enter 그리고 F12 로 리눅스 설치 USB 선택

가장 첫번째 선택

## 터미널에 들어와서

기기 해상도에 맞게 글자 크기 변경

```sh
setfont ter-132n
```

## iwctl 사용해서 wi-fi 연결

iwd 모드 진입

```sh
iwctl
```

기기에 있는 network 인터페이스 조회

```sh
device list
```

show the list of Wi-Fi networks

```sh
station wlan0 get-networks
```

connect to Wi-Fi

```sh
station wlan0 connect "{name of wi-if}"
```

then enter password

exit iwd mode

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

pacman을 업데이트하고

```sh
pacman -Sy
```

archlinux-keyring과 archinstall를 설치

```sh
pacman -S archlinux-keyring
```

```sh
pacman -S archinstall
```

To proceed type `Y` or just press `enter`

## Partitioning

```sh
lsblk
```

```sh
lsblk -a
```

를 이용해서 더 정확하게 볼 수 있다

```sh
cfdisk /dev/nvme0n1
```

또는 `nvme0` 가 아니라 `sda` 라고 뜰 수 도 있다

화살표를 이용해서 `Free space` 로 이동한다음 `New` 선택

`1G` 를 할당한다음에 `Type`를 `EFI`로 바꿈

나머지 `Free space`에 공간을전부 할당하고 `Liux filesystem`로 지정

그리고 `Write`를 선택하고 `yes`를 치고서 나온다

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

`lsblk`를 이용해서 장착 됬는지 확인한다

| NAME      | MOUNTPOINTS |
| --------- | ----------- |
| nvme0n1p5 | /mnt/boot   |
| nvme0n1p6 | /mnt        |

## 설치 시작

이제 모든 준비가 끝났고 설치 스크립트를 사용할 수 있음

```sh
archinstall
```

### Trouble Shooting

- Module Not Found Error가 뜬다면

```sh
pacman -Sy python python-pyparted python-simple-term-menu python-annotated-types python-pydantic python-pydantic-core python-typing_extensions archinstall
```

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

- Additional packages: `brightnessctl`
  - hyprland.conf에 키가 설정되어 있지만 패캐지가 없기때문에

  `git stow neovim hyprpaper waybar ttf-meslo-nerd otf-font-awesome`

- Timezon: `Asia/Seoul`

leave other options as is then select `Install`

## grub 설치

설치 스크립트가 grub를 제대로 설치 하지 못할 수도 있어서

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

비밀번호 입력화면에서 session 을 Hyprland(uwsm-managed) 에서 그냥 Hyprland 로
바꾸고 로그인한다

## Connect to Wi-Fi nmcli

설치되어 있지 않으면 `pacman`으로 설치

```sh
sudo pacman -S networkmanager
```

```sh
sudo systemctl enable --now NetworkManager
```

```sh
sudo systemctl start --now NetworkManager
```

```sh
nmcli device wifi list
```

```sh
nmcli device wifi connect "{wifi list}" password "{password}"
```

check connection

```sh
nmcli connection show
```

## For KDE Plasma

open console

fix the Discover program's backend

```sh
sudo pacman -Sy flatpak
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
