import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'html.parser')

# 找到第一个电影块
first_item = soup.find('div', class_='item')

# 方法：找包含"人评价"的span
people_span = first_item.find('span', string=lambda x: x and '人评价' in x)

if people_span:
    print(f"评价人数原始文本: {people_span.text}")
    # 提取数字部分
    import re
    num = re.search(r'\d+', people_span.text).group()
    print(f"评价人数数字: {num}")
else:
    print("没找到评价人数")