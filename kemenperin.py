import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
start_time = time.time()
page = 1; no = 0
# total page 678 / ekporti 218
kemenperin_data = []
while page < 219:
 url = 'https://kemenperin.go.id/direktori-perusahaan?'
 url_eksportir = 'https://www.kemenperin.go.id/direktori-eksportir?'
 params = {
  "&hal": page,
  "what": 'a',
  "&prov": 0,
 }
 res = requests.get(url_eksportir, params=params)
 soup = BeautifulSoup(res.text, 'html.parser')
 content = soup.find('tbody')
 all_content = content.find_all('tr')
 for item in all_content:
  try:
   no += 1
   company_name = item.find('td').find_next_sibling('td').find('b').text
   address = item.find('td').find_next_sibling('td').contents[2].strip()
   telp = item.find('td').find_next_sibling('td').contents[4].replace('Telp. ', '').strip()
   try:
    web = item.find('td').find_next_sibling('td').find('a').text
   except:
    web = ''
   komoditi = item.find('td').find_next_sibling('td').find_next_sibling('td').text
   bidang_usaha = item.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
  except:
   no = '-'
   company_name = '-'
   address = '-'
   telp = '-'
   komoditi = '-'

  data_dict = {
   'no':no,
   'Nama Perusahaan':company_name,
   'Alamat':address,
   'Telepon':telp,
   'website':web,
   'Komoditi':komoditi,
   'Bidang Usaha':bidang_usaha,
  }
  kemenperin_data.append(data_dict)
 print(page)
 page += 1

df = pd.DataFrame(kemenperin_data)
df.to_csv(f'data_csv/kemenperin_exportir_{no}.csv', index=False)
df.to_json(f'data_json/kemenperin_exportir_{no}.json', orient='records')
df.to_excel(f'data_excel/kemenperin_exportir_{no}.xlsx', index=False)
print(f'{time.time() - start_time} seconds')
