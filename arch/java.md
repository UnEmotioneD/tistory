# JAVA

- How to change java version

---

if you have multiple versions of jdk installed

```bash
sudo pacman -S jdk17-openjdk

sudo pacman -S jdk21-openjdk
```

check which versions are installed

```bash
archlinux-java status
```

change it with `archlinux-java` command

```bash
sudo archlinux-java set java-17-openjdk
```

confirm changes

```bash
java --version
```
