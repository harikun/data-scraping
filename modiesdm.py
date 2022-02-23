import requests; from bs4 import BeautifulSoup; import time
start_time = time.time()
url = 'https://modi.esdm.go.id/portal/dataPerusahaan/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
page = 1; max_page = 301
params = {
    'page' : 1,
}
res = requests.get(url, params=params,  headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
tbody = soup.find('tbody')
tr = tbody.find_all('tr')[:20]
for i in tr:
    no = i.find_all('td')[0].text
    nama_perusahaan = i.find_all('td')[1].text
    nomor_akte = i.find_all('td')[2].text
    tanggal_akte = i.find_all('td')[3].text
    jenis_perizinan = i.find_all('td')[4].text