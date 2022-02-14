import json; import time; import requests; import pandas as pd; from bs4 import BeautifulSoup
start_time = time.time()
url = 'https://www.pertamina.com/id/informasi-kapal'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
outerMainSection = soup.find('section', {'id': 'outerMainSection'})
row_container = outerMainSection.find('div', {'class': 'row-container'})
card_bg_white = row_container.find('div', {'class': 'card'})
bard_body = card_bg_white.find('div', {'class': 'card-body'})
col_lg_9 = bard_body.find('div', {'class': 'col-lg-9'})
table_responsive = col_lg_9.find_all('div', {'class': 'table-responsive'})
tr = table_responsive[0].find_all('tr')[1:]
for dt in tr:
    no = dt.find('td').text.strip()
    nama_kapal = dt.find('td').findNextSibling().text.strip()
    pemilik = dt.find('td').findNextSibling().findNextSibling().text.strip()
    keterangan = dt.find('td').findNextSibling().findNextSibling().findNextSibling().text.strip()
    print(no, nama_kapal, pemilik, keterangan)

print("--- %s seconds ---" % (time.time() - start_time))