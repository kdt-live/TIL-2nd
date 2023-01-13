import requests

students = ['gunhee', 'mingi', 'hyunyoung', 'minji', 'yuyoung']

for name in students:
    URL = f'https://api.nationalize.io/?name={name}'
    response = requests.get(URL).json()
    # print(response)
    # print(response.get('country'))
    # print(response.get('country')[0])
    print(name, response.get('country')[0].get('country_id'))

