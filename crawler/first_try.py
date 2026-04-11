#伪装，请求，解析，打印

import requests
from bs4 import BeautifulSoup
import random
import csv
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


with open('douban_top250.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['排名','电影名称'])
    for i,t in enumerate(titles,1):
        if '/' not in t.text:
            writer.writerow([i,t.text])
print('保存完成')




