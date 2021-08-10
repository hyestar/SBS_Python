# pip install requests // 서버, html 받아오는 프로그램
# pip install bs4     // BeautifulSoup 설치

import requests as req   # requests 모듈 -> 웹페이지를 요청하고 응답데이터를 받을 수 있음
from bs4 import BeautifulSoup

# 요청시 헤더정보를 크롬으로 지정
request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보는 다 쳐낸다. 따라서 기기정보를 작성해 준 것


response = req.get("http://news.naver.com/",headers=request_headers)  # 특정 사이트에 페이지 요청. 응답 데이터 반환
print(response)


#<Response [200] 이라고 뜨면 성공적으로 서버에 접근한 것

# html 읽어와야 함.
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
"""
soup=BeautifulSoup(response.text,'html.parser')
tlist = soup.select(".hdline_article_tit > a")
print(tlist)
# print(html_doc)
# soup = BeautifulSoup(html_doc,'html.paser')  # soup을 이용해서 html_doc 문자열을 피싱. 그 내용을 soup 변수로 대입
# alist = soup.select("a")  # 선택자를 이용해 태그 선택
# print(alist[1].text) # a 태그의 두번째 것만 겟해서 텍스트 가져오기
# print(alist[1]["href"]) # 속성값 가져오기 <태그명 속성명 = "속성값" 속성명2 = "속성값2">
