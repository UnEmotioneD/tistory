# Ranger

Vim 모션을 사용하는 터미널 파일 탐색기

## Install

```sh
sudo apt install ranger
```

---

## Config

`~/.config/ranger/rc.conf` 경로와 설정파일 생성

```sh
ranger --copy-config=rc
```

### Config File

상위, 현재, 하위 경로의 비율 설정

```sh
set column_ratios 1,3,4
```

`.config` 또는 `.bashrc` 처럼 숨겨져 있는 아이템들도 표시

```sh
set show_hidden true
```

---

## Vim Motion

- `j`: 아래로 이동
- `k`: 위로 이동
- `h`: 상위 경로로 이동
- `l`: 하위 경로로 이동

- `gg`: 최상단으로 이동
- `G`: 최하단으로 이동

- `v`: 선택
- `yy`: 아이템 복사
- `dd`: 아이템 삭제 또는 잘라내기
- `p`: 복사, 잘라내기 한 아이템 붙여 넣기

- `/`: 현재 경로에서 검색
  - `n`: 다음 검색 결과
  - `N`: 이전 검색 결과

---

## Application

다음 함수를 `~/.bashrc`에 추가:

- Alias `r`을 생성
- `q`를 누르면 `ranger`를 종료하면서 경로로 이동할 수 있다

```sh
# --- Ranger ---
function r() {
  local tmp="$(mktemp -t ranger-cwd.XXXXXX)" cwd
  command ranger --choosedir="$tmp" "$@"
  cwd="$(cat -- "$tmp")"
  [ -n "$cwd" ] && [ "$cwd" != "$PWD" ] && builtin cd -- "$cwd"
  rm -f -- "$tmp"
}
```

---

### Happy Hacking 🎉
