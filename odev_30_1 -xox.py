print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")
print("X/O olmayi belirleyecegiz. Bunun icin yazi-tura atacagiz.(Y/T)")

a= input("Yazi mi tura mi")
a=a.upper()
if a=="Y":
      print("X oldunuz")
elif a=="T":
      print("O oldunuz")
print("XOX oyununa hosgeldiniz")
print("""Yatay,dikey ya da capraz olarak 3'luyu tamamlamalisiniz!
      X,X,X
      X,X,X
      X,X,X
                """)

tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

for i in tahta:
      print(*i,"\n")
      
kazanma_matris1 = ['0','1','2']
kazanma_matris2 = ("3,4,5")
kazanma_matris3 = ("648")
kazanma_matris4 = ("036")
kazanma_matris5 = ("147")
kazanma_matris6 = ("258")
kazanma_matris7 = ("048")
kazanma_matris8 = ("246")



print ("Bu sekilde varyasyonlardan biri kazanir!\n")
print("""            (0, 1, 2)
            (3, 4, 5)
            (6, 7, 8)
            (0, 3, 6)
            (1, 4, 7)
            (2, 5, 8)
            (0, 4, 8)
            (2, 4, 6)
                        """)
kume=(0,1,2,3,4,5,6,7,8)
kume_1=[]
kume_2= []

while True:           
      sayi1=input("""Kume seklimiz:
               0,1,2
               3,4,5
               6,7,8\nX! gireceginiz yeri seciniz\n>>""")
      #sayi1=int(sayi1)
      print([sayi1],"konumunu sectiniz")
      kume_1+=sayi1
      print("kume_1:",kume_1)
      print(tahta[0])
      sayi2=input("""Kume seklimiz:
               0,1,2
               3,4,5
               6,7,8\nO! gireceginiz yeri seciniz\n>>""")
      if sayi2!=sayi1:
            print([sayi2],"konumunu sectiniz")
      
            kume_2+=sayi2
      
      
            print("kume_2:",kume_2)
      else:
            print("konum dolu")
      if kazanma_matris1 in kume_1:
            print("kazandiniz")
      
      
      
