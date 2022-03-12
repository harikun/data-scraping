import json; import requests; import time; from bs4 import BeautifulSoup; import pandas as pd;
start_time = time.time()
url = 'https://arebi.co.id/arebi_member/carianggota.php?cari='
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
tr = soup.find_all('tr')[1:]
member_arebi = []; no = 0
for td in tr:
    no = int(td.find('td').text)
    Merk = td.find('td').find_next_sibling('td').text
    alamat = td.find('td').find_next_sibling('td').find_next_sibling('td').text
    member_arebi.append({'no': no, 'Merk': Merk})
df = pd.DataFrame(member_arebi)
df.to_csv(f'data_csv/member_arebi_{no}.csv', index=False)
df.to_excel(f'data_excel/memebr_arebi_{no}.xlsx', index=False)
df.to_json(f'data_json/member_arebi_{no}.json', orient='records')
print("--- %s seconds ---" % (time.time() - start_time))