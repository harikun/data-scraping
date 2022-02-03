import json
from turtle import title
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

# scraping manga

def get_total_page():
    url = 'https://myanimelist.net/topmanga.php'
    limit = 0
    params= { 'limit': limit }
    res = requests.get(url, params=params)
    soup = BeautifulSoup(res.text, 'html.parser')
    next_page = soup.find('a', {'class': 'link-blue-box next'}).text

    try:
        while (next_page == 'Next 50'):
            limit += 50
            params= { 'limit': limit }
            res = requests.get(url, params=params)
            soup = BeautifulSoup(res.text, 'html.parser')
            next_page = soup.find('a', {'class': 'link-blue-box next'}).text
            print(limit)
            time.sleep(1)
        else:
            print(' while Total page: ', limit)
    except:
        print(' except Total page: ', limit)

# get_total_page() result is: 57300
def get_all_manga():
    limit = 0
    no = 1
    mymanga_list = []
    while (limit < 100):
        url = 'https://myanimelist.net/topmanga.php'
        params= { 'limit': limit }
        res = requests.get(url, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.find('table', {'class': 'top-ranking-table'})
        all_content = content.find_all('tr', {'class': 'ranking-list'})
        for item in all_content:
            try:
                rank = item.find('span', {'class': 'ranking-data'}).text
            except:
                rank = '-'
            title = item.find('h3', {'class': 'manga_h3'}).text
            link_page = item.find('h3', {'class': 'manga_h3'}).find('a')['href']
            info_eps = item.find('div', {'class': 'information'}).text
            info_eps = info_eps.split('\n')
            print(title, link_page, info_eps)
        limit += 50

get_all_manga()
# scraping anime from myanimelist
# try:
#  limit = 0
#  no = 1
#  myanimelist = []
#  while (limit < 19250):
#   url = 'https://myanimelist.net/topanime.php'
#   params = {
#       'limit': limit,
#   }
#   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
#   res = requests.get(url, headers=headers, params=params)
#   soup = BeautifulSoup(res.text, 'html.parser')
#   #get all items
#   content = soup.find('table', {'class': 'top-ranking-table'})
#   all_content = content.find_all('tr', {'class': 'ranking-list'})

#   for item in all_content:
#       try:
#        rank = item.find('td', {'class': 'rank ac'}).text
#       except:
#        rank = '-'
#       title = item.find('h3', {'class': 'anime_ranking_h3'}).text
#       link_page = item.find('h3', {'class': 'anime_ranking_h3'}).find('a')['href']
#       info_eps = item.find('div', {'class': 'information'}).text
#       info_eps = info_eps.split('\n')
#       eps = info_eps[1].strip()
#       eps_type = eps.split(' ')[0]
#       eps_total = eps.split(' (')[1].replace(' eps)', '')
#       show_time = info_eps[2].strip()
#       member = info_eps[3].strip()
#       total_member = member.split(' ')[0]
#       score = item.find('span', {'class': 'score-label'}).text
#       print(no)
#       # sorting data
#       data_dict = {
#           'no': no,
#           'rank': rank,
#           'title': title,
#           'type': eps_type,
#           'total_eps': eps_total,
#           'show_time': show_time,
#           'member': total_member,
#           'score': score,
#           'link_page': link_page,
#       }
#       myanimelist.append(data_dict)
#       no += 1

#   #get next page
#   next_page = soup.find('a', {'class': 'link-blue-box next'}).text
#   limit += 50
#  with open(f'data_json/myanimelist_{limit}.json', 'w') as f:
#   json.dump(myanimelist, f)
#   f.close()
#  print(f'Successfully export {limit} data to json file')
# #export data to csv & json
#  df = pd.DataFrame(myanimelist)
#  df.to_csv(f'data_csv/myanimelist_{limit}.csv', index=False)
#  print(f'Successfully export {limit} data to csv file')
#  df.to_excel(f'data_excel/myanimelist_{limit}.xlsx', index=False)
#  print(f'Successfully export {limit} data to excel file')
#  print('Done, jumlah anime adalah: ', limit)
# except:
#   print('ada error ', no)
