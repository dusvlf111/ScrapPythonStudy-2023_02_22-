import requests
from bs4 import BeautifulSoup

url = 'https://sell.smartstore.naver.com/#/naverpay/manage/order'


res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
store = soup.find_all('td', attrs={'class':'title'})
title = cartoons[0].a.get_text()
link = cartoons[0].a['href']
print('https://comic.naver.com' + link)
print(title) 