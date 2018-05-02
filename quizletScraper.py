# scrap quizlet word lists
# prework: install requests, bs4 module

from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)
wtag = soup.select('.SetPageTerm-wordText > .TermText')
allw = [i.get_text().encode("utf-8").lower() for i in wtag]


import re
# words from google sheet
a = """
deleterious	jovial	droit
polemic	transient	nonplussed
maladroit	rebuke	dilatory
dispassionate	impartial	sullen
furtive	stringent	flux
mendacity	economical	capricious
elicit	appease	polemic
erudite	disseminate	edifying
posit		indecorous
duress		placate
ignominious		esoteric
pejorative - disapprove		efficacious
reproach		opulence
bolster		
banality		
askance		
maverick		
		
"""
a = re.sub('\n', ' ', a)
a = re.sub(' +', ' ', a)
b = a.split()
b = [i.lower() for i in b]
writtenw = b



remaining = [x for x in allw if x not in writtenw]
