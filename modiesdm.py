import requests; from bs4 import BeautifulSoup; import time; import pandas as pd;
start_time = time.time()
url = 'https://modi.esdm.go.id/portal/dataPerusahaan/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
page = 1; max_page = 302; modi_perusahaan_list = []; no = 0
params = {
    'page' : 1,
}
while page < max_page:
    res = requests.get(url, params=params,  headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')[:20]
    for i in tr:
        no = i.find_all('td')[0].text
        nama_perusahaan = i.find_all('td')[1].text
        jenis_perizinan = i.find_all('td')[4].text

        modi_perusahaan_list.append({
            'no' : no,
            'nama_perusahaan' : nama_perusahaan,
            'jenis_perizinan' : jenis_perizinan
        })
    page += 1
df = pd.DataFrame(modi_perusahaan_list)
df.to_csv(f'data_csv/modi_perusahaan_{no}.csv', index=False)
df.to_excel(f'data_excel/modi_perusahaan_{no}.xlsx', index=False)
df.to_json(f'data_json/modi_perusahaan_{no}.json', orient='records')
print('--- %s seconds ---' % (time.time() - start_time))