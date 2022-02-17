import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
start_time = time.time()
url = 'https://bibitonline.com/artikel/kumpulan-nama-bunga-lengkap-dari-a-z-beserta-gambar-dan-penjelasannya'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
figcaption = soup.find_all('figcaption')
daftar_bunga = []; no = 1
for i in figcaption:
    daftar_bunga.append({ 'no': no, 'nama bunga': i.text })
    no += 1
df = pd.DataFrame(daftar_bunga)
df.to_csv(f'data_csv/bunga_{no}.csv', index=False)
df.to_excel(f'data_excel/bunga_{no}.xlsx', index=False)
df.to_json(f'data_json/bunga_{no}.json', orient='records')
print("--- %s seconds ---" % (time.time() - start_time))