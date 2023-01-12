import requests

print(requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json())