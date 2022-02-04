# scraping data list company in Indonesia from kpbn.co.id
import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://kpbn.co.id/persh.php?'
params ={
 'alphabet':'a'
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

content_header = soup.find('table')
content_body = content_header.find_all('tr')
content = content_body[2]
content_td = content.find('td')
content_table = content_td.find('table', {'border':'1'})

data = content_table.find_all('tr')
end_data = len(data) - 1
for item in data[2:end_data]:
 no = item.find('td').text
 print(no)