import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}
all_title=[]
for page in range(10):
    start = page*25
    url = f'http://movie.douban.com/top250?start={start}'
    response = requests.get(url, headers=headers)
    response.encoding='utf-8'
    print(f'状态码{response.status_code}')
    soup = BeautifulSoup(response.text,'html.parser')
    titles = soup.find_all('span',class_='title')
    for title in titles:
        if '/' not in title.text:
            print(title.text)
    print(f'第{page}页加载完成，当前一共{start}条')
print('\n=====全部电影=====')
for i ,title in enumerate(all_title,1):
    print(f'{i},{title}')