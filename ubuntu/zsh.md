# Z-Shell

- Larger ecosystem compare to BASH

## Install ZSH

```bash
sudo apt install zsh
```

---

## Change Shell

```bash
chsh -s $(which zsh)
```

- reboot

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

- fzf

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

- fzf-git

```bash
mkdir ~/repo
cd ~/repo
git clone https://github.com/junegunn/fzf-git.sh.git
```

- source it from `~/.zshrc`
