from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 
import csv # arquivo

url = urlopen("https://www.imdb.com/chart/top?ref_=nv_mv_250")

html = BeautifulSoup(url.read(),"html.parser")
contentRating = html.find_all("td", {"class": "imdbRating"})
contentTitleYear = html.find_all("td", {"class": "titleColumn"})
contentRating = html.find_all("td", {"class": "imdbRating"})
      
regexMovieYear = re.compile('(\d{4})')
regexUserRating = re.compile('\ ((\d{1,3})((\,|\.)\d{1,3})*)') 

csvFileName = 'IMDBRatingTop250.csv'      

with open(csvFileName, 'w') as csvfile:
    #criando o arquivo csv com o delimitador
    fileWriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL) 
    #Escrevendo cabeçalho no arquivo
    fileWriter.writerow(['TITLE', 'YEAR', 'IMDB RATING', 'USER RATINGS']) 

    for cty, cr in zip(contentTitleYear, contentRating):
        #titulo do filme        
        movieTitle = (cty.a).text 

        #ano de lançamento, com regex para pegar o valor numerico
        movieYear = re.search(regexMovieYear, (cty.span).text) 

        #avaliação do IMDB
        imdbRating = cr.strong.text 

        #avaliações dos usuarios, com regex para pegar apenas valor numerico, excluindo o texto da string obtida.
        userRating = re.search(regexUserRating, cr.strong['title'])  

        #Com os valores salvo nas variaveis escrevo elas no arquivo
        fileWriter.writerow([movieTitle, movieYear.group(0), imdbRating, userRating.group(0)]) 
        
        # print(movieTitle,movieYear.group(0),imdbRating,userRating.group(0))
    print('Arquivo ', csvFileName, 'gerado com sucesso!')