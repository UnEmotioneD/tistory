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
sudo apt-get install ninja-build gettext cmake curl build-essential git
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
git checkout stable
```

```bash
make CMAKE_BUILD_TYPE=RelWithDebInfo
```

```bash
sudo make install
```

- Gets installed to `/usr/local`

---

## Update Neovim Built From Source

```bash
cd neovim
git pull
make distclean  # recommended after major updates
make CMAKE_BUILD_TYPE=Release
sudo make install
```

## Copy & Paste

- yank

```vim
"+y
```

- paste

```vim
"+p
```
