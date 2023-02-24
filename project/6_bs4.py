import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # soup 객체에서 첫번째로 발견되는 a엘리먼트 정보 출력
#print(soup.a.attrs) # a element 의 속성 정보 출력
#print(soup.a['href']) # a element 의 href 속성 값 정보를 출력

#print(soup.find('a',attrs= {'class': 'Nbtn_upload'})) class="Nbtn_upload" 인 a element 를 찾아줘
print(soup.find(attrs= {'class': 'Nbtn_upload'}))   # class = Nbtn_upload" 인 어떤 element 를 찾아줘
