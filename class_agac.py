class Agac:
      tur="meyve"
      bahce={}
      def __init__(self,adi,adedi,yil):
            self.adi=adi
            self.adedi=adedi
            self.yil=yil
            self.bahce_ekle()
                  
      def bahce_ekle(self):
            self.bahce[self.adi]=self.adedi

      @classmethod
      def bahce_goster(cls):
            print(cls.tur,"bahcemizde:")
            for i, j in cls.bahce.items():
                  print("     -{} agacindan {};".format(i, j))
            print("tane vardir!")
            
      @staticmethod     
      def toprak_cinsi():
            print("Arazi humusludur")   
      
            
      def bakim_zamani(self):
            print(self.adi,end=" ")
            yas=int(input("agacinin bakim periyodunu ogrenmek icin yasini giriniz:"))
            if yas>5:
                  print( "2 yilda bir bakim yapilir!")
            else:
                  print("Yilda 1 bakim yapilir!")
      def sulama_zamani(self):
            if self.adi=="elma":
                  print( "ayda 1 kez sulanir")
            else:
                  print("2 ayda 1 kez sulanir")
      
      def kesim_zamani(self):
            busene=int(input("Kesim tarihini hesaplamak icin icinde bulundugumuz yili giriniz:"))
            if busene-self.yil>15:
                  print("kesim zamani gelmistir")
            else:
                  print("Henuz kesilemez")

            


elma=Agac("elma",3,2019)
armut=Agac("armut",5,2019)
seftali=Agac("Seftali",10,2019)
Agac.bahce_goster()
elma.bakim_zamani()
elma.sulama_zamani()
Agac.toprak_cinsi()
elma.kesim_zamani()



           
