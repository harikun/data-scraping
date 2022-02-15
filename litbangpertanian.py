import json; import requests; import pandas as pd; from bs4 import BeautifulSoup; import urllib3; import time
start_time = time.time()
url_varieatas = 'https://www.litbang.pertanian.go.id/varietas/'
p = 1
params = { 'p': p }
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass
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
    print(tahun)
print("--- %s seconds ---" % (time.time() - start_time))