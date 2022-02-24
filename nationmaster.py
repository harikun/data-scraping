import requests; import time; import pandas as pd; from bs4 import BeautifulSoup;
start_time = time.time()
url = 'https://www.nationmaster.com/country-info/stats/Military/Army/Main-battle-tanks'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
tbody = soup.find('tbody')
for tr in tbody.find_all('tr'):
    rangking = tr.find('td').text
    country = tr.find('td').find_next_sibling('td').find('a').find('span', {'class': 'full'}).text.strip()
    tank = tr.find('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', '.').strip()
    print(rangking, country, tank)
print('--- %s seconds ---' % (time.time() - start_time))