from time import sleep
import requests; import pandas as pd; from bs4 import BeautifulSoup; import json
page = 1; max_page = 2; paten_terdaftar = []; no = 0

while page < max_page:
    res = requests.get(f'https://pdki-indonesia-api.dgip.go.id/api/patent/search?keyword=&page={str(page)}&type=patent&order_state=asc')
    soup = BeautifulSoup(res.content, 'html.parser')
    datajson = json.loads(soup.text)

    for data in datajson['hits']['hits']:
        no += 1
        id = data['_id']
        judul_permohonan = data['_source']['judul_permohonan']
        abstract = data['_source']['abstract']
        nama_pemegang = data['_source']['owner'][0]['nama_pemegang']
        nationality = data['_source']['owner'][0]['nationality']
        nama_pemeriksa = data['_source']['nama_pemeriksa']
        nomor_publikasi = data['_source']['nomor_publikasi']
        tanggal_dimulai_perlindungan = data['_source']['tanggal_dimulai_perlindungan']
        tanggal_penerimaan = data['_source']['tanggal_penerimaan']
        tanggal_publikasi = data['_source']['tanggal_publikasi']

        paten_terdaftar.append({
        'no': no,
        'id': id,
        'judul_permohonan': judul_permohonan,
        'abstract': abstract,
        'nama_pemegang': nama_pemegang,
        'nationality': nationality,
        'nama_pemeriksa': nama_pemeriksa,
        'nomor_publikasi': nomor_publikasi,
        'tanggal_dimulai_perlindungan': tanggal_dimulai_perlindungan,
        'tanggal_penerimaan': tanggal_penerimaan,
        'tanggal_publikasi': tanggal_publikasi
        })

    print(page)
    page += 1
df = pd.DataFrame(paten_terdaftar)
df.to_excel(f'data_excel/paten_terdaftar.xlsx', index=False)
df.to_json(f'data_json/paten_terdaftar.json', orient='records')

print('-----done----')