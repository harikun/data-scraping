import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://kemenperin.go.id/direktori-perusahaan?'
page = 1
params = {
 "hal": page,
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
next_result = True
kemenperin_data = []
while next_result:
 res = requests.get(url, params=params)
 soup = BeautifulSoup(res.text, 'html.parser')
 content = soup.find('tbody')
 all_content = content.find_all('tr')
 for item in all_content:
  no = item.find('td', {'align': 'right'}).text.replace('.', '')
  company_name = item.find('td').find_next_sibling('td').find('b').text
  address = item.find('td').find_next_sibling('td').contents[2].strip()
  telp = item.find('td').find_next_sibling('td').contents[4].replace('Telp. ', '').strip()
  komoditi = item.find('td').find_next_sibling('td').find_next_sibling('td').text

  data_dict = {
   'no':no,
   'Nama Perusahaan':company_name,
   'Alamat':address,
   'Telepon':telp,
   'Komoditi':komoditi
  }
  kemenperin_data.append(data_dict)
  print(page)
  page += 1

with open(f'data_json/kemenperin.json', 'w') as f:
 json.dump(kemenperin_data, f, indent=4)
 print(f'Successfully export my {page} page data to json file')

df = pd.DataFrame(kemenperin_data)
df.to_csv(f'data_csv/kemenperin.csv', index=False)
print(f'Successfully export my {page} page data to csv file')

df.to_excel(f'data_excel/kemenperin.xlsx', index=False)
print(f'Successfully export my {page} page data to xlsx file')
