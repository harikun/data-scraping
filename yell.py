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

def get_total_pages():
    params = {
    'scrambleSeed' : '544673055',
    'keywords' : 'indian restaurants',
    'location' : 'United Kingdom',
    }
    res = requests.get(url, params=params, headers=headers)

    # Scraping Step
    total_pages = []
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('div', {'class': 'col-sm-14 col-md-16 col-lg-14 text-center'})
    pages = pagination.find_all('a')
    for page in pages:
        total_pages.append(page.text)
    total = int(max(total_pages))
    print(total + 1)
    return total

def get_all_items():
    params = {
    'scrambleSeed' : '544673055',
    'keywords' : 'indian restaurants',
    'location' : 'United Kingdom',
    }
    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Scraping Process
    headers_container = soup.find_all('div', {'class': 'row businessCapsule--mainRow'})

    for content in headers_container:
        title = content.find('h2', {'class': 'businessCapsule--name text-h2'}).text
        print(title)
  # pick item #
  # * title
  # * classification
  # * ctas (call to action)
    # * website
    # * phone
  # * maps link
  # * opening hours
  # * address
  # * rating
    # * reviews link
    # * rating average
    # * rating total
 # * services

if __name__ == '__main__':
    # get_total_pages()
    get_all_items()
    # run()