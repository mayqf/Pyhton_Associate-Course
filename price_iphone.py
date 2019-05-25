import re
from urllib.request import urlopen

dosya=open("fiyat.txt","w")

def price_check(website_part,price_code):
      website=urlopen(website_part)# website adress
      htmltext=website.read().decode('utf-8')  
      pattern=re.compile(price_code)#iphone price from html
      price=re.findall(pattern,htmltext)
      return price


p_1=price_check("https://www.amazon.de/gp/product/B07HB4TJH1?ie=UTF8&ld=AZDESOAFooter",
                '<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">EUR (.+?)</span>')

p_2=price_check("https://www.bol.com/nl/p/apple-iphone-xr-64gb-zwart/9200000098453451/?language=en",
                '<span class="promo-price" data-test="price">(.+?) <sup class="promo-price__fraction  promo-price__fraction--dash" data-test="price-fraction">-</sup> </span>')
p_3=price_check("https://www.mediamarkt.nl/nl/product/_apple-iphone-xr-64gb-zwart-1591546.html?ga_query=0190198770615",'<meta property="product:price:amount" content="(.+?)"/>')
p_4=price_check("https://www.phonemarket.nl/Apple%20iPhone%20XS%2064GB%20DualSim%20Grijs",'<span itemprop="price" id="price-old">€  (.+?)<sup>,-</sup></span>')



price_full={}
price_full["amazon.com price(€)"]=p_1[0]
price_full["bol.com price(€)"]=p_2[0]
price_full["mediamarkt.nl price(€)"]=p_3[0]
price_full["phonemarket.nl price(€)"]=p_4[0]

for i,j in price_full.items():
      print("{} = {}".format(i, j))
      #dosya.write(i)
      #dosya.write("\n")
      #dosya.write(j)
      #dosya.write("\n")
      

dosya.close()
