import requests
from bs4 import BeautifulSoup
url= 'http://www.example.com'
try:
    respons=requests.get(url)
    respons.encoding='utf-8'
    soup =BeautifulSoup(respons.text,'html.parser')
    print('网页标题',soup.title.string)
except Exception as e:
    print(f'爬取失败：{e}')