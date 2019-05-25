print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")
print("""
Sayi tahmin etme oyununa hosgeldiniz!
1-1000 araliginda aklimdan bir sayi tutacagim ve
siz tahmin etmeye calisacaksiniz!
Eger sayiniz aklimdaki sayidan:
      -buyukse "Buyuk sayi girdiniz, Lutfen kucuk sayi giriniz!"
      -kucukse "Kucuk sayi girdiniz, Lutfen buyuk sayi giriniz!" diyecegim.
Boylece sayiyi tahmin edeceksiniz ve buna gore puan alacaksiniz!
Ornegin ilk seferde tahmin ederseniz 1000, 2. seferde 999, 3. seferde 998 seklinde puan alacaksiniz.)
""")


sefer=0
tutulan_sayi=365
girilen_sayi=1
if girilen_sayi>1000 and girilen_sayi<1:
      print("Aralik disi sayi...")
while tutulan_sayi!=girilen_sayi :
      sefer +=1
      Puan=1001-int(sefer)
      girilen_sayi = int(input("Lutfen bir sayi giriniz(Oyundan cikmak icin '00' basiniz):"))
      if girilen_sayi == 00:
            print("Programdan cikis yapiyorsunuz...")
            break            
      elif tutulan_sayi > girilen_sayi:
            print("{} sayisini girdiniz.".format(girilen_sayi), " Lutfen buyuk sayi giriniz!")
      elif tutulan_sayi < girilen_sayi:
            print("{} sayisini girdiniz.".format(girilen_sayi), " Lutfen kucuk sayi giriniz!")
      else:
            print("\n{} sayisini girdiniz.\n\nTebrikler sayiyi bildiniz!!!\n\nSayiyi {}. seferde tahmin ettiniz!\n\n".format(girilen_sayi, sefer),"{} puan aldiniz!!!".format(Puan),sep="")
            break
            
