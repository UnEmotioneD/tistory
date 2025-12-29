# CLI Tools

- Command Line Interface

## List of cli-tools

- bat
- curl
- eza
- flameshot
- git
- stow
- tmux
- zoxide

- yazi
- lazygit
- fastfetch

---

apt installable packages

```bash
sudo apt install bat curl eza flameshot git stow tmux zoxide
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

---

## Lazygit

- Terminal User Interface git application

install curl frist

```bash
sudo apt install curl
```

download and install

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

check installed

```bash
lazygit --version
```

---

## Tmux Plugin Manager

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

---

## Yazi

Build from source

- create local branch and remove commits to use the stable version

prerequist

```bash
sudo apt install ffmpeg 7zip jq poppler-utils fd-find ripgrep zoxide imagemagick
```

Setup cargo

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

now you can run `fastfetch` from terminal

```bash
fastfetch
```

Uninstall

```bash
sudo apt remove fastfetch
sudo add-apt-repository --remove ppa:zhangsongcui3371/fastfetch
```
