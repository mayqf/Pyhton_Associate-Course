print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")

tahta=["-","-","-","-","-","-","-","-","-"]

print("""            (0)(1)(2)
            (3)(4)(5)
            (6)(7)(8)\n""")

print("""XOX oyununda yapacaginiz hamleyi; yukaridaki numaralari secerek gireceksiniz.\n""")

print("""Yatay,dikey ya da capraz olarak 3'luyu tamamlamalisiniz!\n
      X,X,X
      X,X,X
      X,X,X
                """)
#kullaniciya 0,1,2,3,,4,5,6,7,8 ile secim yapabilecgi yerleri doldurt!
sayac=0
xListesi=[]
oListesi=[]
win_combinations1=[0,1,2]
win_combinations2=[3,4,5]
win_combinations3=[6,7,8]
win_combinations4=[0,3,6]
win_combinations5=[1,4,7]
win_combinations6=[2,5,8]
win_combinations7=[0,4,8]
win_combinations8=[2,4,6]
while sayac<=8:
    if sayac % 2 == 0:# birinci kisinin sirasi icin 
        isaret = "X"
    else:
        isaret = "O"
    print("OYUNCU: {}\n".format(isaret))
    try:
        yer=input("Hamleniz:")
        yer=int(yer)        
        if tahta[yer]=="X" or tahta[yer]=="O":
                print ("Yer dolu...")
        else:
                tahta[yer]= isaret
                sayac += 1            
                print("\t",tahta[:3],"\n","\t",tahta[3:6],"\n","\t",tahta[6:9])
                if isaret == "X":                
                    xListesi += [yer]
                    xListesi.sort()
                    x1=[i for i in xListesi if i in win_combinations1]
                    x2=[i for i in xListesi if i in win_combinations2]
                    x3=[i for i in xListesi if i in win_combinations3]
                    x4=[i for i in xListesi if i in win_combinations4]
                    x5=[i for i in xListesi if i in win_combinations5]
                    x6=[i for i in xListesi if i in win_combinations6]
                    x7=[i for i in xListesi if i in win_combinations7]
                    x8=[i for i in xListesi if i in win_combinations8]                               
                    if x1==win_combinations1:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x2==win_combinations2:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x3==win_combinations3:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x4==win_combinations4:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x5==win_combinations5:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x6==win_combinations6:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x7==win_combinations7:
                       print("Tebrikler...","\a" * 10)
                       break
                    elif x8==win_combinations8:
                       print("Tebrikler...","\a" * 10)
                       break
                elif isaret == "O":
                   oListesi += [yer]
                   oListesi.sort()
                   y1=[i for i in oListesi if i in win_combinations1]
                   y2=[i for i in oListesi if i in win_combinations2]
                   y3=[i for i in oListesi if i in win_combinations3]
                   y4=[i for i in oListesi if i in win_combinations4]
                   y5=[i for i in oListesi if i in win_combinations5]
                   y6=[i for i in oListesi if i in win_combinations6]
                   y7=[i for i in oListesi if i in win_combinations7]
                   y8=[i for i in oListesi if i in win_combinations8]
                   if y1==win_combinations1:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y2==win_combinations2:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y3==win_combinations3:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y4==win_combinations4:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y5==win_combinations5:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y6==win_combinations6:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y7==win_combinations7:
                       print("Tebrikler...","\a" * 10)
                       break
                   elif y8==win_combinations8:
                       print("Tebrikler...","\a" * 10)
                       break                
    except ValueError:
        print("Lütfen sadece sayı giriniz!\n")        
    except IndexError:
        print("0-8 araliginda sayi giriniz!\n")
if sayac==9:
    print("Berabere...")


