import requests
from bs4 import BeautifulSoup

url="http://quickxpertinfotech.com/"
r = requests.get(url)
htmlContent=r.content
print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
title=soup.title
# print(title)
para=soup.find_all('p')
#print(para)
anchor=soup.find_all('a')
#print(anchor)

print(soup.find('p')['class'])
all_links = set()
for link in anchor:
    if(link != '#'):
        link = "http://quickxpertinfotech.com/"+link.get('href')
        all_links.add(link)
        print(link)