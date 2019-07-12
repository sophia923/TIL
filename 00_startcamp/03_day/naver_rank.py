import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

# 요청 보내서 html 받고

html = requests.get(url).text

# 뷰숲으로 정제

soup = BeautifulSoup(html, 'html.parser')

# select 메서드로 사용해서 list 를 얻어낸다.

name = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
for i in name:
    print(i.text)

# 뽑은 list 를 with 구문으로 잘 작성해보자 (txt)

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
    for i in name:
        f.write(f'{i.text}\n')

# with open('example.txt', 'w', encoding='utf-8') as f:

