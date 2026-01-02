# Wezterm

- configuration with `Lua`
- supports image rendering in `yazi`

How to install wezterm on Debian/Ubuntu Linux and configure

---

## Install

- [Wezterm Install](https://wezterm.org/install/linux.html)

```bash
curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg

echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list

sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
```

```bash
sudo apt update
```

Install `wezterm` or `wezterm-nightly`

```bash
sudo apt install wezterm
```

---

## Configuration

Reference: [`Josean - Wezterm`](https://www.josean.com/posts/how-to-setup-wezterm-terminal)

---

## Permission

what is `chmod` with numbers

```bash
sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
```

| Permission | Value |
| ---------- | ----- |
| read       | 4     |
| write      | 2     |
| execute    | 1     |

| Digit | Applise to |
| ----- | ---------- |
| 1st   | Owner      |
| 2dn   | Group      |
| 3rd   | Others     |

0: no permission at all

---

6 = 4(read) + 2(write) = owner can read and write
4 = group can read
4 = others can read

Do `ls -l` it will look like this:

```bash
-rw-r--r--
```

744 is also common

```bash
-rwx-rw-rw-
```

---

### Happy Hacking 🎉
