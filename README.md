# SBS_Python
### 파이썬 보충 사이트 : to2.kr/cUq
프로그래밍 4대요소 => 값, 변수, 조건문, 반복문

추가요소 => 리스트, 클래스. 함수

**파이썬 기초 문법**
- 파이썬의 경우 C나 JAVA와 다르게 ;(세미콜론을 붙이지 않는다)
- 주석은 #을 사용한다.
- 출력 기본 포맷은 다음과 같다.
   - print("{}-{}-{}".format(2021,7,15))

**함수**
- 함수를 사용하려면 정의(선언), 호출(사용), 매개변수와 인수, 리턴값이 필요하다.
- 함수를 사용하면 중복을 최소화 할 수 있다.
- 함수선언의 기본 포맷은 다음과 같다.
- 함수를 값으로 사용하려면 리턴값을 정의. 그렇지 않을 땐 정의 X
- 리턴을 사용하는 이유는 함수 하나로 프로그램이 종료되지 않기 때문에 한 함수의 결과값을 받아서 후속 작업을 해야하기 때문에
    ```
    def test() :
     print("안녕하세요")
     print("안녕하세요")
    ```
- 함수 호출
    ```
    test()
    ```
- 내장함수에는 *int(),input(),print()* 등이 있다.
- 매개변수를 이용한 함수를 만들 수도 있다. (재활용기능 업시키기 위해)
* 매개변수를 이용한 구구단 예시
    ```
    def gugudan(dan) :
      i = 1
      while i <= 9:
        print("{}*{}={}".format(dan,i,dan*i))
        i+=1
    gugudan(2)
    ```
* 함수를 사용하는 이유
  1. 코드의 재활용
  2. 코드의 구조화
  3. 코드의 집중화
---

**리스트**
  
  - 다수의 데이터를 효율적으로 저장하고 관리, 추가, 조회, 수정, 삭제
  ```
  # 이런식으로 변수로 만들면 수열 만들 수 없음.
  # 반복문 사용 불가
  stu = 10
  stu1 = 20
  stu2 = 30

  # 리스트 사용 => 반복문 가능, 데이터 일괄적으로 사용 가능
  stus = [10, 20, 30]
  stus[1]
  ```
  리스트 사용법 - 객체의 일종. 객체 -> 객체만 사용할 수 있는 함수 => 메서드
 ```
 # 추가 => append(값)
 print(stus)
 stus.append(10) # append 무조건 한번에 하나만 가능, 리스트 맨뒤에 추가됨
 
 # 원하는 위치에 추가 => insert(위치, 값)
 stus.insert(0, 25)

 # 리스트 합치기 => exptend()
 list1={1,2,3}
 list2={4,5,6}
 list1.extend(list2)

 # 수정 - 수정을 원하는 인덱스 선택 후 대입으로 수정
 list1[2]=100
 print(list2)

 # 조회 - 조회를 원하는 인덱스로 선택 후 사용
 print(lists[2])

 # 삭제 원하는 위치 삭제 - 삭제를 원하는 인덱스로 선택후 del 키워드로 삭제
 del list[2]
 print(list)

 # 마지막 삭제
 list.pop()
 print(list)

 # 원하는 값으로 삭제
 list.remove(4)
 print(list2)

 # 전체 삭제
 list2.clear()
 print(list2)
 ```
 - 리스트의 길이 정보는 매우 중요!!
 - 리스트의 길이 구하는 내장함수 **length = len(리스트이름)**
 - 처음부터 끝까지 리스트를 사용하는 경우 굳이 인덱스 만들 필요없음.
---
**for문**
- 리스트의 처음부터 끝까지 탐색가능 for aa in list
- 수열을 만들어주는 함수 -> range()

      range(시작, 끝 - 1, 증가량) 
