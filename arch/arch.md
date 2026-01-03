# Arch Linux Install

> **Scope**: Intel CPU & iGPU, UEFI system, Hyprland desktop, GRUB bootloader
> **Method**: `archinstall` (guided install)

---

## 0. Overview

- Hardware: ThinkPad T14 Gen4 (Intel)
- OS layout: Windows 11 + Arch Linux (dual boot)
- Desktop: Hyprland (Wayland)
- Audio: PipeWire
- Network: NetworkManager

**Reference**: Ksk Royal – ArchInstall walkthrough (YouTube)

---

## 1. Pre‑Installation (Windows & BIOS)

### 1.1 Shrink Disk (Windows)

- Open **Disk Management**
- Shrink an existing Windows partition
- Leave **≥ 40 GB unallocated space**

### 1.2 BIOS / UEFI Settings (ThinkPad)

- Enter BIOS: `Enter` → `F1`
- Navigate to:

```sh
Security > Secure Boot
```

- Set:
  - Secure Boot: **Disabled**
  - Clear Secure Boot Keys
  - Allow Microsoft 3rd Party UEFI CA: **Off**

Save & Exit: `F10`

### 1.3 Boot Arch ISO

- Power on `F12`
- Select USB with Arch ISO
- Choose first boot option

---

## 2. Live Environment Setup

### 2.1 Improve TTY Font

```sh
setfont ter-132n
```

### 2.2 Connect to Wi‑Fi (iwd)

```sh
iwctl
```

```sh
device list
station wlan0 get-networks
station wlan0 connect "<SSID>"
exit
```

Verify:

```sh
ping google.com
```

---

## 3. Prepare Installer

### 3.1 Sync Package Databases

```sh
pacman -Sy
```

### 3.2 Install Required Packages

```sh
pacman -S archlinux-keyring archinstall
```

---

## 4. Disk Partitioning (Manual)

### 4.1 Identify Disk

```sh
lsblk
```

### 4.2 Partition with cfdisk

```sh
cfdisk /dev/nvme0n1
```

Create:

| Size | Type             | Purpose |
| ---- | ---------------- | ------- |
| 1 GB | EFI System       | `/boot` |
| Rest | Linux filesystem | `/`     |

Write changes and exit.

---

## 5. Format & Mount

### 5.1 Format Partitions

```sh
mkfs.fat -F32 /dev/nvme0n1pX   # EFI
mkfs.ext4 /dev/nvme0n1pY      # Root
```

### 5.2 Mount

```sh
mount /dev/nvme0n1pY /mnt
mkdir /mnt/boot
mount /dev/nvme0n1pX /mnt/boot
```

Verify:

```sh
lsblk
```

---

## 6. ArchInstall (Guided)

```sh
archinstall
```

### 6.1 Common Options

- Mirrors → South Korea
- Disk Configuration → **Pre-mounted** (`/mnt`)
- Bootloader → **GRUB**
- Profile → Desktop → **Hyprland**
- Audio → PipeWire
- Network → NetworkManager
- Timezone → Asia/Seoul

### 6.2 Additional Packages

```sh
brightnessctl git stow neovim hyprpaper waybar ttf-meslo-nerd otf-font-awesome
```

### 6.3 Troubleshooting: Missing Python Modules

```sh
pacman -Sy python python-pyparted python-simple-term-menu \
python-annotated-types python-pydantic python-pydantic-core \
python-typing_extensions archinstall
```

---

## 7. GRUB Fix (If Needed)

```sh
pacman -Sy grub efibootmgr dosfstools mtools
```

```sh
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

Exit chroot and reboot.

---

## 8. Post‑Install Networking

```sh
sudo pacman -S networkmanager
sudo systemctl enable --now NetworkManager
```

```sh
nmcli device wifi list
nmcli device wifi connect "<SSID>" password "<password>"
```

---

## 9. Add Windows to GRUB

```sh
sudo pacman -S os-prober
sudo nvim /etc/default/grub
```

Enable:

```sh
GRUB_DISABLE_OS_PROBER=false
```

Regenerate config:

```sh
grub-mkconfig -o /boot/grub/grub.cfg
```

---

## 10. GRUB Resolution (Optional)

At GRUB menu:

```sh
c
video info
```

Set resolution:

```sh
GRUB_GFXMODE=640x480
```

Rebuild GRUB config.

---

## 11. Remove Arch Linux (Rollback)

### 11.1 Delete Linux Partition (Windows)

- Open **Disk Management**
- Delete Arch Linux primary partition

### 11.2 Remove EFI Entry

```powershell
diskpart
list disk
select disk 0
list partition
select partition <EFI_ID>
delete partition override
```

---

#### Happy Hacking 🎉
