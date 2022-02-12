import time
import requests
from bs4 import BeautifulSoup

start_time = time.time()
url = 'https://www.aprindo.org/profil-aprindo/'
def download_logo():
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    td_outer_wrap = soup.find('div', {'id': 'td-outer-wrap'})
    td_main_content_wrap = td_outer_wrap.find('div', {'class': 'td-main-content-wrap'})
    td_container = td_main_content_wrap.find('div', {'class': 'td-container'})
    td_pb_row = td_container.find('div', {'class': 'td-pb-row'})
    print(td_pb_row)

download_logo()

print("--- %s seconds ---" % (time.time() - start_time))