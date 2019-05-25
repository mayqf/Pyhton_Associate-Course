import re
from urllib.request import urlopen
import time
url = "https://www.ebay.com/itm/WOMENS-Nike-Air-Force-1-07-MTLC-GOLD-Sneakers-AR0642-001-Size-5-5/123716122189?epid=18030931495&hash=item1cce0e364d:g:C3gAAOSw9PZcnXwo"
url1 = "https://www.ebay.com/itm/NIKE-AIR-FORCE-1-LOW-LOVE-WHITE-BRIGHT-CRIMSON-AR5432-167-WMNS-SZ-5-5/372643412523?epid=26027554869&hash=item56c3473a2b:g:7u8AAOSwHPdcJtkr"
url2= "https://www.ebay.com/itm/New-Womens-Nike-Air-Force-1-Sage-Low-LX-Shoe-Size-7-5-Phantom-White-AR5409-001/323784366994?epid=23030128880&hash=item4b630d5b92:g:yE8AAOSwuXxcs-FA"
url3="https://www.ebay.com/itm/Nike-WMNS-Air-Force-1-HI-LX-Just-Do-It-Grey-White-AO5138-100-Womens-Shoes-NIB/123219999241?var=&hash=item1cb07bfa09&enc=AQADAAADAFjVrDbVsZ8oH%2F8PNHtt9VX4%2Fw7FZcmMuqsX8uaFEduVnPXSAzUPKu3lu1vMCbsZw%2BU46HIfa%2BKHEuqGSxldpAj1YPl%2BOFd9gz%2F1RVg%2B7lIPiQODTB7QolI%2BLWZ6ywzfXnv25jTi3TV5hOM8NmU3X%2F9N1R6ei5cHzwzZplYKRaVLJ8Yb%2BL748uf0NCRMnad5uRJctNo8iaXfWMTbl%2BhdlNtcXTUCmppfPnGyX%2BnnrF0vbsSV0Gn2RfifKT3OT%2BjJN11H15hqlLJxJ7TBlBaHm%2B6D37%2FtlKhIl36co%2BJXBM%2BGUSPuSmKkRukQH3E2yZC8kUdTq%2B%2Bt%2B9CntAR%2Bkr3%2FfzAm4oQcjNjbulNnQxNttw7310D4MzfF77g0ndtGuvtD5aAXpkwWlgak1ZqXVrhJuH65LcioujAuNCfAkIGD45gVzuf3j5Gb%2FYA5Bt8vzfT4jvRbkXT3UswPtHowaihCqqzfTW%2BdvqZTB%2FedunFMEdz21jEBNAtIbvRuXbhttY5wLuPjEF7ny3U6%2BbNDpMocEtn9p5OZFxaWnSrW6PnaOc3BsTQIeI0R6yowSgOREWCevmSNrAGX4ai5hU3i1bYk%2Fg11HT9YS5Njhvl5yFtYlWtf3bj38ShD49ecKGnGonC6NrdxUndPSvZUnyLborVnCknEugSF%2BJV7O4GQlI4L4ujJZ2C4WsDnVbNbFfMJjzHq5bg6ntCnc%2FrXzYwIgn9wdPaacLKjMDaRtVkxg88KGPCFxreyseuHGSusM04rUI%2Bamacv3k2w6OZgZywNl4FaNLYMGL3pjUNhHUITmDikqCYQNsUz%2FvjA2QdAWv90zPU4THDTH0hMBGzMdqu5OMibUSg01jkzcoGKrgUE9Kts25ucZpGRXrrO5zmKQjLrnsqS9OeHA9s0ZTwOAbZnXxS%2FQf%2BrKBUopBsWB4%2BExdgh8GDw1S0CtbPXFLyoprNbprgeskzEswxtdEDK5qKELNtjQERnh9Dd%2BUJRIyOhkdTaAC7yCGeDweSnP86lFyo04M%2FcuQ%3D%3D&checksum=12321999924142b2d4a9a50c426fba5b629c08a87c5d"

f = urlopen(url)
f1 = urlopen(url)
f2 = urlopen(url)
f3 = urlopen(url)
dosya =open("fiyatlar.txt",'w+')


for i in f:
     product= re.search("[0-9]+$", i)
     if product:
         dosya.write("Site ; Ebay",product.group())

for i in f1:
    product1 = re.search("[0-9]+$", i)
    if product1:
        dosya.write("Site ; Ebay", product1.group())

for i in f2:
    product2 = re.search("[0-9]+$", i)
    if product2:
        dosya.write("Site ; Ebay", product2.group())

for i in f3:
    product3 = re.search("[0-9]+$", i)
    if product3:
        dosya.write("Site ; Ebay", product3.group())


