import requests
import json

url = 'https://www.instagram.com/graphql/query'
variables = {
 "shortcode":"CZRax8PlDEW",
 "include_reel":True,
 "first":24
}
query_hash =  'd5d763b1e2acf209d62d22d184488e57'
params = {
   'query_hash': query_hash,
   'variables': json.dumps(variables)
}

res = requests.get(url, params=params).json()
print(res)
# users = res['data']['shortcode_media']['edge_liked_by']['edges']
# for user in users:
#     username = user['node']['username']
#     print(username)