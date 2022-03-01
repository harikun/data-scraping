import requests; from bs4 import BeautifulSoup; import pandas as pd;

page = 1; max_page = 175; daftar_perusahaan_pers = []
while page < max_page:
    url = 'https://datapers.dewanpers.or.id/site/iframe-verified?'
    params = {
        'page': page,
        'per-page': 10,
        '_pjax': '#grid',
        '_pjax': '#grid',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    all_tr = tbody.find_all('tr')
    for tr in all_tr:
        td = tr.find_all('td')
        no = int(td[0].get_text())
        nama_media = td[1].get_text()
        jenis_media = td[2].get_text()
        penanggung_jawab = td[3].get_text()
        pemimpin_redaksi = td[4].get_text()
        badan_hukum = td[5].get_text()
        provinsi = td[6].get_text()
        alamat = td[7].get_text()
        telp = td[8].get_text()
        email = td[9].get_text()
        daftar_perusahaan_pers.append({
            'no': no,
            'nama media': nama_media,
            'jenis media': jenis_media,
            'penanggung jawab': penanggung_jawab,
            'pemimpin redaksi': pemimpin_redaksi,
            'badan hukum': badan_hukum,
            'provinsi': provinsi,
            'alamat': alamat,
            'email': email
        })
        print(no, nama_media, email)
    page += 1
df = pd.DataFrame(daftar_perusahaan_pers)
df.to_excel(f'data_excel/daftar_perusahaan_pers_{no}.xlsx', index=False)
df.to_csv(f'data_csv/daftar_perusahaan_pers_{no}.csv', index=False)
df.to_json(f'data_json/daftar_perusahaan_pers-{no}.json', orient='records')
print('Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')