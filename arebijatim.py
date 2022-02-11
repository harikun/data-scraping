import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://arebijatim.org/anggota'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')
tr = tbody.find_all('tr')
no = 1
member_arebijatim = []
for td in tr:
    member_id = td.find('td').text
    logo = td.find('img').get('src')
    brand_name = td.find('td').find_next_sibling('td').find_next_sibling('td').text
    company_name = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    principal_and_vice = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    address = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
    email = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text

    member_arebijatim.append({
        'no': no,
        'member id': member_id,
        'logo': logo,
        'brand name': brand_name,
        'company name': company_name,
        'principal and vice': principal_and_vice,
        'address': address,
        'email': email
    })
    no += 1

with open('data_json/arebijatim_144.json', 'w') as f:
    json.dump(member_arebijatim, f, indent=4)

df = pd.DataFrame(member_arebijatim)
df.to_csv('data_csv/arebijatim_144.csv', index=False)

df = pd.DataFrame(member_arebijatim)
df.to_excel('data_excel/arebijatim_144.xlsx', index=False)
print('Done!')
