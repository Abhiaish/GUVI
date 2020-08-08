import requests
wiki_link="https://www.onlinesbiglobal.com/64GBweb/index.htm"
link=requests.get(wiki_link).text
from bs4 import BeautifulSoup
soup=BeautifulSoup(link,"lxml")
print(soup.prettify())
print(soup.title)
print(soup.a)
print(soup.title.string)
all_link=soup.find_all("a")
for link in all_link:
    print(link.get("href"))
all_tables=soup.find_all('table')
    
