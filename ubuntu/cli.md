# CLI Tools

- Command Line Interface

## List of cli-tools

- git
- curl
- stow
- tmux
- bat
- eza
- zoxide
- flameshot
- yazi
- lazygit
- fastfetch

---

apt installable packages

```bash
sudo apt install git curl stow tmux bat eza zoxide flameshot
```

---

## Bat

- File previewer

```bash
sudo apt install bat
```

- in `.bashrc` add alias to avoid collision

```bash
alias bat='batcat'
```

stow bat theme from my dotfiles and build cache to make the theme work

```bash
bat cache --build
```

---

## Lazygit

- Git in TUI

- [lazygit/installation/Debian and Ubuntu](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#debian-and-ubuntu)

download with `curl`

and install

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

---

## TMUX

- Terminal Multi Plexer

clone TPM(tmux plugins manager)

`~/.tmux/plugins`: where plugins will be installed

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

---

## Yazi

- Terminal File Explorer

- [Installation/Yazi](https://yazi-rs.github.io/docs/installation/)

Build from source

create local branch and remove commits to use the stable version

prerequist

```bash
sudo apt install ffmpeg 7zip jq poppler-utils fd-find ripgrep zoxide imagemagick
```

Setup cargo

- [Install Rust](https://rust-lang.org/tools/install/)

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update
```

Clone it to your disered directory from git and build it

```bash
git clone https://github.com/sxyazi/yazi.git
cd yazi
cargo build --release --locked
```

and move `yazi`, `ya` files to `$PATH`

```bash
sudo mv target/release/yazi target/release/ya /usr/local/bin/
```

- Uninstall

remove the `yazi` and `ya` files under the `$PATH`

```bash
sudo rm /usr/local/bin/yazi /us/local/bin/ya
```

---

## Fastfetch

Install with `PPA`

```bash
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt upgrade
sudo apt install fastfetch
```

Uninstall

```bash
sudo apt remove fastfetch
sudo add-apt-repository --remove ppa:zhangsongcui3371/fastfetch
```

## GitHub CLI

[github cli for ubuntu](https://github.com/cli/cli/blob/trunk/docs/install_linux.md#debian)

install

```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

update

```bash
sudo apt upgrade
sudo apt install gh
```

run the following to use `gh` command

```bash
gh auth login
```

### Markdown Preview

- [yusukebe/gh-markdown-preview](https://github.com/yusukebe/gh-markdown-preview)

- For `.md` file preview style to be exactly like from `github`
- No scroll sync though ...

Install

```bash
gh extension install yusukebe/gh-markdown-preview
```

Update

```bash
gh extension upgrade markdown-preview
```

How to use

```bash
gh markdown-preview README.md
```

Auto detects `README.md` file

```bash
gh markdown-preview
```

Useful flags

```bash
--dark-mode         # Force dark mode
--markdown-mode     # Force "markdown" mode (rather than default "gfm")
--disable-auto-open # Disable auto opening your browser
--disable-reload    # Disable live reloading
--verbose           # Show verbose output
```

- Tip: use separate tmux window to run the command
