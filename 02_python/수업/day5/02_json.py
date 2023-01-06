import json
from pprint import pprint
# with open('data/movie.json', 'r', encoding='UTF8') as f:
#     movie = json.load(f)
#     pprint(movie)
#     print(type(movie))
#     print(movie['title'])

with open('data/movies.json', 'r', encoding='UTF8') as f:
    movie = json.load(f)
    # pprint(movie)
    print(type(movie))
    # 각 리스트 요소?
    print(movie[0])

