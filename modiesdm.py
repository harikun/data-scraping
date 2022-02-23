import requests; from bs4 import BeautifulSoup; import time; import pandas as pd;
start_time = time.time()
url = 'https://modi.esdm.go.id/portal/dataPerusahaan/'
page = 1; max_page = 3; modi_perusahaan_list = []
while page < max_page:
    params = {
        'page' : page,
    }
    res = requests.get(url, params=params)
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')[:20]
    for i in tr:
        no = i.find('td').text
        nama_perusahaan = i.find('td').find_next_sibling('td')
        jenis_perizinan = i.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text
        modi_perusahaan_list.append({
            'no' : no,
            'nama_perusahaan' : nama_perusahaan,
            'jenis_perizinan' : jenis_perizinan
        })
    print(page)
    page += 1
df = pd.DataFrame(modi_perusahaan_list)
df.to_csv(f'data_csv/modi_perusahaan_{no}.csv', index=False)
df.to_excel(f'data_excel/modi_perusahaan_{no}.xlsx', index=False)
df.to_json(f'data_json/modi_perusahaan_{no}.json', orient='records')
print('--- %s seconds ---' % (time.time() - start_time))