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

create new branch

```bash
git branch {new-branch-name}
```

checkout the branch

```bash
git checkout {branch-name}
```

show workingtree differences

```bash
git diff
```

merge branch into current branch without creating new commit

`--ff-only`: fast-forward-only

```bash
git merge --ff-only {branch-name}
```

pull and push

`-u`: upstream

```bash
git pull
git push -u origin main
```

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
