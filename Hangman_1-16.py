print("""
        #######################################################
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #                   PYHTON v.3.7.2                    #
        #                   Yazan: Mustafa                    #
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #######################################################


                        H   A   N   G   M   A   N
                        

                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
****************                                       +                  ##
*  BEGINNER    *                                   /+++++++\              ##
*--------------*                                  / +  H  + \             ##
* INTERMEDIATE *                                =/  +  H  +  \=           ##
*--------------*                                    +++++++               ##
*  ADVANCED    *                                     +   +                ##
****************                                     +   +                ##
                                                     +   +                ##
                                                     +   +                ##
                                                     +   +                ##
                                                   +++   +++              ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================

Welcome to Hangman game!!!\n
We have 3 three different levels(Beginner,Indermediate and Advanced) and
languages(Turkish,English and Dutch).
Firstly you should choose levels and language.
""") # Here we firstly designed welcome page.

print("Lutfen dili seciniz\ Please select language\Alstublieft taal)")
language=['Turkce','English','Nederlands']
language=input("Lutfen dili seciniz\ Please select language\Alstublieft taal):")
level= ['Baslangic','Orta','Zor','Beginner','Indermediate','Advanced','Beginner2','Indermediate2','Advanced2']
kelime_1='kus'
kelime_2='agac'
kelime_3='gokyuzu'

if language== 'Turkce' :
      print("Adam  Asma Oyununa hosgeldiniz!")
      level= input("Lutfen zorluk derecesini seciniz:")
      if level=='Baslangic':
            print('Haydi baslayalim, 3 harfli bir kelime')
            while kelime==kelime_1:
                  harf= input("Lutfen harf giriniz:"
                              if harf in kelime_1:
                                    print ('Tebrikler, devam edin')
                                    break
            else:
                                    print("tekrar deneyin")
                                
                  
      elif level=='Orta':
            print('Haydi baslayalim2')
      elif level=='Zor':
            print('Haydi baslayalim3')
elif language== 'English' :
      print("Welcome to Hangman game,Please select game level and category!")
      level= input("Please select level:")
      if level=='Beginner':
            print('Haydi baslayalim4')
      elif level=='Intermediate':
            print('Haydi baslayalim5')
      elif level=='Advanced':
            print('Haydi baslayalim6')
else:
      print("Ned-Welcome to Hangman game,Please select game level and category!")
      level= input("Selecteer level:")
      if level=='Beginner2':
            print('Haydi baslayalim7')
      elif level=='Intermediate2':
            print('Haydi baslayalim8')
      elif level=='Advanced2':
            print('Haydi baslayalim9')
      

