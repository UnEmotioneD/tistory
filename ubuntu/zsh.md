# Z-Shell

- Larger ecosystem compare to BASH

## Prerequisite

- install `git` and check

```bash
sudo apt install git
git --version
```

## ZSH

```bash
sudo apt install zsh
```

```bash
chsh -s $(which zsh)
```

Reboot your machine

## Plugins

- oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

- powerlevel10k

```bash
git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
```

- autosuggestion

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
```

- history-substring-search

```bash
 git clone https://github.com/zsh-users/zsh-history-substring-search ~/.oh-my-zsh/custom/plugins/zsh-history-substring-search
```

- fast-syntax-highlighting

```bash
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting
```

- FZF

Download and install from source instead of using `apt`

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

- fzf-git

Used by `nvim` but sourced from `~/.zshrc`

```bash
git clone https://github.com/junegunn/fzf-git.sh.git
```

- source it from `~/.zshrc`
