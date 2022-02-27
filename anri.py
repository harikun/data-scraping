import requests; import pandas as pd; from bs4 import BeautifulSoup
page = 1; daftar_arsip = []; no = 0
while page < 2:
    res = requests.get(f'https://anri.go.id/sekitar-arsip/arsip-statis/sarana-temu-balik-arsip/daftar-arsip?page={str(page)}')
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    page += 1