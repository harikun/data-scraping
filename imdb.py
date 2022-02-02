# scarping New and Upcoming VOD, DVD, and Blu-ray Releases from imdb.com
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls016522954/?'
params={
 'ref_':'nv_tvv_dv',
 'sort': 'list_order,asc',
 'mode': 'detail',
 'page': '1'
}
res = requests.get(url, params=params)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())