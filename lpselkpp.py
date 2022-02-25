from wsgiref import headers
import requests; import time; from bs4 import BeautifulSoup; import pandas as pd; import json
url = 'https://lpse.lkpp.go.id/eproc4/dt/lelang?draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=false&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&authenticityToken=c6c9063e23221df93b5f1b6b605bf76dfb76dcd4&_=1645779351046'
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
            'Cache-Control': 'max-age=0',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Connection': 'keep-alive',
            'Cookie':'SPSE_SESSION=5c367223a498e9000bca485af7a472447ca3b20f-___AT=c6c9063e23221df93b5f1b6b605bf76dfb76dcd4&___TS=1645782048774&___ID=98f9f4ed-bd96-4a78-9e3a-56cd3a83397f; TS0162cd9f=01e621ef1de9371a5d9a5d26c01b79620c39a24b3c24783448f2d9287ab0095b67cbc087bf16a4f197134d390340409f2ce01a1984bf6a3ad84920834905c75f745fe5f97b2607eb45d66ff811a92d6d54bd9c9f36fa1560a3ef1ae970d548ef75af81e9a9c9ef9b0d056ca729a263ef8bdb14cdb07705f7c3e481ac053d7864c4bb9ff5a5bf57cbb650226e7ee1498cb9950a3ccb; f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=HGEJMBGAPGMNEICENKEBJPDDLGACEHHNNMJIEEEFEFLJAJPLDFMOMANFHPPMIGGLBLCDOICJFMDKNCEDGBCAKAPOCJALAHDDNHNDNDPAKFPCPKADBDPHMKGLBHHKAIAB; lkpp.go.id=!MO/kxHZFeIjvNSE3/oE9p1QQvaD2pftJLwHIXeLZsyR1Q08pSSpg3NHokX9n1vkcgmGkjJ6kEWoKwA==; f5avraaaaaaaaaaaaaaaa_session_=BAOKKOPOOEEFPKFAEBCCMNJDNDHEIFDIDGAAOFICKOBAEOCCFIJKJFFDJDAIPEEEGDODFGEANJFNPOENLILAFCJMCJCCCBHJBDOHIHFKBNJNOICNOJINFIGGIPHGKDKJ; TS00000000076=08d7571cd2ab280055eb130fdbc4a380cfbf35ed522ddd1302e585f02bb838e204c429af7240d4fbded5897d2e47850208b450088509d00000d80af171c28a6da9f2e02206d336fac5a488fdb45bd583a8856f280b6bc5196fe6a4cfd3bcacd037b14c06cb27753c036bc411601da986ead3a1752601841deee2429ba41c2f94fc9dbc20d08a9de2d2de244ee781ed22b5246467f7246a0121e6a826912a8e869fada8fe455c31ccf05590368e29c373f8ca530608af19b0ef102ea904c1006a02b1bb7ef40d8c879371d28c48eaa3dca7c92c1be8b2fdb37508a0f85fbeee4a3641b94053145924562d66c20e1db6be3f566d9d4214bdb8699e96adca332a978768a41176febd0c; TSPD_101_DID=08d7571cd2ab280055eb130fdbc4a380cfbf35ed522ddd1302e585f02bb838e204c429af7240d4fbded5897d2e47850208b4500885063800e2379f1df978c95b271d901fb057e31c33c51d81df34d3e9be744b6b80ca5f07787ff7b8dd8144f349bd79ad46482d4f1822fe10f46d2621; TS01f96abb=01e621ef1d9be511067459fd5ebc7e7cba194285ee75ef86c77dfa82febece34f7a9ec865fba893265becc9caca6a2c3e6c1f1eeb1d17c79f54621959b03c322936ec5ce1502f337781c2a7958ef7b33d00e773c64ce4d3febd1b43349d6402212c5cc6da66aa1037096ef66515b3d580f8f064f3d; TS942487d7027=08d7571cd2ab20003f4887091f794e6df559ba66caf2a5c78aa2114ab19197a6bd21cf006066156608ea1da59f11300096cc56eabbcee0ec566059c109f20204b0473578abce5d746daf9ad56fe386da6294dd91f8005998c3ae2ed31be4ab79',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'X-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 FKUA/website/41/website/Desktop',
            'Content-Type': 'application/json',
            'Host': 'lpse.lkpp.go.id',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'Pragma': 'no-cache',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            }
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.data)