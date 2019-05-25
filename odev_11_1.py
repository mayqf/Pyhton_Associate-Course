print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")

import sys

version_2="Yapacaginiz islem bu surum ile yapilamaz!"
version_3="Python 3.7.2'ye hosgeldiniz!"

# Burada oncelikli olarak Python surum kontrolu yapacagiz.

if  sys.version_info.major >=3:
      print(version_3)
else:
      print(version_2)
      
# Eger surumunuz 3 ise isleme devam edebileceksiniz.
      
      
kullanici_adi = input ("Kullanici adi: ")
parola = input ("Parola: ")

#Burada sizden hesap makinesine giris icin dogru kullanici adi v parolayi girmeniz istenecektir.
if kullanici_adi == "mustafa" and parola=="1234" :
      print ("Hesap makinesine hosgeldiniz")
      
      bilgi = """
      Bu hesap makinesi ile sadece asagidaki islemleri yapabilirsiniz!

       SIMGE       ISLEM
      -------     --------

         +        toplama
         -        cıkarma
         *        carpma
         /        bolme
         **       us hesaplama
       karekok    karekok hesaplama
         %        mod hesaplama
      """
      print(bilgi)
      islem= input("Yapmak istediginiz islemi seciniz!")      
      print(islem," islemini sectiniz!")
      #burada oncelikle yapmak istediginiz islemin simgesini girmeniz gerekmektedir.
      
      if islem == "+" :
            sayi_1 = int(input("Ilk sayiyi giriniz:"))
            sayi_2 = int(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ",sayi_1,"+",sayi_2,"=",sayi_1+sayi_2)
      elif islem == "-" :
            sayi_1 = int(input("Ilk sayiyi giriniz:"))
            sayi_2 = int(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ","{} - {} = ".format(sayi_1,sayi_2),sayi_1-sayi_2)        

      elif islem == "*" :
            sayi_1 = int(input("Ilk sayiyi giriniz:"))
            sayi_2 = int(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ","{} * {} = ".format(sayi_1,sayi_2),sayi_1*sayi_2)
      elif islem == "/" :
            sayi_1 = float(input("Ilk sayiyi giriniz:"))
            sayi_2 = float(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ", "{} / {} = ".format(sayi_1,sayi_2),sayi_1/sayi_2)
      elif islem == "**" :
            sayi_1 = int(input("Ilk sayiyi giriniz:"))
            sayi_2 = int(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ",sayi_1,"**",sayi_2,"=",sayi_1**sayi_2)
      elif islem == "karekok" :
            sayi_1 = int(input("Sayi giriniz:"))            
            print("Sonuc= ",sayi_1,"**",0.5,"=",sayi_1**0.5)
      elif islem == "%" :
            sayi_1 = int(input("Ilk sayiyi giriniz:"))
            sayi_2 = int(input("Ikinci sayiyi giriniz:"))
            print("Sonuc= ",sayi_1,"%",sayi_2,"=",sayi_1%sayi_2)
      else :
            print("Yanlis bir islem sectiniz, hesaplama yapilamaz!\n",bilgi)
else:
      print("Yanlis parola ya da kullanici")
      
#Hesap makinesi yanlizca dogru kullanici adi ve parola ile kullabilirsiniz.


