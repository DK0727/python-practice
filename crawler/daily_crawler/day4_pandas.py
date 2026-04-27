import random

import requests
from bs4 import BeautifulSoup
import time
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
    print(f'爬取失败，原因{e}')
    exit()


soup=BeautifulSoup(r.text,'html.parser')
# titles=soup.find_all('span',class_='title')
# rating_num=soup.find_all('span',class_='rating_num')

items=soup.find_all('div',class_='item')

result=[]
rank=1
for item in items:
    title_tag=item.find('span',class_='title')
    if not title_tag or '/' in title_tag.text:
        continue
    title = title_tag.text
    rating_tag=item.find('span',class_='rating_num')
    rating= rating_tag.text if rating_tag else ''
    star_div = item.find('div',class_='star')
    num_review = ''
    if star_div:
        spans = star_div.find_all('span')
        if len(spans) >1:
            num_review = spans[-1].text.replace('评价','').strip()
    inq_tag=item.find('span',class_='inq')
    summary = inq_tag.text if inq_tag else ''
    result.append([rank,title,rating,num_review,summary])
    rank+=1




#
# for t in titles:
#     if '/' not in t.text:
#         result.append([rank,t.text])
#         rank+=1


with open('day4_crawler_top250.csv','w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f)
    writer.writerow(['名次','名称','评分','评价人数','简介'])
    writer.writerows(result)
print(f'成功，共{len(result)}部电影')


