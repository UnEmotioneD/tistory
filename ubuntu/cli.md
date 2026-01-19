# CLI Tools

- Command Line Interface

## List of cli-tools

- git
- curl
- stow
- [tmux](#tmux)
- [bat](#bat)
- [eza](#eza)
- [zoxide](#zoxide)
- [yazi](#yazi)
- [lazygit](#lazygit)
- [delta](#delta)
- [fastfetch](#fastfetch)
- [speedtest-cli](#speedtest-cli)
- pavucontrol
- speedtest-cli

---

APT installable packages

```sh
sudo apt install git curl stow tmux bat eza zoxide git-delta pavucontrol speedtest-cli
```

---

## Bat

File previewer

```sh
sudo apt install bat
```

Inside `.bash_aliases` add alias to avoid collision

```sh
alias bat='batcat'
```

Stow `bat` theme from my `dotfiles` and build cache to make the theme work

```sh
bat cache --build
```

---

## Eza

- [eza - github](https://github.com/eza-community/eza)

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

## Zoxide

- [zoxide - github/installation](https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#installation)

better `cd`

load `zoxide` and override `cd` to use zoxide

- Bash

```sh
eval "$(zoxide init --cmd cd bash)"
```

- ZSH

```sh
eval "$(zoxide init --cmd cd zsh)"
```

---

## Lazygit

- [lazygit github/install ubuntu](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#debian-and-ubuntu)

git wrapped in tui

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

after install remove temp files

```sh
rm ~/lazygit ~/lazygit.tar.gz
```

to install remove lazygit at `/usr/local/bin` and run the install scripts again

```sh
sudo rm /usr/local/bin/lazygit
```

### Config

If you keep config file at `~/.config/lazygit/config.yml` and fill it in with
default config it will freeze when you try to open file inside `lazygit`

Add or edit as follow:

```yml
os:
  edit: "nvim {{filename}}"
```

---

## TMUX

Terminal Multi Plexer

Clone TPM(tmux plugins manager) for use

`~/.tmux/plugins`: where plugins will be installed

```sh
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

---

## Yazi

- [yazi install ubuntu](https://yazi-rs.github.io/docs/installation#debian)

terminal file explorer

### Prerequist

```sh
sudo apt install ffmpeg 7zip jq poppler-utils fd-find ripgrep zoxide imagemagick
```

### Setup Cargo

- [Install Rust](https://rust-lang.org/tools/install/)

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update
```

### Clone and Build

```sh
git clone https://github.com/sxyazi/yazi.git
cd yazi
cargo build --release --locked
```

and move `yazi`, `ya` files to `$PATH`

```sh
sudo mv target/release/yazi target/release/ya /usr/local/bin/
```

### Uninstall Yazi

Remove the `yazi` and `ya` files under the `$PATH`

```sh
sudo rm /usr/local/bin/yazi /usr/local/bin/ya
```

Then remove the cloned repo

---

## Delta

[delta / GitHub](https://github.com/dandavison/delta)

add the following to `~/.gitconfig` customize `delta`

```gitconfig
[core]
  pager = delta
[interactive]
  diffFilter = delta --color-only
[delta]
  # use n / N to move between diff sections
  navigate = true
  side-by-side = true
  line-numbers = true
  syntax-theme = GitHub
[merge]
  conflictstyle = zdiff3
[diff]
  colorMoved = default
```

---

## Fastfetch

System info fetch program

### Install with PPA

```sh
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt upgrade
sudo apt install fastfetch
```

### Uninstall

```sh
sudo apt remove fastfetch
sudo add-apt-repository --remove ppa:zhangsongcui3371/fastfetch
```

---

## Speedtest-cli

```sh
speedtest --secure
```

---

### Happy Hacking 🎉
