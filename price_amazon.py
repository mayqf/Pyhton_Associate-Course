


import re
from urllib.request import urlopen
# size gerekli olan adres
website=urlopen("https://www.amazon.de/s?k=0190198770615")
htmltext=website.read().decode('utf-8')
# site icinde altin fiyatinin bulundugu alan
getinspect='<span class="a-size-base a-color-price s-price a-text-bold">EUR (.+?)</span>'
pattern=re.compile(getinspect)
price=re.findall(pattern,htmltext)
print(price)





