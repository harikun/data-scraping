# scarping New and Upcoming VOD, DVD, and Blu-ray Releases from imdb.com
import json
import requests
import pandas as pd
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
imdb_list = []
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

    data_dict = {
        'no': no,
        'title': title,
        'year': year,
        'certificate': certificate,
        'run time': run_time,
        'genre': genre,
        'rating': rating,
        'description': description,
        'director and actor': director_actor,
        'vote': vote,
        'release date': release_date
    }
    imdb_list.append(data_dict)

with open('data_json/imdb.json', 'w') as f:
    json.dump(imdb_list, f, indent=4)
    f.close()

df = pd.DataFrame(imdb_list)
df.to_csv('data_csv/imdb.csv', index=False)
print(f'imdb.csv saved')
df.to_excel('data_excel/imdb.xlsx', index=False)
print(f'imdb.xlsx saved')
