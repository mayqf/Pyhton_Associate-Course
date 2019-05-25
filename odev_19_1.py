a= open("a.txt") # varolan a ve b dosyalarini acmak icin
a_satirlar = a.readlines() # satır-satir okuyoruz
b= open("b.txt")
b_satirlar = b.readlines()

fark_1=open("C:\\phyton\\fark.txt", "w")#fark ve c isimli 2 yeni dosya actik
c_1=open("C:\\phyton\\c.txt", "w")

print("a_eleman_sayisi= ",len(a_satirlar))
print("b_eleman_sayisi= ",len(b_satirlar))

fark = ""
c= ""

for isim in a_satirlar:
      if not isim in b_satirlar:
            if not isim in fark:
                  fark +=isim
                  fark_1.write(isim)#fark ve c isimli dosyalara yazdirmak icin
      else:
            if not isim in c:
                  c +=isim
                  c_1.write(isim)
a.close()
b.close()
fark_1.close()
c_1.close()



