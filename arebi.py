import json; import requests; import time; from bs4 import BeautifulSoup

url = 'https://arebi.co.id/arebi_member/carianggota.php?cari='
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
