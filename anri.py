import requests; import pandas as pd; from bs4 import BeautifulSoup
page = 1; daftar_arsip = []; no = 0; base_url = 'https://anri.go.id/'
while page < 2:
    res = requests.get(f'https://anri.go.id/sekitar-arsip/arsip-statis/sarana-temu-balik-arsip/daftar-arsip?page={str(page)}')
    soup = BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    all_tr = tbody.find_all('tr')
    for tr in all_tr:
        no = int(tr.find('td').text)
        nama_file = tr.find_all('td')[1].text
        tahun = int(tr.find_all('td')[2].text)
        tautan = base_url + tr.find_all('td')[3].find('a')['href']
        daftar_arsip.append({'no': no, 'nama file': nama_file, 'tahun': tahun, 'tautan': tautan})
        print(no)
    page += 1
df = pd.DataFrame(daftar_arsip)
df.to_csv(f'data_csv/anri_daftar_arsip_{no}.csv', index=False)
df.to_excel(f'data_excel/anri_daftar_arsip_{no}.xlsx', index=False)
df.to_json(f'data_json/anri_daftar_arsip_{no}.json', orient='records')
print('Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')