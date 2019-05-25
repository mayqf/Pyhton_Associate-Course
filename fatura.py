#her bir ayin kac gun cektigini tanimliyoruz.
ocak=mart=mayis=temmuz=agustos=ekim=aralik=31
nisan=haziran=eylul=kasim=30
subat=28
#dogalgazin vergiler dahil metrekup fiyati
birimfiyat=0.79
#kullanici ayda ne kadar dogalgaz tuketmis?
ayliksarfiyat=input("aylik dogalgaz sarfiyatinin metrekup olarak giriniz:")
#kullanici hangi aya ait faturasinin odemek istiyor?
donem=input("""hangi aya ait faturayi hesaplamak istersiniz?
(Lutfen ay adini tamami kucuk harf olacak sekilde giriniz)\n""")
#yukaridaki input()fonksiyonundan gelen veriyi
#Pyhton'in anlayabilecegi bir bicime donusturuyoruz
ay=eval(donem)
#kullanicilarin gunluk dogalgaz sarfiyati
gunluksarfiyat=int(ayliksarfiyat)/ay
#fatura tutari
fatura=birimfiyat*gunluksarfiyat*ay
print("gunluk sarfiyatiniz:\t",gunluksarfiyat,"metrekup\n",
      "tahmini fatura tutari:\t",fatura,"TL",sep="")
