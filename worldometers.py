import requests; from bs4 import BeautifulSoup; import time; import pandas as pd;
start_time = time.time()
url = 'https://www.worldometers.info/world-population/population-by-country/'
base_url = 'https://www.worldometers.info/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
tbody = soup.find('tbody')
all_content = tbody.find_all('tr')
for td in all_content:
    no = td.find('td').text
    country = td.find('td').find_next_sibling('td').text
    country_link = base_url + td.find('td').find_next_sibling('td').find('a').get('href')
    population_2020 = int(td.find('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', ''))
    yearly_change = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    net_change = int(td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', ''))
    density_p_km2 = int(td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', ''))
    print(no, density_p_km2)