import requests
from bs4 import BeautifulSoup

url = 'https://www.daftarperusahaan.com/bidang/'
bidang = 'migas'
page = 0
params = {
 'page' : page
}

res = requests.get(url + bidang, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
clear_block = soup.find('div', class_='clear-block')

