import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com'
params = {
    'q': 'python developer',
    'l': 'United States',
    '_ga': '2.103645448.948588261.1643193635-35629996.1642520933'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
# https://www.indeed.com/jobs?q=Python+Developer&l=New+York+State&_ga=2.103645448.948588261.1643193635-35629996.1642520933
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

def get_total_pages():
    params = {
    'q': 'python developer',
    'l': 'United States',
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

def get_all_items():
    params = {
    'q': 'python developer',
    'l': 'United States',
    '_ga': '2.103645448.948588261.1643193635-35629996.1642520933'
    }
    res = requests.get(url, params=params, headers=headers)

    with open('temp/temp.html', 'w') as f:
        f.write(res.text)
        f.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    #Scraping process
    contents = soup.find_all('table', {'class': 'jobCard_mainContent big6_visualChanges'})
    print(contents)

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
    print('Jumlah Datanya adalah ', len(jobs_list))


if __name__ == '__main__':
    # get_total_pages()
    get_all_items()