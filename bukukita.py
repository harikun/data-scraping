import requests; from bs4 import BeautifulSoup; import pandas as pd
page = 1; max_page = 8; buku_kita_populer = []
while page <= 2:
    res = requests.get(f'https://www.bukukita.com/katalogbukuatribut.php?page={str(page)}&atrId=3')
    soup = BeautifulSoup(res.text, 'html.parser')
    page += 1