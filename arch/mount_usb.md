# How to Mount External Drives

Mount and unmount external drives from terminal

- [Find External Drive](#find-external-drive)
- [Create Mount Directory](#create-mount-directory)
- [Mount](#mount)
- [Unmount](#unmount)

---

## Find External Drive

Use `lsblk` to list block devices:

```sh
lsblk
```

Example output:

```text
sdb      # entire disk
└─sdb1   # partition on the external drive
```

> **Note:** Device names like `sdb` / `sdb1` are examples.
> Always confirm the correct device on your system.

---

## Create Mount Directory

Create a directory where the drive will be mounted:

```sh
sudo mkdir -p /mnt/usb
```

---

## Mount

Mount the partition (most common case):

```sh
sudo mount /dev/sdb1 /mnt/usb
```

If the drive has no partitions, you may need to mount the disk itself:

```sh
sudo mount /dev/sdb /mnt/usb
```

---

## Unmount

You can unmount by mount point:

```sh
sudo umount /mnt/usb
```

Or by device name:

```sh
sudo umount /dev/sdb1
```

---

### Happy hacking 🎉
