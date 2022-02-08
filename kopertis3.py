import json
import requests
from bs4 import BeautifulSoup

def get_pts():
	url = 'http://kopertis3.or.id/v2/2010/09/08/alamat-perguruan-tinggi-swasta-no-urut-1-200/'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')

	table = soup.find('table')
	tr = table.find_all('tr')

	for i in range(1, len(tr)):
		no = int(tr[i].find('td').text.strip())
		kpdti = int(tr[i].find('td').find_next_sibling('td').text.strip())
		pts_name = tr[i].find('td').find_next_sibling('td').find_next_sibling('td').text.strip()

		print(no, pts_name)

get_pts()
