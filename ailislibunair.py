import requests; import pandas as pd; from bs4 import BeautifulSoup;
page = 1; max_page = 2; buku_perpus_unair = []; no = 0
while page < max_page:
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
    form = col_sm_9.find('form')
    table = form.find('table', class_='table2 table-striped')
    tr = table.find_all('tr')
    for td in tr:
        row = td.find_all('div', class_='row')
        for data in row[:1]:
            no += 1
            title = data.find('div', class_='col-sm-9').find('a').text
            link = data.find('div', class_='col-sm-9').find('a').get('href')
            material_type = data.find('div', class_='col-sm-9').find('td',{'width': "78%"}).text
            publisher = data.find('div', class_='col-sm-9').find('td',{'valign': 'top'}).find_next_sibling('td').text.strip()
            availability = data.find('div', class_='col-sm-9').find('a', {'data-toggle':'collapse'}).text
            print(no, title, availability)
            buku_perpus_unair.append({
                'no': no,
                'link': link,
                'material_type': material_type,
                'publisher': publisher,
                'availability': availability
                'title': title,
            })
    page += 1
df = pd.DataFrame(buku_perpus_unair)
df.to_csv(f'data_csv/buku_perpus_unair-{no}.csv', index=False)
df.to_excel(f'data_excel/buku_perpus_unair-{no}.xlsx', index=False)
df.to_json(f'data_json/buku_perpus_unair-{no}.json', orient='records')

print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')