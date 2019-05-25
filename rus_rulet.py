print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")
print("""Rus ruleti oyununa hosgeldiniz!\n
Oyunda sirayla toplam 6 adet atis yapilacaktir!
Silahin 6 mermi haznesi vardir ve bir tanesinde mermi vardir.
Oyunu bilgisayara karsi oynayacaksiniz!
Atislari mermi hazne numarasini(1,2,3,4,5,6) secerek yapacaksiniz\n""")

hazne=["",
      "","",
      "","",
      ""]

print("""                (0)
             (1)   (2)
             (3)   (4)
                (5) 
                   \n""")
import random
sayac=0
liste=[0,1,2,3,4,5]

while sayac<6:
      try:         
      
            if sayac% 2 == 0:
                  secenek=int(input("Sira sizde,atis yapiniz:"))
                  if secenek==5:
                        print("Oldunuz!!!!!!!!!")
                        break
                  else:                        
                        liste.remove(secenek)
                        hazne[secenek]="X"
                        print("  ",hazne[:1],"\n",hazne[1:3],"\n",hazne[3:5],"\n","  ",hazne[5:],"\n"*2)
            else:
                  atis= random.choice(liste)
            
                  print("Sira bilgisayarda:",atis)            
                  if atis==5:
                        print("Oldum(Mermi 5'teymis), sen kazandin!!!!!")
                        break
                  else:                        
                        liste.remove(atis)
                        hazne[atis]="X"
                        print("  ",hazne[:1],"\n",hazne[1:3],"\n",hazne[3:5],"\n","  ",hazne[5:],"\n"*2)
            sayac+=1
            
      except ValueError:
            print("Boyle bir hazne yok\n")
            
      
      
            
