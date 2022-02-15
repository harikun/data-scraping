import json; import requests; import pandas as pd; from bs4 import BeautifulSoup; import urllib3; import time
start_time = time.time()
url_varieatas = 'https://www.litbang.pertanian.go.id/varietas/'
p = 1; no = 1; daftar_varietas = []
params = { 'p': p }
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

while p < 107:
    res = requests.get(url_varieatas, params=params, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    containter = soup.find('div', {'class': 'col-lg-9 mt-4'})
    table = containter.find('table', {'class':'table table-striped list'})
    tbody = table.find('tbody')
    tr = tbody.find_all('tr')
    for td in tr:
        no = int(td.find('td').text)
        kelompok = td.find('td').find_next_sibling('td').text
        komoditas = td.find('td').find_next_sibling('td').find_next_sibling('td').text
        varietas_detail = url_varieatas + td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find('a')['href']
        nama_varietas = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find('a').text
        tahun = int(td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text)
        daftar_varietas.append({
            'no': no,
            'kelompok': kelompok,
            'komoditas': komoditas,
            'varietas detail': varietas_detail,
            'nama varietas': nama_varietas,
            'tahun': tahun
        })
    p += 1

with open(f'data_json/varietas_{no}.json', 'w') as outfile:
    json.dump(daftar_varietas, outfile, indent=4)
df = pd.DataFrame(daftar_varietas)
df.to_csv(f'data_csv/varietas_{no}.csv', index=False)
df.to_excel(f'data_excel/varietas_{no}.xlsx', index=False)
print("--- %s seconds ---" % (time.time() - start_time))