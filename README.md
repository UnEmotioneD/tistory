# Machine-Setup

- Markdown files about how to setup my machines

- macOS
- Arch Linux, Hyprland
- Ubuntu, i3wm

---

- [ ] Create complete setup scripts
- [ ] Upload on [Tistory](https://unemotioned.tistory.com/)

---

## Git

### Reset Commit History

orphan branch which has no history but have all the files

```bash
git checkout --orphan temp_branch
```

add all

```bash
git add -A
```

create commit

```bash
git commit -m "first commit"
```

delete old main branch

```bash
git branch -D main
```

rename current branch to main

```bash
git branch -m main
```

force push to github

```bash
git push -f origin main
```
