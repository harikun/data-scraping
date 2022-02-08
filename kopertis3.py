import json
import requests
from bs4 import BeautifulSoup

url = 'http://kopertis3.or.id/v2/2010/09/08/alamat-perguruan-tinggi-swasta-no-urut-1-200/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())