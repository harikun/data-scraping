import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.yell.com/ucs/UcsSearchAction.do?'
site = 'https://www.yell.com'
params = {
 'scrambleSeed' : '544673055',
 'keywords' : 'indian restaurants',
 'location' : 'United Kingdom',
}
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

def get_total_pages():
    params = {
    'scrambleSeed' : '544673055',
    'keywords' : 'indian restaurants',
    'location' : 'United Kingdom',
    }
    res = requests.get(url, params=params, headers=headers)

    total_pages = []
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('div', {'class': 'col-sm-14 col-md-16 col-lg-14 text-center'})
    pages = pagination.find_all('a')
    for page in pages:
        total_pages.append(page.text)
    total = int(max(total_pages))
    return total

def get_all_items(page):
    params = {
    'scrambleSeed' : '544673055',
    'keywords' : 'indian restaurants',
    'location' : 'United Kingdom',
    'pageNum' : page
    }
    res = requests.get(url, params=params, headers=headers)
    headers_container = soup.find_all('div', {'class': 'row businessCapsule--mainRow'})

    data_list = []
    for content in headers_container:
        title = content.find('h2', {'class': 'businessCapsule--name text-h2'}).text
        classification = content.find('span', {'class': 'businessCapsule--classification'}).text
        try:
            ctas_web = content.find('a', {'class': 'btn btn-yellow businessCapsule--ctaItem'}).get('href')
        except:
            ctas_web = 'N/A'
        ctas_phone = content.find('span', {'class': 'business--telephoneNumber'}).text
        maps_link = site + content.find('a', {'class': 'col-sm-24 businessCapsule--address businessCapsule--link'}).get('href')
        try:
            opening_hours =  content.find('div', {'class': 'col-sm-24 businessCapsule--openingHours'}).text.strip("\n")
        except:
            opening_hours = 'N/A'
        address = content.find('span', {'itemprop': "address"}).text.strip("\n")
        rating = content.find('div', {'class': 'businessCapsule--ratings'}).text.strip("\n")
        try:
            services = content.find('div', {'class': 'col-sm-24 businessCapsule--services'}).text
        except:
            services = 'N/A'

        data_dict = {
            'title': title,
            'classification': classification,
            'ctas_web': ctas_web,
            'ctas_phone': ctas_phone,
            'maps_link': maps_link,
            'opening_hours': opening_hours,
            'address': address,
            'rating': rating,
            'services': services
        }
        data_list.append(data_dict)

    print(f'Data berhasil halaman ke-{page} berhasil di scraping')
    return data_list

def run():
    total = 9
    final_result = []
    for page in range(total):
        page += 1
        final_result += get_all_items(page)

    try:
       os.mkdir('data_json')
    except OSError:
        pass

    with open('data_json/yell.json', 'w+') as f:
        json.dump(final_result, f)
        f.close()
    print('Data berhasil di simpan di data_json/yell.json')
    print('Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')


if __name__ == '__main__':
    # get_total_pages()
    # get_all_items()
    run()