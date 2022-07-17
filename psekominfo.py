import requests; import pandas as pd; from bs4 import BeautifulSoup; import json
page = 1; max_page = 564; SE_terdaftar = []; no = 0

while page < max_page:
    res = requests.get(f'https://pse.kominfo.go.id/api/v1/jsonapi/tdpse-terbit?filter[status_id]=TERDAFTAR&filter[lokalitas]=LOKAL&page[page]={str(page)}&page[limit]=10&filter[search_term]=')
    soup = BeautifulSoup(res.content, 'html.parser')
    datajson = json.loads(soup.text)

    for data in datajson['data']:
        no += 1
        SE_terdaftar.append({
        'no': no,
        'type': data['type'],
        'id': data['id'],
        'lokalitas': data['attributes']['lokalitas'],
        'nama': data['attributes']['nama'],
        'nama_perusahaan': data['attributes']['nama_perusahaan'],
        'nama_tampil_badan_hukum': data['attributes']['nama_tampil_badan_hukum'],
        'nomor_pb_umku': data['attributes']['nomor_pb_umku'],
        'nomor_tanda_daftar': data['attributes']['nomor_tanda_daftar'],
        'qr_code': data['attributes']['qr_code'],
        'sektor': data['attributes']['sektor'],
        'sistem_elektronik_id': data['attributes']['sistem_elektronik_id'],
        'status_id': data['attributes']['status_id'],
        'tanggal_daftar': data['attributes']['tanggal_daftar'],
        'tanggal_terbit': data['attributes']['tanggal_terbit'],
        'website': data['attributes']['website'],
        'links': data['links']['self']
        })
    print(page)
    page += 1
df = pd.DataFrame(SE_terdaftar)
df.to_excel(f'data_excel/SE_terdaftar_{str(no)}.xlsx', index=False)
df.to_csv(f'data_csv/SE_terdaftar{str(no)}.csv', index=False)

print('-----done----')