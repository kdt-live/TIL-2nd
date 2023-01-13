import requests
import pprint
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'

while True:
response = requests.get(URL)
# print(response)
# print(type(response))
# print(dir(response))
data = response.json()

print(data.get('data').get('BTC').get('closing_price'))
