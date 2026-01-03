# 윈도우 시간

- 리눅스를 듀얼 부트 하면 리눅스를 실행했다가 윈도우로 돌아가면 시간이 맞지 않게 되는 문제 해결

- [Fix time on dual boot - TroubleChute](https://www.youtube.com/watch?v=xO0lPxrtFCw)

- Change Windows From using local time to use UTC like in linux

## 자동 시간 설정 끄기

- 설정 > 시간 및 언어 > 날짜 및 시간 > 자동으로 시간 설정 ==> 끔

## 레지스트리 편집기

단축키 `Ctrl + R`로 실행 창을 띄우고 `regedit`을 입력 해서 편집기 창을 띄움

그리고 경로창에 다음 경로를 입력

```txt
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation
```

이 경로 안에서 우클릭 > 새로만들기 > `dword32비트` 선택 그리고 `RealTimeIsUniversal`이라고 이름 지정

편집하기 위해 엔터 한번 더 누른후 값을 `1`로 변경

---

### Happy Hacking 🎉
