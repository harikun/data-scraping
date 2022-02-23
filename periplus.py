import requests; import time; import pandas as pd; from bs4 import BeautifulSoup;
start_time = time.time()
url = 'https://www.periplus.com/c/1/books?'
sar = 1; page = 1; page_end = 418; periplus_list = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
while page < 2:
    params = {
        'page' : page,
        'sar' : 1,
    }
    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    section = soup.find('section', class_='product-area shop-sidebar shop section')
    container = section.find('div', class_='container')
    row_category = container.find('div', class_='row row-category')
    row_categor_grid = row_category.find_all('div', class_='row row-category row-categor-grid')
    row = row_categor_grid[2].find_all('div', class_='col-xl-2 col-lg-4 col-md-6 col-6')
    page += 1