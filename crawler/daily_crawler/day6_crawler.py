import movies as movies
import requests
from bs4 import BeautifulSoup
import time
import csv
import random




USER_AGENTS=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',
]
def fetch(url):
    headers = {
        'User-Agent':random.choice(USER_AGENTS)
    }
    r=requests.get(url,headers=headers,timeout=10)
    r.encoding='utf-8'
    return r
def parse(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',class_='item')
    movies=[]
    for item in items:
        title_tag=item.find('span',class_='title')
        if not title_tag or '/' in title_tag.text:
            continue
        title = title_tag.text
        rating_tag=item.find('span',class_='rating_num')
        rating=rating_tag.text if rating_tag else ''
        people=''
        spans=item.find_all('span')
        if len(spans)>1:
            people = spans[-2].text.replace('人评价', '')
        quote_q=item.find('p',class_='quote')
        quote_tag = quote_q.find('span') if quote_q else ''
        quote=quote_tag.text if quote_tag else ''
        movies.append([title,rating,people,quote])
    return movies



def save_csv(data,filename):
    with open(filename,'w',newline='',encoding='utf-8-sig') as f:
        writers=csv.writer(f)
        writers.writerow(['标题','评分','评价人数','评语'])
        writers.writerows(data)

def main():
    all_movies=[]
    for page in range(10):
        url=f'http://movie.douban.com/top250?start={page * 25}'
        r=fetch(url)
        movies=parse(r.text)
        all_movies.extend(movies)
        print(f'一共{page+1}页完成,共{len(all_movies)}条信息')
        time.sleep(random.uniform(1,2))
    save_csv(all_movies,'4.28_test')
    print('全部完成')

if __name__ == '__main__':
    main()