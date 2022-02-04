# scraping data list company in Indonesia from kpbn.co.id
import json
import time
from numpy import number
import requests
import pandas as pd
from bs4 import BeautifulSoup

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
company_list = []
for alfa in alfabet:
 url = 'https://kpbn.co.id/persh.php?'
 params ={
  'alphabet':alfa
 }
 res = requests.get(url, params=params)
 soup = BeautifulSoup(res.text, 'html.parser')

 content_header = soup.find('table')
 content_body = content_header.find_all('tr')
 content = content_body[2]
 content_td = content.find('td')
 content_table = content_td.find('table', {'border':'1'})

 data = content_table.find_all('tr')
 end_data = len(data) - 1
 for item in data[2:end_data]:
  try:
   no = item.find('td').text
  except:
   no = '-'

  try:
   name = item.find('td').find_next_sibling('td').text.replace('\n', '')
  except:
   name = '-'

  try:
   group = item.find('td').find_next_sibling('td').find_next_sibling('td').text
  except:
   group = ''

  try:
   head_office = item.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace('\n', '')
  except:
   head_office = ''

  try:
   telephone_1 = item.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[0].strip()
  except:
   telephone_1 = ''

  try:
   telephone_2 = item.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[2].strip()
  except:
   telephone_2 = ''
  try:
   fax = item.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
  except:
   fax = ''

  data_dict = {
   'no':no,
   'Nama Perusahaan':name,
   'Grup':group,
   'Alamat':head_office,
   'Telepon 1':telephone_1,
   'Telepon 2':telephone_2,
   'Fax':fax
  }
  company_list.append(data_dict)

with open(f'data_json/company_list_.json', 'w') as f:
 f.write(json.dumps(company_list))
 f.close()
print('Success to scrap data company list json')

df = pd.DataFrame(company_list)
df.to_csv(f'data_csv/company_list_.csv', index=False)
print('Success to scrap data company list csv')

df = pd.DataFrame(company_list)
df.to_excel(f'data_excel/company_list_.xlsx', index=False)
print('Success to scrap data company list xlsx')

