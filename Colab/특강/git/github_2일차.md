### 절대 

- ~에서 'git init' 진행
- 리포 안에 리포 만들기
- $ git init 입력 전 확인할 점
  1. ~ 인지 확인
  2. 폴더명 옆 (master)가 있는지 확인

### 프로젝트 초기화 진행

- 폴더를 리포로 

  $ git init

- README 파일 & .gitignire 파일 생성 

  - 빈폴더에서는 add 가 안 돼서 파일을 하나 만들어야 함 (?) -> README.md 생성

  - 빈폴더는 관리대상이 아님. 그냥 빈 폴더라서

- *** gitignore.io 에 접속하여 필요한 내용 복붙 ***

  - *** 반드시 초기작업 단계에서 진행할 것 ***

- README 파일 add(tracking) - 얼굴도장(스테이지에 올리기)

  $ git add README.md

- 계정용 서명 등록

  $ git config --global user.name  쓰고 싶은 닉네임

  $ git config --global user.email 이메일

- 서명이 정상적으로 등록되었는지 확인

  $ cat ~/.gitconfig

- commit

  - 파일들이 초록색으로 뜬다면 커밋이 된다는 뜻?

  $ git commit -m 'MESSAGE'

- 원격 저장소 생성 @ github.com

- 생성한 원격 저장소 등록

  $ git remote add origin <URL>

- 지금까지의 commit push

  $git push origin master

### 명령어 정리

- 초기화 시점에 1회 입력

  $ git init

- 작업중

  $ git add<Filename>

  $ git commit - m 'MESSAGE'

- 모니터링

  $ git status

  $ git log

- github에 원격 저장소 생성하기

- 원격저장소(Remote repo) 추가하기(등록하기)

  $ git remote add origin <URL>

  - 디셔너리 구조. origin이 키값, URL에 대응값
  - Ex). git remote add A <URL> -> A라는 이름으로 URL 저장

  - 여러개 등록 가능. 여러개의 백업저장소

- 원격저장소 확인하기 (위의 remote add 로 추가한)

  - git remote -v

- 원격저장소에서 삭제 하기

  $ git remote remove <name>

  $ git remote remove  A (1개씩만 입력)

  - -> 로컬에서 삭제하고 push로 반영

- 원격 저장소에 지금까지의 commit PUSH하기

  $ git push origin master

  - origin에 등록된 곳으로 가겠다?



#### 기타

-  리포가 관리하는 것은 폴더 안의 내용들.
  - 리포 폴더의 이름을 변경하거나 폴더를 이동시키는 것은 관리 밖의 일 -> 변경으로 보지 않음

- 마스터 머징
  - 