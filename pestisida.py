import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
url = 'https://pestisida.id/simpes_app/rekap_komoditas_formula.php?'
s_keyword = input('masukkan nama tanaman:')
page = 1
params = {
    's_keyword': s_keyword,
    'rekap_komoditas_formula1Page': page
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
tr = soup.find_all('tr', class_='Row')
Navigator = soup.find('span', class_='Navigator')
img = Navigator.find_all('img')
for i in img:
    if i['src'] == 'Styles/GreenApple/Images/en/ButtonNext.gif':
        page += 1
