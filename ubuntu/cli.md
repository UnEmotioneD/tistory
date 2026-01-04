# CLI Tools

- Command Line Interface

## List of cli-tools

- git
- curl
- stow
- [tmux](#tmux)
- [bat](#bat)
- [eza](#eze)
- [zoxide](#zoxide)
- [yazi](#yazi)
- [lazygit](#lazygit)
- [fastfetch](#fastfetch)
- [speedtest-cli](#speedtest-cli)

---

APT installable packages

```bash
sudo apt install git curl stow tmux bat eza zoxide
```

---

## Bat

File previewer

```bash
sudo apt install bat
```

Inside `.bash_aliases` add alias to avoid collision

```bash
alias bat='batcat'
```

Stow `bat` theme from my `dotfiles` and build cache to make the theme work

```bash
bat cache --build
```

---

## [Eza](https://github.com/eza-community/eza)

`ls` command replcement

add the following alias to `.bashrc` or `.zshrc`

- list in vertical line
- color and icons
- directory first
- show git status

```sh
alias ls="eza --oneline --color=always --icons=always --group-directories-first --git"
```

---

## [Zoxide](https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#installation)

better `cd`

- Bash

```sh
eval "$(zoxide init bash)"
```

- ZSH

```sh
eval "$(zoxide init zsh)"
```

---

## [Lazygit](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#debian-and-ubuntu)

git wrapped in tui

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

---

## TMUX

Terminal Multi Plexer

Clone TPM(tmux plugins manager) for use

`~/.tmux/plugins`: where plugins will be installed

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

---

## [Yazi](https://yazi-rs.github.io/docs/installation#debian)

terminal file explorer

### Prerequist

```bash
sudo apt install ffmpeg 7zip jq poppler-utils fd-find ripgrep zoxide imagemagick
```

### Setup Cargo

- [Install Rust](https://rust-lang.org/tools/install/)

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update
```

### Clone and Build

```bash
git clone https://github.com/sxyazi/yazi.git
cd yazi
cargo build --release --locked
```

and move `yazi`, `ya` files to `$PATH`

```bash
sudo mv target/release/yazi target/release/ya /usr/local/bin/
```

### Uninstall Yazi

Remove the `yazi` and `ya` files under the `$PATH`

```bash
sudo rm /usr/local/bin/yazi /us/local/bin/ya
```

Then remove the cloned repo

---

## Fastfetch

### Install with PPA

```bash
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt upgrade
sudo apt install fastfetch
```

### Uninstall

```bash
sudo apt remove fastfetch
sudo add-apt-repository --remove ppa:zhangsongcui3371/fastfetch
```

---

## Speedtest-cli

```bash
sudo apt install speedtest-cli
speedtest --secure
```

---

### Happy Hacking 🎉
