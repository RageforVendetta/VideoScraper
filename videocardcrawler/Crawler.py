#import re
from bs4 import BeautifulSoup as bs
from PyQT.app import r
html = r.text
soup = bs(html,'html.parser')

#divs = soup.find(id="products-container")
myUL = soup.find("ul",{"class": "products"})
all_h2_elements = soup.find_all("h2")
for el in all_h2_elements:
    pass
    #print(el,end="\n")
price = soup.find_all("span",{"class":"price"})
for el in price:
    pass
    #print(el,end="\n")


childs = myUL.find_all('a')
print(childs)