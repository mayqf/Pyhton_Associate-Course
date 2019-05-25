print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")


a=open("C:\\phyton\\a.txt","r")#mevcut dosyayi actik
b=open("C:\\phyton\\b.txt","w")#islem sonuclarinin yazilacagi dosyalari actik


liste_satirlar=a.readlines()
#liste_satirlar= liste_satirlar.split(" ")

sayac=0
kodlama="utf-8"
welcome = open("welcome.html", "w", encoding=kodlama)
icerik = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset={0}" />
<title></title>
</head>
<body>
<h1>mustafa.com web sitesine hos geldiniz!!!!!!</h1>
<p><b></b></p>
</body>
</html>"""

kul_adi=input("kullanici adi:")
sifre=input("sifre:")

for i in liste_satirlar:
      liste_satirlar1=list(i.split(" "))
      
      for z in liste_satirlar1:
            if kul_adi==z[0:8] and sifre==z[9:12]:
                  print("Kullanici adi ve sifre dogru!!!")
            else:                  
                  sayac+=1

if sayac==5:
      print("kullanici adi:{} sifre:{} girdiniz".format(kul_adi,sifre),file=b)
else:
      print(icerik, file=welcome)
      
      
a.close()
b.close()
welcome.close()
