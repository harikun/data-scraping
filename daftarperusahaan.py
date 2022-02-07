import requests
from bs4 import BeautifulSoup

page = 0
no = 1
company_list = []
while (page < 1):

 url = 'https://www.daftarperusahaan.com/bidang/'
 bidang = 'migas'
 params = {
  'page' : page
 }
 base_url = 'https://www.daftarperusahaan.com'

 res = requests.get(url + bidang, params=params)
 soup = BeautifulSoup(res.text, 'html.parser')
 clear_block = soup.find('div', class_='clear-block')

 for link in clear_block.find_all('div', class_='node'):
  link_url = link.find('a')['href']
  res = requests.get(base_url + link_url)
  soup = BeautifulSoup(res.text, 'html.parser')
  content_block = soup.find('div', class_='content clear-block')
  name = content_block.find('strong').text
  address = content_block.find('p').text
  telfon = content_block.find('div', class_='field field-type-text field-field-telepon').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
  fax = content_block.find('div', class_='field field-type-text field-field-fax').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
  try:
   kode = content_block.find('div', class_='field field-type-text field-field-kode').find('div', class_='field-items').find('div', class_='field-item').text
   email = content_block.find('div', class_='field field-type-text field-field-email').find('div', class_='field-items').find('div', class_='field-item odd').text
   website = content_block.find('div', class_='field field-type-text field-field-website').find('div', class_='field-items').find('div', class_='field-item odd').text
   bidang = content_block.find('div', class_='field field-type-text field-field-bidangnya').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
   broker = content_block.find('div', class_='field field-type-text field-field-broker').find('div', class_='field-items').find('div', class_='field-item odd').text
   npwp = content_block.find('div', class_='field field-type-text field-field-npwp').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('NPWP :', '').strip()
  except:
   kode = ''
   email = ''
   website = ''
   try:
    bidang = content_block.find('div', class_='field field-type-text field-field-keterangan').find('div', class_='field-items').find('div', class_='field-item').text.replace('\n', '').strip()
   except:
    bidang = ''
   broker = ''
   pwp = ''

   # sorting data
   data_dict = {
    'no' : no,
    'name' : name,
    'address' : address,
    'telfon' : telfon,
    'fax' : fax,
    'kode' : kode,
    'email' : email,
    'website' : website,
    'bidang' : bidang,
    'broker' : broker,
    'npwp' : npwp
   }
   company_list.append(data_dict)
   no += 1
 page += 1
 print(page)
 print(company_list)