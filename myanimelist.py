import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
res = requests.get(url, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

#get total pages
#get all items
content = soup.find('table', {'class': 'top-ranking-table'})
print(content)
#export data to csv & json
#run
