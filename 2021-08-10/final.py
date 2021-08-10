# pip install requests // 서버, html 받아오는 프로그램

import requests as req   # requests 모듈 -> 웹페이지를 요청하고 응답데이터를 받을 수 있음
from bs4 import BeautifulSoup

request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), }
response = req.get("http://news.naver.com/",headers=request_headers)

soup=BeautifulSoup(response.text,'html.parser')

tlist = soup.select("#section_society .mlist2.no_bg a") # 후손이니깐 띄어쓰기

print(tlist[0].text)   # tlist 첫번째 text 겟
url=tlist[0]["href"]  # 주소 링크

response2 = req.get(url,headers=request_headers)
soup2=BeautifulSoup(response2.text, 'html.parser')

# 제목
tag = soup2.select("#articleTitle")
print(tag)  # 이렇게 하면 리스트라서 대괄호가 같이 나오므로 꼭 따로 빼줘야함
tags = tag[0]
title = tags.text

# 등록날짜
tag = soup2.select(".article_info .sponsor .t11")[0]
date = tag.text

# 본문
tag = soup2.select("#articleBody .link_news")[0]
body = tag.text

print("제목 : {}".format(title))
print("등록날짜 : {}".format(date))
print("내용 : {}".format(body))

# 이미지 링크
tag = soup2.select("#articleBody img")
img1 = tag[0]
response3 = req.get(img1["src"],headers=request_headers)

f1 = open("img1.jpg","wb")
f1.write(response3.content)
f1.close()
