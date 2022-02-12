import time
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
china = '1'; vietnam = '3'; korea = '4'
url = "http://www.bkipm.kkp.go.id/bkipmnew/upifn/index/"

def importir_terdaftar():
    res = requests.get(url + china)
    soup = BeautifulSoup(res.text, 'html.parser')

    table = soup.find('table')

    print(table)

importir_terdaftar()

print("--- %s seconds ---" % (time.time() - start_time))