#伪装，请求，解析，打印

import requests
from bs4 import BeautifulSoup
import random

url='http://movie.douban.com/top250'

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',
]

headers={
    'User-Agent':random.choice(USER_AGENT)
}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')
titles=soup.find_all('span',class_='title')
for t in titles:
    if '/' not in t.text:
        print(t.text)




