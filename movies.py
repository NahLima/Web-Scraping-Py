from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.imdb.com/chart/top?ref_=nv_mv_250")

html = BeautifulSoup(url.read(),"html.parser")
contentTitleYear = html.find_all("td", {"class": "titleColumn"}) 
    
for cty in contentTitleYear:        
    movieTitle = (cty.a).text
    movieYear = (cty.span).text
    print(movieTitle, '-', movieYear)


