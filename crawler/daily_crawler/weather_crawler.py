import requests
from bs4 import BeautifulSoup
import random
import csv
import time

with open('weather.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['城市', '日期','温度'])
    province_id={
        '北京': '101010100',
        '上海': '101020100',
        '广州': '101280101',
        '深圳': '101280601',
        '杭州': '101210101',
        '南京': '101190101',
        '成都': '101270101',
        '武汉': '101200101',
        '西安': '101110101',
        '重庆': '101040100',
        '天津': '101030100',
        '苏州': '101190401',

    }
    for city,city_code in province_id.items():
        url=f'https://www.weather.com.cn/weather1d/{city_code}.shtml#search'
        #伪装部分


        USER_AGENTS=[
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64))AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7))AppleWebKit/537.36',
        ]

        headers={
            'User-Agent': random.choice(USER_AGENTS)
        }



        #请求部分
        try:
            r=requests.get(url,headers=headers,timeout=2)
            r.encoding='utf-8'

        except requests.exceptions.RequestException:
            print('error')
            exit()

        #解析部分
        soup=BeautifulSoup(r.text,'html.parser')
        data=soup.find('input',id='hidden_title')
        if data :
            value=data['value']
            part=value.split()
            temperature=part[-1]
            date=part[1]
            print(city,date,temperature)




        writer.writerow([city,part[-1]])