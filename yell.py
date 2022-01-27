from concurrent.futures import process
from email import header
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
soup = BeautifulSoup(res.text, 'html.parser')

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

    contents = soup.find_all('div', {'class': 'row results--row results--capsuleList'})
    print(len(contents))

# scraping process
# 1. get the page number
# 2. get the page url
# 3. get the page content
# 4. get the page title
# 5. get the page price
# 6. get the page location
# 7. get the page rating
# 8. get the page review count
# 9. get the page image url
# 10. get the page description
# 11. get the page phone number
# 12. get the page website
# 13. get the page address
# 14. get the page hours
# 15. get the page categories
if __name__ == '__main__':
    # get_total_pages()
    get_all_items()
    # run()