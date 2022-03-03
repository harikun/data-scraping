import requests; import pandas as pd; from bs4 import BeautifulSoup
res=requests.get('https://wetv.vip/channel/anime?id=anime.all_content&type=PAGE_TYPE_ALBUM_FILTER')
soup=BeautifulSoup(res.content,'html.parser')
module__list = soup.find('div',{'class':'module__list'})
module__item = module__list.find_all('div',{'class':'module__item'})
anime_list = []; no = 0
for i in module__item:
    print(i)