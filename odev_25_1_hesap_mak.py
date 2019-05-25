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
bilgi = """
      Bu hesap makinesi ile sadece asagidaki islemleri yapabilirsiniz!

       SIMGE       ISLEM
      -------     --------

         +        toplama
         -        cıkarma
         *        carpma
         /        bolme
         **       us hesaplama
         %        mod hesaplama
         karekok  karekok hesaplama
      """
islem_listesi= "+,-,*,/,**,%,karekok" #Yapilabilecek islemler kumesini tanimladik


if  sys.version_info.major >=3: # Burada oncelikli olarak Python surum kontrolu yapacagiz.
      print(version_3)   
      kullanici_adi = input ("Kullanici adi: ")
      parola = input ("Parola: ") #Burada sizden hesap makinesine giris icin dogru kullanici adi ve parolayi girmeniz istenecektir.      
      if kullanici_adi == "mustafa" and parola=="1234" :
            print ("Hesap makinesine hosgeldiniz\n",bilgi)
            while True: # Hesap makinesinde islem devamliligi icin dongu olusturduk            

                  islem= input("Yapmak istediginiz islemi seciniz(Cikmak icin q ya basiniz)!")#burada oncelikle yapmak istediginiz islemin simgesini girmeniz gerekmektedir.
                  if islem in islem_listesi:                  
                        print(islem," islemini sectiniz!")
                        try:
                              sayi_1 = int(input("Ilk sayiyi giriniz:"))
                              sayi_2 = int(input("Ikinci sayiyi giriniz:"))
                              sonuc="{}{}{}=".format(sayi_1,islem,sayi_2)                  
                              if islem == "+" :
                                    print(sonuc,sayi_1+sayi_2)                              
                              elif islem == "-" :
                                    print(sonuc,sayi_1-sayi_2)
                              elif islem == "*" :
                                    print(sonuc,sayi_1*sayi_2)
                              elif islem == "**" :
                                    print(sonuc,sayi_1**sayi_2)                        
                              elif islem == "/" :
                                    try:
                                          print(sonuc,sayi_1/sayi_2)
                                    except ZeroDivisionError:#0 a bolunme hatasini tanimladik.
                                          print("Bir sayıyı 0'a bölemezsiniz!")
                              elif islem == "%" :
                                    try:
                                          print(sonuc,sayi_1%sayi_2)

                                    except ZeroDivisionError:
                                          print("Bir sayıyı 0'a bölemezsiniz!")
                              elif islem=="karekok": # karekok islemi secilmesi durumunda hata verilmesini istedim
                                    raise Exception("Bu programda simdilik karekok alamazsin")
                        except ValueError:# Sayi disinda girdi olmasi durumunda hata
                              print("Lütfen sadece sayı girin!")
                  elif islem=="q":
                        print("Cikis yapiliyor...")
                        break
                  else :
                        raise Exception ("Yanlis bir islem sectiniz, hesaplama yapilamaz!",bilgi)                     
                  
      else:
            print("Yanlis parola ya da kullanici")#Hesap makinesi yanlizca dogru kullanici adi ve parola ile kullabilirsiniz.
else:
      print(version_2) # Eger surumunuz 3 ise isleme devam edebileceksiniz.
      



