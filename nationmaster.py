import requests; import time; import pandas as pd; from bs4 import BeautifulSoup;
start_time = time.time()
url = 'https://www.nationmaster.com/country-info/stats/Military/Army/Main-battle-tanks'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
main_battle_tanks = []; no = 0
tbody = soup.find('tbody')
for tr in tbody.find_all('tr'):
    no += 1
    rangking = tr.find('td').text
    country = tr.find('td').find_next_sibling('td').find('a').find('span', {'class': 'full'}).text.strip()
    tank = tr.find('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', '.').strip()
    year = int(tr.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip())
    main_battle_tanks.append({ 'no': no, 'rangking' : rangking, 'country' : country, 'number of tank' : tank, 'year' : year })
df = pd.DataFrame(main_battle_tanks)
df.to_csv(f'data_csv/main_battle_tanks_{no}.csv', index=False)
df.to_excel(f'data_excel/main_battle_tanks_{no}.xlsx', index=False)
df.to_json(f'data_json/main_battle_tanks_{no}.json', orient='records')
print('--- %s seconds ---' % (time.time() - start_time))

print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')
print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')