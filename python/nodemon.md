# Nodemon

- Watch files for change and execute a command

## Installation

Install with npm

```bash
sudo npm i -g nodemon
```

## Configuration

Create `nodemon.json` at where you will run `nodemon` command

- `watch`: Files or directories to monitor
- `ext`: File extensions to watch
- `ignore`: Path to exclude
- `exec`: Command to run on changes
- `start`: Command to run on start before `exec`

```json
{
  "watch": ["*.py"],
  "ext": "py",
  "ignore": [],
  "exec": "python3 ./binary_tree.py",
  "events": {
    "start": "clear"
  }
}
```

## Use

just run:

```bash
nodemon
```

---

### Happy Hacking 🎉
