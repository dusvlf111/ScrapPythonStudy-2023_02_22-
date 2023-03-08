import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=799793'


res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print('https://comic.naver.com' + link)
# print(title) 

for cartton in cartoons:
    title = cartton.a.get_text()
    link = 'https://comic.naver.com' + cartton.a['href']
    print(title, link)