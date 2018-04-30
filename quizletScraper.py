# scrap quizlet word lists
# prework: install has requests, bs4 module

from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)

wtag = soup.select('.SetPageTerm-wordText > .TermText')

w = [i.get_text() for i in w]
