import requests; from bs4 import BeautifulSoup; import pandas as pd;
res = requests.get('http://sigpjj.binamarga.pu.go.id/iyo/record/index/?data=57&_tog1149016d=all')
soup = BeautifulSoup(res.text, 'html.parser')
tr = soup.find('tbody').find_all('tr')
no = 0; daftar_kawasan_industri = []
for td in tr:
    no = int(td.find_all('td')[0].get_text())
    nama_kawasan = td.find_all('td')[1].get_text()
    provinsi = td.find_all('td')[2].get_text()
    kabupaten = td.find_all('td')[3].get_text()
    print(no, nama_kawasan, provinsi, kabupaten)
    daftar_kawasan_industri.append({
        'no': no,
        'nama kawasan': nama_kawasan,
        'provinsi': provinsi,
        'kabupaten': kabupaten
    })
df = pd.DataFrame(daftar_kawasan_industri)
df.to_excel(f'data_excel/daftar_kawasan_industri_{no}.xlsx', index=False)
df.to_csv(f'data_csv/daftar_kawasan_industri_{no}.csv', index=False)
df.to_json(f'data_json/daftar_kawasan_industri-{no}.json', orient='records')
print('\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')