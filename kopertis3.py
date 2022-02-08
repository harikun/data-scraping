import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_pts():
	url = 'http://kopertis3.or.id/v2/2010/09/08/alamat-perguruan-tinggi-swasta-no-urut-1-200/'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')

	table = soup.find('table')
	tr = table.find_all('tr')
	pts = []
	no = 0
	for i in range(1, len(tr)):
		no = int(tr[i].find('td').text.strip())
		kpdti = int(tr[i].find('td').find_next_sibling('td').text.strip())
		pts_name = tr[i].find('td').find_next_sibling('td').find_next_sibling('td').text.strip()
		pts_address = tr[i].find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
		try:
			pos_code = int(tr[i].find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip())
		except:
			pos_code = ""
		pts_phone = tr[i].find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
		fax = tr[i].find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
		pts.append({
			'no': no,
			'kpdti': kpdti,
			'nama pts': pts_name,
			'alamat': pts_address,
			'kode pos': pos_code,
			'telp': pts_phone,
			'fax': fax
		})

	with open(f'data_json/pts_kopertis3_{no}.json', 'w') as outfile:
		json.dump(pts, outfile, indent=4)

	df = pd.DataFrame(pts)
	df.to_csv(f'data_csv/pts_kopertis3_{no}.csv', index=False)

	df = pd.DataFrame(pts)
	df.to_excel(f'data_excel/pts_kopertis3_{no}.xlsx', index=False)
	print(f'{no} pts berhasil di download')


def get_website_pts():
	url = 'http://kopertis3.or.id/v2/link-pts/'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')

	entry = soup.find('div', class_='entry')
	li = entry.find_all('li')

	no = 0
	website_pts = []
	for i in range(len(li)):
		try:
			kpdti = li[i].find('a').text.split(' ')[0]
			pts_name = li[i].find('a').text.replace(kpdti, '').strip()
		except:
			kpdti = ""
			pts_name = ""
		print(no, pts_name)
		no += 1

get_website_pts()
# get_pts()
