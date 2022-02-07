import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

page = 0

company_list = []
while (page < 623):
	url = 'https://www.daftarperusahaan.com/bidang/'
	bidang = 'migas'
	params = {'page' : page	}
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
		try:
			fax = content_block.find('div', class_='field field-type-text field-field-fax').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			telfon = content_block.find('div', class_='field field-type-text field-field-telepon').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			kode = content_block.find('div', class_='field field-type-text field-field-kode').find('div', class_='field-items').find('div', class_='field-item').text.replace('\n', '').strip()
			email = content_block.find('div', class_='field field-type-text field-field-email').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			website = content_block.find('div', class_='field field-type-text field-field-website').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			try:
				bidang = content_block.find('div', class_='field field-type-text field-field-bidangnya').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			except:
				bidang = content_block.find('div', class_='field field-type-text field-field-keterangan').find('div', class_='field-items').find('div', class_='field-item').text.replace('\n', '').strip()
			broker = content_block.find('div', class_='field field-type-text field-field-broker').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('\n', '').strip()
			npwp = content_block.find('div', class_='field field-type-text field-field-npwp').find('div', class_='field-items').find('div', class_='field-item odd').text.replace('NPWP :', '').strip()
		except:
			fax = ''
			telfon = ''
			kode = ''
			email = ''
			website = ''
			bidang = ''
			broker = ''
			pwp = ''

		data_dict = {
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
	page += 1
	print(page)

with open(f'data_json/daftarperusahaan_{len(company_list)}.json', 'w') as outfile:
	json.dump(company_list, outfile)

df = pd.DataFrame(company_list)
df.to_csv('data_csv/daftarperusahaan.csv', index=False)
print(f'{len(company_list)} data saved to csv')

df = pd.DataFrame(company_list)
df.to_excel('data_excel/daftarperusahaan.xlsx', index=False)
print(f'{len(company_list)} data saved to excel')
