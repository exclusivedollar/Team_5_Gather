import requests
from bs4 import BeautifulSoup

URL = "https://twitter.com/search?q=Eskom_SA&src=typed_query"
r = requests.get(URL)
print(r.text)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
