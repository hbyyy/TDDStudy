# TDD Study

- [Test-Driven Development with Python](https://www.obeythetestinggoat.com/book/praise.harry.html) 책의 예제를 진행하면서 정리

## To-Do 
- 책은 Django 1.1 을 사용하기 때문에, 내 환경(Django 3.2) 에서 안되는 부분을 찾아 정리해야 한다.


## 정리

### Selenium 설치

1. 패키지 설치
    - `pip install selenium`
   
2. 웹드라이버
    - 책에서는 Firefox 를 사용하기 때문에, Geckodriver 가 필요하다
        - [geckodriver github](https://github.com/mozilla/geckodriver/tags) 에 접속해 다운로드
        - 압축을 푼 후 `/usr/bin/local` 경로에 파일을 넣는다
        - 터미널에서 `geckodriver --version` 입력 후 다음과 같이 나오면 성공
          ```text
          geckodriver 0.29.1 (970ef713fe58 2021-04-08 23:34 +0200)
          
          The source code of this program is available from
          testing/geckodriver in https://hg.mozilla.org/mozilla-central.
          
          This program is subject to the terms of the Mozilla Public License 2.0.
          You can obtain a copy of the license at https://mozilla.org/MPL/2.0/.
          ```

### git mv

- 프로젝트 내에서 이미 git에 추가되어있는 파일의 이름을 바꾸거나 옮길 때 사용한다

  ```shell
  # mv 커맨드로 옮길 시 아래처럼 파일이 delete 되고 새로 생긴 것으로 추적됨
  
  On branch master
  Changes not staged for commit:
    (use "git add/rm <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)
  
  	deleted:    test.py
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
  
  	test_directory/
  
  
  # git mv 를 이용하면 정상적으로 추적됨
  
  On branch master
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)
  
  	renamed:    test.py -> test_directory/test.py
  
  ```

### LiveServerTestCase

