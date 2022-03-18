import requests; import pandas as pd; from bs4 import BeautifulSoup
res=requests.get('https://wetv.vip/channel/anime?id=anime.all_content&type=PAGE_TYPE_ALBUM_FILTER')
soup=BeautifulSoup(res.content,'html.parser')
module__list = soup.find('div',{'class':'module__list'})
module__item = module__list.find_all('div',{'class':'module__item'})
anime_list = []; no = 0; base_url = 'https://wetv.vip'
for i in module__item:
    no += 1
    title = i.find('h1',{'class':'item__title'}).text
    link = base_url +  i.find('a',{'class':'item__link--title'})['href']
    print(no, title, link)
    anime_list.append({'no':no, 'title':title, 'link':link})
df = pd.DataFrame(anime_list)
df.to_csv(f'data_csv/wetv-anime-{no}.csv', index=False)
df.to_excel(f'data_excel/wetv-anime-{no}.xlsx', index=False)
df.to_json(f'data_json/wetv-anime-{no}.json', orient='records')
print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')