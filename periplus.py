import requests; import time; import pandas as pd; from bs4 import BeautifulSoup;
start_time = time.time()
url = 'https://www.periplus.com/c/1/books?'
sar = 1; page = 1; page_end = 417; periplus_list = []; no = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
while page < page_end:
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
    for item in row:
        no += 1
        img = item.find('img')['src']
        title = item.find('h3').text
        author = item.find('div', class_ = 'product-author').text.strip()
        binding = item.find('div', class_ = 'product-binding').text.strip()
        price = item.find('div', class_ = 'product-price').text.strip().replace(',' , '.')
        periplus_list.append({
            'no' : no,
            'img' : img,
            'title' : title,
            'author' : author,
            'binding' : binding,
            'price' : price,
        })
    print(page)
    page += 1
df = pd.DataFrame(periplus_list)
df.to_csv(f'data_csv/periplus_{no}.csv', index=False)
df.to_excel(f'data_excel/periplus_{no}.xlsx', index=False)
df.to_json(f'data_json/periplus_{no}.json', orient='records')
print('--- %s seconds ---' % (time.time() - start_time))