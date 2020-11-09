import bs4
from bs4 import element
import requests

file=open('example.html')
lsoup= bs4.BeautifulSoup(file.read(), 'html.parser')
elem= lsoup.select('#author')
print(elem[0].get_text())

print('~~~~~~~ Extract H2 ~~~~~~~~~~')
res=requests.get('http://www.cs.cmu.edu/~pausch/')
#used for display error message if url not valid
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
#<Store list of all <h1> tags to element>
elements=soup.select('h1')
for item in elements:
    print(item)
    print(item.get_text())
    print()

print(soup.prettify())