import urllib.request # for downloading the dataset # handling the url\
from bs4 import BeautifulSoup # for parsing the html # handling the html\

import nltk # for nlp tasks\
nltk.download('stopwords') # for removing stopwords\
from nltk.corpus import stopwords # for removing stopwords\

#get the info from webSite 
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/data_science')
html = response.read()
# print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
# print(text)
tokens = [t for t in text.split()]
#print(tokens)

sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
        
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False) 