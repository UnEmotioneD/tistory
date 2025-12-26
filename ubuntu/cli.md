# CLI Tools

- Command Line Interface

## List of cli-tools

- git
- curl
- zoxide
- eza
- fzf
- bat
- tmux
- yazi
- stow
- lazygit
- flameshot: screen shot program
- fastfetch

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

## Tmux Plugin Manager

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

---

## Yazi

Must build from source

Prerequit

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

and add `yazi`, `ya` to `$PATH`

```bash
mv target/release/yazi target/release/ya /usr/local/bin/
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
