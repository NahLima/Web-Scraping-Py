from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re 
import csv

csvFileName = 'IMDBRatingTop250.csv'
regexMovieYear = re.compile('(\d{4})')
regexUserRating = re.compile('\ ((\d{1,3})((\,|\.)\d{1,3})*)')

try:
    url = urlopen("https://www.imdb.com/chart/top?ref_=nv_mv_250")
except HTTPError as error:
    print(error)
except URLError as error:
    print(error)
else:
    html = BeautifulSoup(url.read(),"html.parser")
    contentTitleYear = html.find_all("td", {"class": "titleColumn"})
    contentRating = html.find_all("td", {"class": "imdbRating"})
  
    with open(csvFileName, 'w') as csvfile:
        fileWriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(['TITLE', 'YEAR', 'IMDB RATING', 'USER RATINGS']) #HEADER 

        for cty, cr in zip(contentTitleYear, contentRating):        
            movieTitle = (cty.a).text
            movieYear = re.search(regexMovieYear, (cty.span).text)
            imdbRating = cr.strong.text
            userRating = re.search(regexUserRating, cr.strong['title'])
            fileWriter.writerow([movieTitle, movieYear.group(0), imdbRating, userRating.group(0)]) #CONTENT
            print(movieTitle,movieYear.group(0),imdbRating,userRating.group(0))
        print('Arquivo ', csvFileName, 'gerado com sucesso!')