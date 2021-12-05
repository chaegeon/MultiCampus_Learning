# 2021-12-02

## Git 01

### Git Bash

- 설치
  - https://git-scm.com/download/win

- 명령어

  - 폴더

    - cd : 홈폴더로 이동
    - cd a : a라는 하위 폴더로 이동  
    - cd .. : 상위 폴더로 이동
    - ls : 폴더의 파일 목록들을 보여줌
    - ls -a : 숨김 파일까지 포함하여 전부 보여줌
    - mkdir AA : AA라는 폴더 생성 
    - rm -r AA : AA라는 폴더 삭제 
    - 

  - 파일

    - 생성

      - touch aaa.txt : aaa.txt파일 생성
      - touch .hidden.txt : 파일명 앞에 .을 붙이면 숨김파일로 생성

    - 삭제 (영구삭제)

      - rm aaa.txt : aaa.txt파일 삭제
      - rm *.txt : txt형식의 파일을 전부 삭제
      - rm .hidden.txt : 숨겨진 hidden.txt파일 삭제

    - 이동

      - mv aaa.txt AA : aaa.txt파일을 AA폴더로 이동

        

      **mv A B 에서 A는 파일명, B는 존재하는 폴더의 이름인 경우 이동, 존재하지 않는 폴더의 이름인 경우 파일의 이름변경**

      

    - 이름변경

      - mv aaa.txt bbb : aaa.txt파일을 bbb로 이름변경

    - 실행

      - start test.md : test.md 파일 실행
      - star . : 내 위치 실행

  - 기타

    - Tap : 이름 자동완성 ex) aa Tap => aa로 시작하는 파일이 있을 경우 자동으로 파일명이 완성됨
    - code . : 현재 폴더를 vscode로 실행




### Git

​	특정 파일을 관리하는 것이 아닌, **폴더**를 관리하는 도구

- 새로운 컴퓨터에서 기존 원격 저장소 복제하기
- ``` sh
- $ git clon<URL>
- ```

원격 저장소의 내용 받아오기
```sh
$ git pull origin master
```
