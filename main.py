import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com'
params = {
    'q': 'python developer',
    'l': 'United States',
    '_ga': '2.103645448.948588261.1643193635-35629996.1642520933'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

def get_total_pages(query, location):
    params = {
    'q': query,
    'l': location,
    '_ga': '2.103645448.948588261.1643193635-35629996.1642520933'
    }
    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
       pass

    with open('temp/temp.html', 'w') as f:
        f.write(res.text)
        f.close()

    # Scraping Step
    total_pages = []
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', {'class': 'pagination-list'})
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total

def get_all_items(query, location, start, page):
    params = {
    'q': query,
    'l': location,
    'start': start,
    '_ga': '2.103645448.948588261.1643193635-35629996.1642520933'
    }
    res = requests.get(url, params=params, headers=headers)

    with open('temp/temp.html', 'w') as f:
        f.write(res.text)
        f.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    #Scraping process
    contents = soup.find_all('table', {'class': 'jobCard_mainContent big6_visualChanges'})

    #pick item
    # * title
    # * company name
    # * company link
    # * company address

    jobs_list = []
    for item in contents:
        title =  item.find('h2', {'class': 'jobTitle'}).text
        company = item.find('span', {'class': 'companyName'})
        company_name = company.text
        try:
            company_link =  site + company.find('a')['href']
        except:
            company_link = 'N/A'

        # sorting data
        data_dict = {
         'title': title,
         'company name': company_name,
         'link': company_link
        }
        jobs_list.append(data_dict)
    #writing json file
    try:
        os.mkdir('data_json')
    except FileExistsError:
       pass
    with open(f'data_json/{query}_in_{location}_page_{page}.json', 'w+') as f:
        json.dump(jobs_list, f)
        f.close()
    print('Data berhasil di simpan di data_json/data.json')
    return jobs_list

def create_document(dataFrame, filename):
    try:
       os.mkdir('data_result')
    except FileExistsError:
       pass
    df = pd.DataFrame(dataFrame)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    df.to_excel(f'data_result/{filename}.xlsx', index=False)

    print(f'File {filename}.csv and {filename}.xlsx has been created')

def run():
    query = input('Masukkan kata kunci: ')
    location = input('Masukkan lokasi: ')

    total = get_total_pages(query, location)
    counter = 0

    final_result = []
    for page in range(total):
        page += 1
        counter += 10
        final_result += get_all_items(query, location, counter, page)

     # formating data
    try:
        os.mkdir('reports')
    except FileExistsError:
       pass

    with open(f'reports/{query}_in_{location}.json', 'w+') as f:
        json.dump(final_result, f)
        f.close()
    print('Data berhasil di simpan di reports')

    # create document
    create_document(final_result, f'{query}_in_{location}')

if __name__ == '__main__':
    # get_total_pages()
    # get_all_items()
    run()