print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                 Yazan: Mustafa AYDAR                #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")
# Dort islemi(+,-,*,/) yapabilecek bir hesap makinesi olusturacagiz.
# Burada, sayilari ve yapilmasini istediginiz aritmetik islemi gireceksiniz.
Islem= input(" Lutfen yapilmasini istediginiz islemi giriniz!\n")
#Yapilmasini istediginiz aritmetik islemi girdikten sonra enter'a basiniz!
print("Isleminizin sonucu=",eval(Islem))
print("-->"*len("Isleminizin sonucu"),sep="",end="\n")
print("Bir sonraki isleme gecebilirsiniz...")
#Burada, eval fonksiyonu girilen sayilarin karakter dizi olarak algilanmasini engeller.
