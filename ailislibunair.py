import requests; import pandas as pd; from bs4 import BeautifulSoup;
page = 1; max_page = 2; buku_perpus_unair = []; no = 0
while page <= max_page:
    res = requests.get(f'http://ailis.lib.unair.ac.id/opac/pencarian-sederhana?action=pencarianSederhana&katakunci=&ruas=Semua+Ruas&bahan=Semua+Jenis+Bahan&fAuthor=&fPublisher=&fPublishLoc=&fPublishYear=&page={str(page)}&limit=10&location=Perpustakaan+Pusat')
    soup = BeautifulSoup(res.text, 'html.parser')
    table2 = soup.find('table', class_='table2 table-striped')
    content = table2.find_all('tr')
    print(content)
    page += 1