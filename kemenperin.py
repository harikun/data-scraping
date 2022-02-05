import json
import requests
from bs4 import BeautifulSoup

url = 'https://kemenperin.go.id/direktori-perusahaan?'
page = 1
params = {
 "hal": page,
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

# pagination = soup.find('ul',{'class': "pagination"})
# pages = pagination.find_all('li')
# for page in pages:
#     page = page.find("a").contents[0].replace('.', '')
#     res = requests.get(url, params=params)
#     soup = BeautifulSoup(res.text, 'html.parser')

content = soup.find('tbody')
all_content = content.find_all('tr')
for item in all_content:
 no = item.find('td', {'align': 'right'}).text.replace('.', '')
 company_name = item.find('td').find_next_sibling('td').find('b').text
 address = item.find('td').find_next_sibling('td').contents[2].strip()
 print(no, address)