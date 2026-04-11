import random
import requests
from bs4 import BeautifulSoup
import time
import csv


url='http://movie.douban.com/top250'
UESR_AGENTS=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',
]

headers={
    'User-Agent': random.choice(UESR_AGENTS)
}
r=requests.get(url,headers=headers,timeout=10)

r.encoding='utf-8'

soup=BeautifulSoup(r.text,'html.parser')
titles=soup.find_all('span',class_='title')

result=[]
rank=1
for t in titles:
    if '/' not in t.text:
        result.append([rank,t.text])
        rank +=1
with open('douban_top250_2.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerow(['排名','名称'])
    writer.writerows(result)
print('打印完成')
