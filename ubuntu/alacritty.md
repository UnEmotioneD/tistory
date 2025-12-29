# Alacritty

- Build from source to use the latest version

## Prerequisites

the git repo

```bash
git clone https://github.com/alacritty/alacritty.git
cd alacritty
```

- `rustup`

`Rust` programming language installer

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

stable version of rust.rs

```bash
rustup overrride set stable
rustup update stable
```

required packages for `ubuntu`

```bash
sudo apt install cmake g++ pkg-config libfontconfig1-dev libxcb-xfixes0-dev libxkbcommon-dev python3
```

## Building

inside the cloned `alacritty` directory

```bash
cargo build --release
```
