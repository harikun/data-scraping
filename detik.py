import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
# params = 'ippd=www.detik.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

res = requests.get(url, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

#Scraping process
contents = soup.find('div', {'class': 'grid-row list-content'})
# print(contents)

#pick item
 # * News title
 # * News link
 # * News Time
 # * News Image

titles = contents.find_all('a', {'class': 'media__link'})
images = contents.find_all('div', {'class': 'media__image'})
dates = contents.find_all('div', {'class': 'media__date'})

for title in titles:
    print(title.text)
# data_dict = {
#  'title': titles
# }
# Sorting the data
# for title in titles:
#     print(title.text)
# for image in images:
#     print(image.img['src'])
#     print(image.a['href'])
# for date in dates:
#     print(date.span['title'])