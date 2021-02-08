from urllib.request import urlopen  #urlopen é a responsável para baixar o html da url e depois criamos um objeto BeautifulSoup passando esse html no modo leitura
from bs4 import BeautifulSoup

page = urlopen("https://www.imdb.com/") 
ret = BeautifulSoup(page.read(),"html.parser")
print(ret.title.text) 


