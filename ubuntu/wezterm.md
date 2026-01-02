# Wezterm

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