- 무한반복 할 땐 while문이 더 좋음.   
---
**구조화**
- 리스트는 데이터의 순서는 있지만 데이터의 이름이 없다.
- 데이터를 index가 아닌 이름으로 관리 -> 딕셔너리
- 딕셔너리는 {}로 묶는다
  ```
  # 딕셔너리 방법
  # 리스트는 순서(인덱스, index), 딕셔너리 이름(키, key)
  hong = {"이름" : "홍길동", "나이" : 20, "전화번호" : "01011112222","주소" : "대전"}
  print(hong["이름"])
  print(hong["나이"])

  # 리스트 방법
  hong = ["홍길동", 20, "01011112222", "대전"]
  print(hong[0])

  => 리스트의 경우 순서에 따라 달라지므로 값을 찾기 어렵다.
  ```
  딕셔너리 메서드
  ```
  # 추가
  print(dic1)
  dic1["숫자5"]=5

  # 수정
  print(dic1)
  dic1["숫자5"]=6   #추가와 문법 동일하지만 없던 키일경우 추가 있던 키면 수정

  # 조회
  print(dic1["숫자5"])

  # 삭제
  del list1[0]
  del dic1["숫자5"]
  print(dic1))
  ```
  딕셔너리 전체 조회
  ```
  for k in article.keys() :
     print(k)

  for v in article.values() :
     print(v)

  for v, k in article.items() :
     print("{} : {}".format(k, v))
  ---
  **클래스**
  
  => 같은 성격의 자료구조와 그 자료구조를 처리하는 함수를 따로 모아놓은 것이다.
  
* 속성 정보를 처리한다. 
* 클래스의 첫글자는 대문자로 작성해야하며, 숫자나 특수문자로는 시작할 수 없다. 
* 객체는 복사본이다
* 클래스 안에 함수 메서드 넣을때는 self 사용하기(자신의 것을 사용할 때)
* 별도로 문법안에 들어간 함수는 무조건 self 넣어줘야함.
 
 ---
 **외부 모듈**
 
 외부 모듈을 가져와서 사용할 수 있다.
 ```
 import class3
 class3.bye()

 from class3 import bye # bye 함수 사용
 from class3 import * # 전체 함수 사용
 ```

 ---
 **파일저장 및 가져오기**

 1) 파일 저장

 ```기본문법 => open("파일경로/파일이름.확장자","모드")```
  - 모드는 4가지 정도 외우기
  - 텍스트 문서는 t, 그 외 이미지나 사운드는 다 b
    - wb - 2진수로 작성 
    - wt - 문자로 작성
    - rb - 2진수로 읽어옴
    - rt - 문자로 읽어옴 
  - 다 작성했으면 꼭 close() 써서 닫아주기

 2) 파일 가져오기 예시
  ```
  f2 = open("class2.txt", "rt")
  print(f2.read()) # 전체 읽어옴
  print(f2.readline()) # 한줄씩 읽어옴
  f2.close()
  ```
---
**파이썬으로 html, 서버 사용하는 법(scrap)**

- pip install requests   =>  서버, html 받아오는 프로그램 설치
- pip install bs4    =>    BeautifulSoup 설치

`import requests as req 
from bs4 import BeautifulSoup` 
( requests 모듈 -> 웹페이지를 요청하고 응답데이터를 받을 수 있음)
      
요청시 헤더정보를 크롬으로 지정
```
request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보는 다 쳐낸다. 따라서 기기정보를 작성해 준 것
```
특정 사이트에 페이지 요청. 응답 데이터 반환
```
response = req.get("http://news.naver.com/",headers=request_headers)
print(response)
```

##### <Response [200] 이라고 뜨면 성공적으로 서버에 접근한 것


html 읽어오기 위한 코드
```
print(response.text)

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
print(html_doc)
"""
```
```
soup = BeautifulSoup(html_doc,'html.paser')  # soup을 이용해서 html_doc 문자열을 피싱. 그 내용을 soup 변수로 대입
alist = soup.select("a")  # 선택자를 이용해 태그 선택
print(alist[1].text) # a 태그의 두번째 것만 겟해서 텍스트 가져오기
print(alist[1]["href"]) # 속성값 가져오기 <태그명 속성명 = "속성값" 속성명2 = "속성값2">
```