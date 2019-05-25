import random
import time
class Kumanda():
      def __init__(self,tv_durum="Acik",tv_ses=0,kanal_listesi=["CNN"],kanal="CNN",dil_listesi=["Turkce", "English","Nederlands","German"],dil="Turkce"):
            self.tv_durum=tv_durum
            self.tv_ses=tv_ses
            self.kanal_listesi=kanal_listesi
            self.kanal=kanal
            self.dil_listesi=dil_listesi
            self.dil=dil
      def tv_ac(self):
            if (self.tv_durum=="Acik"):
                  print("TV zaten acik...")
            else:
                  print("Televizyon Aciliyor....")
                  self.tv_durum="Acik"
      
      def tv_kapat(self):
            if (self.tv_durum=="Kapali"):
                  print("TV zaten kapali...")
            else:
                  print("Televizyon kapaniyor....")
                  self.tv_durum="Kapali"
    
      def ses_ayarlari(self):
            while True:

                  cevap=input ("Sesi Azalt:'<'\nSesi Artirir:'>'\nCikis:cikis")
                  if (cevap=="<"):
                        if (self.tv_ses!=0):
                              self.tv_ses-=1
                              print("Ses:",self.tv_ses)
                        else:
                              print("Ses zaten '0' ")
                  elif(cevap==">"):
                        if (self.tv_ses!=31):
                              self.tv_ses+=1
                              print("Ses:",self.tv_ses)
                  else:
                        print("Ses guncellendi",self.tv_ses)
                        break
      def kanal_ekle(self,kanal_ismi):
            print("Kanal ekliyor....")
            time.sleep(1)
            self.kanal_listesi.append(kanal_ismi)
            print("Kanal eklendi.....")
      def rasgele_kanal(self):
            rasgele=random.randint(0,(len(self.kanal_listesi)-1))
            self.kanal=self.kanal_listesi[rasgele]
            print("Suanki Kanal:", self.kanal)
      def dil_sec(self):
            print("Dil seceneklerimiz:",self.dil_listesi)
            secim=int(input("Sirayla 0,1,2,3 secebilirsiniz"))
            self.dil=self.dil_listesi[secim]
            print("Suanki Dil:", self.dil)
      def  __len__(self):            
                  return len(self.kanal_listesi)
      def __str__(self):
            return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nSuanki Kanal: {}\nDil Listesi: {}\nSuanki dil:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,
                                                                                                                             self.kanal,self.dil_listesi,self.dil)
def bilgi():
      print("""

      Televizyon Uygulamasi

      1.Tv Ac
      2.Tv Kapat
      3.Ses Ayarlari
      4.Kanal Ekle
      5.Kanal Sayisini Ogrenme
      6.Rasgele Kanala Gecme
      7.Televizyon Bilgileri
      8.Dil Bilgisi

      Cikmak icin'q' basiniz
      """)
bilgi()
kumanda=Kumanda()
while True:
      
      islem=input("Islem Seciniz:")
      if islem=="q":
            print("Program sonlandiriliyor...")
            break
      elif islem=="1":
            kumanda.tv_ac()
      elif islem=="2":
            kumanda.tv_kapat()
      elif islem=="3":
            kumanda.ses_ayarlari()
      elif islem=="4":
            kanal_isimleri=input("Kanal islemlerini ',' ile ayirarak girin:")
            kanal_listesi=kanal_isimleri.split(",")
            for eklenecekler in kanal_listesi:
                  kumanda.kanal_ekle(eklenecekler)
      elif islem=="5":
            print("Kanal Sayisi:", len(kumanda))
      elif islem=="6":
            if len(kumanda.kanal_listesi)==1:
                  print("Sadece 1 kanal var, rasgele secim yapilamaz!!!")
            else:
                  kumanda.rasgele_kanal()
      elif islem=="7":
            print(kumanda)
      elif islem=="8":
            kumanda.dil_sec()
      else:
            print("Gecersiz Islem!")
            
      
            
