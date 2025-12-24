# NeoVim

## Packages

- nerd fonts
- nodejs
- npm
- yarn

```bash
sudo apt install nodejs npm yarn
```

---

## Build From Source

- Prerequist packages

```bash
sudo apt-get install ninja-build gettext cmake unzip curl
```

- Clone nvim repo

```bash
git clone https://github.com/neovim/neovim
```

```bash
cd neovim
```

- Checkout stable branch for stable version

```bash
make CMAKE_BUILD_TYPE=RelWithDebInfo
```

```bash
sudo make install
```

- Gets installed to `/usr/local`

---

## Copy & Paste

- yank

```vim
"+y
```

- paste

```vim
"+p
```
