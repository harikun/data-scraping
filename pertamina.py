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
kapal_list = []; no = 1
for dt in tr:
    no = dt.find('td').text.strip()
    nama_kapal = dt.find('td').findNextSibling().text.strip()
    pemilik = dt.find('td').findNextSibling().findNextSibling().text.strip()
    keterangan = dt.find('td').findNextSibling().findNextSibling().findNextSibling().text.strip()
    kapal_list.append({
        'no': no, 'nama kapal': nama_kapal, 'pemilik': pemilik, 'keterangan': keterangan
    })
with open(f'data_json/pertamina_{no}.json', 'w') as f:
    json.dump(kapal_list, f, indent=4)
df = pd.DataFrame(kapal_list)
df.to_csv(f'data_csv/pertamina_{no}.csv', index=False)
df.to_excel(f'data_excel/pertamina_{no}.xlsx', index=False)
print("--- %s seconds ---" % (time.time() - start_time))