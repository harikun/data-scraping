import requests; import pandas as pd; from bs4 import BeautifulSoup
res = requests.get('https://www.centralasialelang.com/properti.php?idC=all&idBk=all&idJ=all&idK=all&idS=all&cari=Cari')
soup = BeautifulSoup(res.text, 'html.parser')
all_tr = soup.find_all('tr')
properti_lelang = []; no = 0
for tr in all_tr[7:]:
    no += 1
    jenis = tr.find('td').text
    kategori = tr.find_all('td')[1].text
    bank = tr.find_all('td')[2].text
    deskripsi = tr.find_all('td')[3].text
    lokasi = tr.find_all('td')[4].text
    properti_lelang.apppend({'no': no, 'jenis': jenis, 'kategori': kategori, 'bank': bank, 'deskripsi': deskripsi, 'lokasi': lokasi})
df = pd.DataFrame(properti_lelang)
df.to_csv(f'data_csv/centralasialelang_{no}.csv', index=False)
df.to_excel(f'data_excel/centralasialelang_{no}.xlsx', index=False)
df.to_json(f'data_json/centralasialelang_{no}.json', orient='records')
print('Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')