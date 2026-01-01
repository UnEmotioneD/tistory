# Neovim

## Packages

- nerd fonts
- ripgrep
- nodejs
- npm
- yarn
  - markdown-preview
- python3-full
  - clang-format
  - pylint
  - isort
  - black
- openjdk-17-jdk
  - nvim-java

```bash
sudo apt install ripgrep nodejs npm python3-full openjdk-17-jdk
```

For the markdown-preview install `yarn` with `npm`

```bash
sudo npm i -g yarn
```

---

## Build From Source

If neovim is already installed with apt, remove before building it.

Prerequist packages

```bash
sudo apt-get install ninja-build gettext cmake curl build-essential git
```

Clone nvim repo

```bash
git clone https://github.com/neovim/neovim
cd neovim
```

Checkout stable branch for stable version

```bash
git checkout stable
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install
```

Gets installed to `/usr/local`

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

Copy paste with no configs

- Yank
- Paste

```vim
"+y

"+p
```

---

### Happy Hacking 🎉
