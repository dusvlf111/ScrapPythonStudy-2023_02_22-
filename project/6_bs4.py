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
# print(soup.find(attrs= {'class': 'Nbtn_upload'}))   # class = Nbtn_upload" 인 어떤 element 를 찾아줘

# rank1 = soup.find('li', attrs= {'class': 'rank01'})
# print(rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling # 찾은 엘리먼트의 다음 
# print(rank2.a.get_text())

# rank3 = rank2.previous_sibling.previous_sibling
# print('001',rank3.a.get_text())

#print(rank1.parent)

# rank2 = rank1.find_next_sibling('li') #li 태그만 찾음
# print(rank2.a.get_text())

# rank2 = rank1.find_next_siblings('li') # siblings로 하면 형제들을 가져옴

# print(rank2)

webtoon = soup.find('a', text="청춘 블라썸-125화: EP.4 동채의 꽃 (30)")

print(webtoon)