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
soup = BeautifulSoup(res.text, 'html.parser')

content = soup.find_all('div', {'class': 'lister-item mode-detail'})
for item in content:
    item_header = item.find('h3', {'class': 'lister-item-header'})
    no_text = item_header.find('span', {'class': 'lister-item-index'}).text
    no = int(no_text.strip('.'))
    title = item_header.find('a').text
    year = item_header.find('span', {'class': 'lister-item-year text-muted unbold'}).text.replace('(', '').replace(')', '')
    try:
     certificate = item.find('p', {'class': 'text-muted text-small'}).find('span', {'class': 'certificate'}).text
    except:
     certificate = 'Unrated'
    run_time_text = item.find('p', {'class': 'text-muted text-small'}).find('span', {'class': 'runtime'}).text
    run_time = int(run_time_text.split(' ')[0])
    genre = item.find('p', {'class': 'text-muted text-small'}).find('span', {'class': 'genre'}).text.strip()
    rating_widget = item.find('div', {'class': 'ipl-rating-widget'}).find('span', {'class': 'ipl-rating-star__rating'}).text
    rating = float(rating_widget)
    description = item.find('p', {'class': ''}).text
    star_actor = item.find_all('p', {'class': 'text-muted text-small'})
    director_actor = star_actor[1].text.strip()
    vote_text = star_actor[2].find('span', {'name': 'nv'}).text
    vote = int(vote_text.replace(',', ''))
    release_date = item.find('div', {'class': 'list-description'}).find('p').text.strip()
    print(no, year)
    # print(certificate, run_time, genre)