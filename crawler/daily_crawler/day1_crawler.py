import requests
from bs4 import BeautifulSoup
import csv
import time
import random


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
    print(f'请求失败{e}')
    exit()

soup=BeautifulSoup(r.text,'html.parser')
titles=soup.find_all('span',class_='title')
movie_data=[]
rank=1
for t in titles:
    if '/'not in t.text:
        movie_data.append([rank,t.text])
        rank+=1

try:
    with open('douban_top250.csv','w',newline='',encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        writer.writerow(['排名','名称'])
        writer.writerows(movie_data)
    print(f'保存成功共{len(movie_data)}部电影')
except Exception as e:
    print(f'失败{e}')


