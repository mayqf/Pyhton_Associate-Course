print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")


liste=open("C:\\phyton\\liste.txt","r")#mevcut dosyayi actik
dosya_2=open("C:\\phyton\\dosya_2.txt","w")#islem sonuclarinin yazilacagi dosyalari actik
dosya_3=open("C:\\phyton\\dosya_3.txt","w")
liste_satirlar=liste.readlines()

for line in sorted(liste_satirlar):
      print(line)
for line in liste_satirlar:
      sorted.liste_satirlar
      print(line)

cevrim = {i: liste_satirlar.index(i) for i in liste_satirlar}

a=sorted(i+1, key=cevrim.get)
print(a)


            
liste.close()#dosyalari kapattik.
dosya_2.close()
dosya_3.close()

