from gettext import NullTranslations
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://lelang.go.id/lot-lelang?'
page = 0
no =	1
params = {
	"no-cache":"Ls6B2X9NdqUOS5vCmYiG",
	"page": page
}
barang_lelang = []
new_result = True
while new_result:
	res = requests.get(url, params=params)
	soup = BeautifulSoup(res.text, 'html.parser')

	products_grid = soup.find('ul', {'class': 'products-grid'})
	products = products_grid.find_all('div', {'class': 'product'})

	for product in products:
		name = product.find('h2', {'class': 'product-name'}).text
		price = product.find('span', {'class': 'product-price'}).text.replace('Rp.', '').replace('.', '')
		price = int(price)
		location = product.find('small').text
		link_product = product.find('h2', {'class': 'product-name'}).find('a')['href']
		link_image = product.find('img')['src']

		barang_lelang.append({
			'no': no,
			'name': name,
			'price': price,
			'location': location,
			'link_product': link_product,
			'link_image': link_image,
		})
		no += 1
	print(page)
	page += 1

with open(f'data_json/barang_lelang_{no}.json', 'w') as f:
	json.dump(barang_lelang, f, indent=4)
print(f'{no} data json saved')

df = pd.DataFrame(barang_lelang)
df.to_csv(f'data_csv/barang_lelang_{no}.csv', index=False)
print(f'{no} data csv saved')

df = pd.DataFrame(barang_lelang)
df.to_excel(f'data_excelbarang_lelang_{no}.xlsx', index=False)
print(f'{no} data csv saved')
