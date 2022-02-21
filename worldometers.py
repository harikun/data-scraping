from numpy import append
import requests; from bs4 import BeautifulSoup; import time; import pandas as pd;
start_time = time.time()
url = 'https://www.worldometers.info/world-population/population-by-country/'
url_coronavirus = 'https://www.worldometers.info/coronavirus/'
base_url = 'https://www.worldometers.info/'
res = requests.get(url_coronavirus)
soup = BeautifulSoup(res.content, 'html.parser')
tbody = soup.find('tbody')
all_content = tbody.find_all('tr')[8:]
world_pop_2020 = []
for td in all_content:
    no = td.find('td').text
    country = td.find('td').find_next_sibling('td').text
    # country_link = base_url + td.find('td').find_next_sibling('td').find('a').get('href')
    population_2020 = int(td.find('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', ''))
    # yearly_change = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    net_change = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', '')
    # density_per_km2 = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', '')
    land_area_per_km2 = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', '')
    # try:
    #     migrants_net = int(td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace(',', ''))
    # except:
    #     migrants_net = ''
    # fert_rate = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    # med_age = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    # urban_population = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    # world_share = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
# world_pop_2020 = pd.DataFrame({'No': [no], 'Country': [country], 'Country link': [country_link], 'Population 2020': [population_2020], 'Yearly change': [yearly_change], 'Net change': [net_change], 'Density per km2': [density_per_km2], 'Land area per km2': [land_area_per_km2], 'Migrants (net)': [migrants_net], 'Fert rate': [fert_rate], 'Med age': [med_age], 'Urban population': [urban_population], 'World share': [world_share]})
    world_pop_2020.append({'No': no, 'Country': country, 'total case': population_2020, 'total deaths': net_change, 'total recovered': land_area_per_km2})
df = pd.DataFrame(world_pop_2020)
df.to_csv(f'data_csv/coronavirus_{no}.csv', index=False)
df.to_excel(f'data_excel/coronavirus_{no}.xlsx', index=False)
df.to_json(f'data_json/coronavirus_{no}.json', orient='records')
print("--- %s seconds ---" % (time.time() - start_time))