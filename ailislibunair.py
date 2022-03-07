import requests; import pandas as pd; from bs4 import BeautifulSoup;
page = 1; max_page = 2; buku_perpus_unair = []; no = 0
while page <= max_page:
    res = requests.get(f'http://ailis.lib.unair.ac.id/opac/pencarian-sederhana?action=pencarianSederhana&katakunci=&ruas=Semua+Ruas&bahan=Semua+Jenis+Bahan&fAuthor=&fPublisher=&fPublishLoc=&fPublishYear=&page={str(page)}&limit=10&location=Perpustakaan+Pusat')
    soup = BeautifulSoup(res.text, 'html.parser')
    body = soup.find('body', class_='skin-blue layout-top-nav')
    wrapper = body.find('div', class_='wrapper')
    content_wrapper = wrapper.find('div', class_='content-wrapper')
    container = content_wrapper.find('div', class_='container')
    content = container.find('section', class_='content')
    box_box_default = content.find('div', class_='box box-default')
    content2 = box_box_default.find('section', class_='content')
    box_box_default2 = content2.find('div', class_='box box-default')
    box_body = box_box_default2.find('div', class_='box-body')
    row2 = box_body.find('div', class_='row').find_next_sibling('div', class_='row')
    col_sm_9 = row2.find('div', class_='col-sm-9')
    print(col_sm_9)
    page += 1