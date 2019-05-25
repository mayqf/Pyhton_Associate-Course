
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
                                                       =========================\n\n\n""")
# Burada yanlis cevap asamalarinda cikacak resimleri tasarladik.
resim_1=(""" 
                        

                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")
resim_2=("""     
                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                    +++++++               ##
                                                    +  H  +               ##
                                                    +  H  +               ##
                                                    +++++++               ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")
resim_3=("""
                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                    +++++++\              ##
                                                    +  H  + \             ##
                                                    +  H  +  \=           ##
                                                    +++++++               ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")
resim_4=("""
                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                   /+++++++\              ##
                                                  / +  H  + \             ##
                                                =/  +  H  +  \=           ##
                                                    +++++++               ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")
resim_5=("""
                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                   /+++++++\              ##
                                                  / +  H  + \             ##
                                                =/  +  H  +  \=           ##
                                                    +++++++               ##
                                                         +                ##
                                                         +                ##
                                                         +                ##
                                                         +                ##
                                                         +                ##
                                                         +++              ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")
resim_6=("""
                                                       #####################
                                                       #                  ##
                                                       #                  ##
                                                       +                  ##
                                                     +   +                ##
                                                       +                  ##
                                                   /+++++++\              ##
                                                  / +  H  + \             ##
                                                =/  +  H  +  \=           ##
                                                    +++++++               ##
                                                     +   +                ##
                                                     +   +                ##
                                                     +   +                ##
                                                     +   +                ##
                                                     +   +                ##
                                                   +++   +++              ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                                          ##
                                                       =========================
                                                       =========================""")

print('Welcome to Hangman game!!!\n\n',"Oyunumuz 3 level'dir(beginner,intermediate,advanced)\n\n","Kelimeyi tahmin icin; sirasiyla 2,4,6'sar hakkiniz vardir!\n",sep="")

kelime='marti'
print('Haydi baslayalim, kelimemiz', len(kelime), 'harflidir.\n')

deneme=0
level=input('Lutfen seviye giriniz(beginner,intermediate,advanced):\t')
if level=='advanced':
      while deneme<2:
            harf=input('Bir harf ya da kelimeyi giriniz:\t')
            if harf in kelime:
                  if harf=='m':
                        print('{} harfi'.format(harf),'1. siradadir.\n')
            
                  elif harf=='a':
                        print('{} harfi'.format(harf),'2. siradadir.\n')
            
                  elif harf=='r':
                        print('{} harfi'.format(harf),'3. siradadir.\n')
            
                  elif harf=='t':
                        print('{} harfi'.format(harf),'4. siradadir.\n')
            
                  elif harf=='i':
                        print('{} harfi'.format(harf),'5. siradadir.\n')                  
                  elif kelime==harf:
                        print('Tebrikler bildiniz!!!')
                        break
            elif harf not in kelime:
                  deneme+=1
                  if deneme==1:
                        print('Yanlis harf!\n',resim_4,)
                        print('!!!!!SON HAKKINIZ!!!!!\n')
                  elif deneme==2:
                        print(resim_6)
                        print("!!!!!!!!!!Maalesef kaybettiniz!!!!!!!!!!")
            
            elif kelime==harf:
                  print('Tebrikler bildiniz!!!')
                  break
if level=='intermediate':
      while deneme<4:
            harf=input('Bir harf ya da kelimeyi giriniz:\t')
            if harf in kelime:
                  if harf=='m':
                        print('{} harfi'.format(harf),'1. siradadir.\n')
            
                  elif harf=='a':
                        print('{} harfi'.format(harf),'2. siradadir.\n')
            
                  elif harf=='r':
                        print('{} harfi'.format(harf),'3. siradadir.\n')
            
                  elif harf=='t':
                        print('{} harfi'.format(harf),'4. siradadir.\n')
            
                  elif harf=='i':
                        print('{} harfi'.format(harf),'5. siradadir.\n')                  
                  elif kelime==harf:
                        print('Tebrikler bildiniz!!!')
                        break
            elif harf not in kelime:
                  deneme+=1
                  if deneme==1:
                        print('Yanlis harf',resim_1)
                  elif deneme==2:
                        print('Yanlis harf',resim_3)
                  elif deneme==3:
                        print('Yanlis harf',resim_4)
                        print('!!!!!SON HAKKINIZ!!!!!\n')
                  elif deneme==4:
                        print(resim_6)
                        print("!!!!!!!!!!Maalesef kaybettiniz!!!!!!!!!!")
            
            elif kelime==harf:
                  print('Tebrikler bildiniz!!!')
                  break
      
if level=='beginner':
      while deneme<6:
            harf=input('Bir harf giriniz kelimeyi giriniz:\t')
            if harf in kelime:
                  if harf=='m':
                        print('{} harfi'.format(harf),'1. siradadir.\n')
            
                  elif harf=='a':
                        print('{} harfi'.format(harf),'2. siradadir.\n')
            
                  elif harf=='r':
                        print('{} harfi'.format(harf),'3. siradadir.\n')
            
                  elif harf=='t':
                        print('{} harfi'.format(harf),'4. siradadir.\n')
            
                  elif harf=='i':
                        print('{} harfi'.format(harf),'5. siradadir.\n')                  
                  elif kelime==harf:
                        print('Tebrikler bildiniz!!!')
                        break
            elif harf not in kelime:
                  deneme+=1
                  if deneme==1:
                        print('Yanlis harf',resim_1)
                  if deneme==2:
                        print('Yanlis harf',resim_2)
                  if deneme==3:
                        print('Yanlis harf',resim_3)
                  if deneme==4:
                        print('Yanlis harf',resim_4)
                  if deneme==5:
                        print('Yanlis harf',resim_5)
                        print('!!!!!SON HAKKINIZ!!!!!\n')
                  elif deneme==6:
                        print(resim_6)
                        print("!!!!!!!!!!Maalesef kaybettiniz!!!!!!!!!!")
            
            elif kelime==harf:
                  print('Tebrikler bildiniz!!!')
                  break      
   
