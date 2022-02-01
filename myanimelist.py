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
all_content = content.find_all('tr', {'class': 'ranking-list'})
for item in all_content:
    rank = item.find('td', {'class': 'rank ac'}).text
    title = item.find('h3', {'class': 'anime_ranking_h3'}).text
    link_page = item.find('h3', {'class': 'anime_ranking_h3'}).find('a')['href']
    info_eps = item.find('div', {'class': 'information'}).text
    info_eps = info_eps.split('\n')
    eps = info_eps[1].strip()
    show_time = info_eps[2].strip()
    member = info_eps[3].strip()
    total_member = member.split(' ')[0]
    score = item.find('td', {'class': 'score ac'}).text
    print(eps, score)
#export data to csv & json
#run
