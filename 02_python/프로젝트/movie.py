# 반드시 터미널에서 
# pip install requests
import requests

# https://developers.themoviedb.org/3/movies/get-popular-movies
# https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
# https://api.themoviedb.org/3/movie/2846?api_key=8854669b886a6c07c12ea947bcc2311d

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular' # API 문서에서 적절하게 구성
params = { # 그 문서에서 필요한 params 정의
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'language': 'ko-KR',
    'region': 'KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)
print(response.get('results')[0])