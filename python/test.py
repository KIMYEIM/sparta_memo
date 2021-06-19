import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies :
    title = movie.select_one('td.title > div > a')
    point = movie.select_one('td.point')
    rank = movie.select_one('td:nth-child(1) > img')
    if title is not None :
        print(rank['alt'], title.text, point.text)