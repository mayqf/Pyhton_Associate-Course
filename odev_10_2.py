print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   PYHTON v.3.7.2                    #
#                   Yazan: Mustafa                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")

import random
b = 1
liste = []
liste1=[]
while b < 70:
    a = random.randrange(0,300)
    if a not in liste:
        liste +=[a]
        b+=1  

        
for i in liste:  
    
        a=min(liste)
        liste1+=[a]
        liste.remove(a)
print("Sirali liste(<)=",liste1,"\n"*3)

    

isimler=["ahmet", "mustafa", "ismail", "dilara", "can", "ece","aysegul","omer","aziz","fatih",
         "fatma","yahya","gulseren","arif","esra","seyma","huseyin","erdem","alperen","beyza"]
isimler1=[]      
for i in isimler:  
    
        a=min(isimler)
        isimler1+=[a]
        isimler.remove(a)
print("Sirali liste(<)=",isimler1)









