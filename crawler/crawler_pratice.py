import requests
from bs4 import BeautifulSoup
import random
import time



session = requests.Session()

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',

]
def fetch(url,retry=3):
    for i in range(retry):
        try:
            headers={'User-Agent':random.choice(USER_AGENTS)}
            r= requests.get(url,headers=headers,timeout=10)
            if r.status_code == 200:
                print(f'拿到网页，长度{len(r.text)}')
                return r
            print(f'重试{i+1}')
        except:
            time.sleep(2)

            return None
def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    titles = []
    # print('找到title数量:',len(soup.find_all('span',class_='title')))
    for item in soup.find_all('span',class_='title'):
        # print('原始文本',item.text)
        if '/' not in item.text:
            titles.append(item.text)
    return titles



def main():
    all_data=[]
    for page in range(10):
        url=f'http://movie.douban.com/top250?start={page*25}'
        r=fetch(url)
        if not r:
            break
        data = parse(r.text)
        all_data.extend(data)
        print(f'第{page+1}页：{len(data)}条')
        time.sleep(random.uniform(1,2))
    print(f'共{len(all_data)}条')
if __name__ == '__main__':
    main()
