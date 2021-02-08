from urllib.request import urlopen
from bs4 import BeautifulSoup
import re  # biblioteca re que serve para trabalhar com expressões regulares e tratar as strings obtidas

url = urlopen("https://www.imdb.com/chart/top?ref_=nv_mv_250")

html = BeautifulSoup(url.read(),"html.parser")
contentRating = html.find_all("td", {"class": "imdbRating"})
contentTitleYear = html.find_all("td", {"class": "titleColumn"})
contentRating = html.find_all("td", {"class": "imdbRating"})
      
#Analisando a string obtida, criei essas expressões regulares para obter a informação do ano de lançamento sem os 
# parênteses e obter apenas a quantidade de votos dos usuário
 
regexMovieYear = re.compile('(\d{4})')
regexUserRating = re.compile('\ ((\d{1,3})((\,|\.)\d{1,3})*)')       

for cty, cr in zip(contentTitleYear, contentRating):        
    movieTitle = (cty.a).text
    movieYear = re.search(regexMovieYear, (cty.span).text)
    imdbRating = cr.strong.text
    userRating = re.search(regexUserRating, cr.strong['title'])
    print(movieTitle,movieYear.group(0),imdbRating,userRating.group(0))
