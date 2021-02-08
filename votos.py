from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.imdb.com/chart/top?ref_=nv_mv_250")

html = BeautifulSoup(url.read(),"html.parser")
contentRating = html.find_all("td", {"class": "imdbRating"})
      
for cr in contentRating:            
    print(cr.strong['title'])