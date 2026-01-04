# JAVA

How to change java version when you have multiple JDKs installed

---

## Package Name

### Arch / Pacman

```sh
jdk17-openjdk
jdk21-openjdk
```

### Ubuntu / APT

```sh
openjdk-17-jdk
openjdk-21-jdk
```

---

## 1. Check Installed JDKs

### Arch Only

```sh
archlinux-java status
```

---

## 2. Change JDK Version

### For Arch

```sh
sudo archlinux-java set java-17-openjdk
```

### For Ubuntu

```sh
sudo update-alternatives --config java
```

```sh
sudo update-alternatives --config javac
```

---

## 3. Confirm Changes

```sh
java --version
```

---

### Happy Hacking 🎉
