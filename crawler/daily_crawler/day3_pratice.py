import requests
from bs4 import BeautifulSoup
import time
import random
import csv


url='http://movie.douban.com/top250'

USER_AGENTS=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',
]


headers={
    'User-Agent':random.choice(USER_AGENTS)
}

try:
    r=requests.get(url,headers=headers,timeout=10)
    r.encoding='utf-8'
except requests.exceptions.RequestException as e:
    print(f'失败，原因{e}')

soup=BeautifulSoup(r.text,'html.parser')
titles=soup.find_all('span',class_='title')

result=[]
rank=1

for t in titles:
    if '/' not in t.text:
        result.append([rank,t.text])
        rank +=1
with open('day4_top250.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerow(['排名','名称'])
    writer.writerows(result)
print('成功')
