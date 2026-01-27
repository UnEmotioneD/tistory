# Zoxide

[zoxide - github/installation](https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#installation)

더 괜찮은 `cd` 명령

---

## 설치

`APT`를 이용해서 설치:

```sh
sudo apt install zoxide
```

설치 확인:

```sh
zoxide --version
```

---

## 준비

다음 코드를 `~/.bashrc`에 추가:

```sh
# --- Zoxide ---
eval "$(zoxide init --cmd cd bash)" # zoxide를 불러오고 기본 cd 대신 사용
```

변경사항을 현재 shell에 적용:

```sh
source ~/.bashrc
```

또는 한방에:

```sh
echo 'eval "$(zoxide init --cmd cd bash)"' >> ~/.bashrc && . ~/.bashrc
```

`echo`: 따옴표 안에 있는 내용을 출력
`>>`: 결과를 특정 파일에 추가
`.`: `source`의 단축어

---

## 사용

[zoxide - getting started](https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#getting-started)

`zoxide`로 한번 이동했던 경로는 다음부터 더 간단하게 입력해도 이동 가능

```sh
cd ~/dev_ws/robot

cd robot   # 최종 경로만 입력
cd rob     # 대충 입력해도 가능
cd dev rob # 다른 비슷한 경로와 구분되게 중간 경로 입력
```
