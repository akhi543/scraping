# scrap quizlet word lists
# prework: install requests, bs4 module

from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)
wtag = soup.select('.SetPageTerm-wordText > .TermText')
allw = [i.get_text().encode("utf-8") for i in wtag]


import re
# words from google sheet
a = """trite    sanction    intrepid    pernicious
hegemony    irrevocable dilettante  
ravenous    obsequious  poignant    winsome
arcane  tractable   inscrutable precipitous
munificent  resurgent   rescind haphazard
garrulous   constituent reverent    
prolific    tempered    myriad  
taciturn        pernicious  
sycophant       circumscribe    
sporadic        inimical    
subversive      inveterate  
        repudiate   """
a = re.sub('\n', ' ', a)
a = re.sub(' +', ' ', a)
b = a.split()
writtenw = b



remaining = [x for x in allw if x not in writtenw]
