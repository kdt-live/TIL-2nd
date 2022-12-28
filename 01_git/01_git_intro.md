# Git 기초 흐름

## Git 저장소 만들기

```bash
$ git init
Initialized empty Git repository in C:/Users/hphk/Desktop/목표/.git/
```


## Git으로 

### (1) 작업 완료 후 status

```bash
$ git status
On branch master # 마스터 브랜치

No commits yet # 아직 커밋 없음 (당연히 지금 init 했으니까)

Untracked files: # 1통
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
# 아직 커밋할 것 없음(2통X), 트래킹 되지 않은 파일 있음(1통O)
```

### (2) add

```bash
$ git add .
```

```bash
$ git status
On branch master

No commits yet

Changes to be committed: # 커밋될 변경사항들 (2통)
  (use "git rm --cached <file>..." to unstage)   
        new file:   README.md # 생성
```

### (3) commit

```bash
$ git commit -m '개발자 커리어의 시작'
[master (root-commit) b561c19] 개발자 커리어의 시작
 1 file changed, 7 insertions(+)
 create mode 100644 README.md
```

```bash
$ git status
On branch master
nothing to commit, working tree clean
```

```bash
$ git log
commit b561c19c1b9414aa8c15f2a6e4791bde845fa3ce (HEAD -> master)
Author: KDT live <kdt-live@hphk.kr>
Date:   Wed Dec 28 10:15:07 2022 +0900

    개발자 커리어의 시작

$ git log --oneline
b561c19 (HEAD -> master) 개발자 커리어의 시작
```

