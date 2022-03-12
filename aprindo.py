import time; import requests; from bs4 import BeautifulSoup
start_time = time.time()
url = 'https://www.aprindo.org/profil-aprindo/'
def download_logo():
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    td_outer_wrap = soup.find('div', {'id': 'td-outer-wrap'})
    td_main_content_wrap = td_outer_wrap.find('div', {'class': 'td-main-content-wrap'})
    td_container = td_main_content_wrap.find('div', {'class': 'td-container'})
    td_pb_row = td_container.find('div', {'class': 'td-pb-row'})
    td_main_content = td_pb_row.find('div', {'class': 'td-main-content'})
    td_ss_main_content = td_main_content.find('div', {'class': 'td-ss-main-content'})
    td_page_content = td_ss_main_content.find('div', {'class': 'td-page-content'})
    p_5 = td_page_content.find('p').findNextSibling().findNextSibling().findNextSibling().findNextSibling()
    for img in p_5.find_all('img'):
        img_src = img['src']
        img_name = img_src.split('/')[-1]
        img_res = requests.get(img_src)
        with open(f'data_image/aprindo/{img_name}', 'wb') as f:
            f.write(img_res.content)
            f.close()
download_logo()
print("--- %s seconds ---" % (time.time() - start_time))
print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')