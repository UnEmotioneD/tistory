# Z-Shell

Larger ecosystem and better customizability then BASH

---

## Prerequist

### Install Git

For cloning plugins

```bash
sudo apt install git
git --version
```

---

## ZSH

### Install ZSH

```bash
sudo apt install zsh
```

### Change Shell

```bash
chsh -s $(which zsh)
```

Reboot needed

---

## Plugins

### [Oh My ZSH](https://ohmyz.sh/#install)

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### [Powerlevel10k](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#manual)

```bash
git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
```

### [ZSH-Autosuggestions](https://github.com/zsh-users/zsh-history-substring-search)

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
```

### [ZSH-History-Substring-Search](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)

```bash
 git clone https://github.com/zsh-users/zsh-history-substring-search ~/.oh-my-zsh/custom/plugins/zsh-history-substring-search
```

### [Fast-syntax-highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting?tab=readme-ov-file#installation)

```bash
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting
```

---

## Tools

### [FZF](https://github.com/junegunn/fzf?tab=readme-ov-file#using-git)

Download and install from source instead of using `apt`

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

### [FZF-git](https://github.com/junegunn/fzf-git.sh?tab=readme-ov-file)

Used by `nvim` but sourced from `~/.zshrc`

```bash
git clone https://github.com/junegunn/fzf-git.sh.git
```

Source it from `~/.zshrc`

---

#### Happy Hacking 🎉
