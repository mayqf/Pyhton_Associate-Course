import random

mermi_haznesi = range(7)


liste = ['1','2','3','4','5','6','7']

     



dongu = 1

print("""Rus ruleti oyununa hos geldin.

7 mermi kovanimizin oldugu bir silahimiz var.
Ve bu kovanlarin sadece birisinde mermi var.
Eger mermi olan kovan en ustteki hazneye gelirse
(sekildeki gibi) oyun disisin.

                         o
                       x   x
                      x     x
                       x   x
                    
Oyundan istedigin zaman cikabilirsin!""")

giris = input("ilk el atesine hazir misin?(evet,hayir): ")

if giris == "evet":


    while dongu == 1:

    

            b = random.choice(liste)

            if b == "6":
                print("OLDUN!! OYUN DISISIN")
                print("""
                         o
                       x   x
                      x     x
                       x   x
                       """)
                dongu = 10
                break


            elif b == "1":     
                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       o   x
                      x     x
                       x   x
                       """)

                else:
                    quit()
            

            elif b == "2":
                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       x   x
                      o     x
                       x   x
                       """)

                else:
                    quit()
            
            

            elif b == "3":

                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       x   x
                      x     x
                       o   x
                       """)

                else:
                    quit()
            

            elif b == "4":
                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       x   x
                      x     x
                       x   o
                       """)

                else:
                    quit()
            
            

            elif b == "5":
                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       x   x
                      x     o
                       x   x
                       """)

                else:
                    quit()
            

            elif b == "7":
                print("SANSLISIN BOS KOVAN")
                a = input("Devam edilsin mi(evet/hayir): ")
                if a == "evet":
                    print("BAAM")
                    print("""
                         x
                       x   o
                      x     x
                       x   x
                       """)

                else:
                    quit()


    
        

       
