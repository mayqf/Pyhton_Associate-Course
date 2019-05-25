class Tugla():
        def __init__(self,adi="20lik",boyutlar=[10,20,5],renk_listesi=["Sari","Gri","Turuncu"],renk="Gri",agirlik="Hafif",uretim_suresi=5,miktar=10000,fiyat=5):
            self.adi=adi
            self.boyutlar=boyutlar
            self.renk_listesi=renk_listesi
            self.renk=renk
            self.agirlik=agirlik
            self.uretim_suresi=uretim_suresi
            self.miktar=miktar
            self.fiyat=fiyat
        def renk_secimi(self):
            secim=input("Renk secimi(Gri\Turuncu\Sari)=")
            if secim in self.renk_listesi:
                print(secim, "rengini sectiniz")
                self.renk=secim
                return self.renk                        
            else:
                print("Bu renkte uretim yok")
                secim=input("Renk secimi(Gri\Turuncu\Sari)=")
                self.renk=secim
                return self.renk 
        def agirlik_secimi(self):
            secenek=input("Hafif urun cesidi icin 'Hafif', Agir urun cesidi icin 'Agir' giriniz:")
            if secenek=="Hafif":
                self.agirlik="Hafif"
                print(secenek,"urun cesidini sectiniz")
            elif secenek=="Agir":
                self.agirlik="Agir"
                print(secenek,"urun cesidini sectiniz")
            else:
                    print("Hafif ya da Agir seciniz")
                    secenek=input("Hafif urun cesidi icin 'Hafif', Agir urun cesidi icin 'Agir' giriniz:")
                    self.agirlik=secenek
            
        def uretim_sure_secim(self,renk,agirlik):
            if self.renk=="Sari":
                if self.agirlik=="Hafif":
                    print("Uretim suresi, 10 gundur.")
                    self.uretim_suresi=10
                    return self.uretim_suresi
                else:
                    print("Uretim suresi, 5 gundur.")
                    self.uretim_suresi=7
                    return self.uretim_suresi
            else:
                    self.uretim_suresi=5
                    return self.uretim_suresi
        
        def __len__(self):#Ozel metodlar
                return self.miktar
        def __del__(self):
                print("Tugla objesi siliniyor........")                
                
        def __str__(self):
                return """
                        Urun ozellikleri
                        
                Urun Adi:{}
                Boyutlari:{}
                Renk Secenekleri:{}
                Renk:{}
                Agirlik:{}
                Uretim Suresi(gun):{}
                Stoktaki Miktar:{}
                Fiyat(TL):{}""".format(self.adi,self.boyutlar,self.renk_listesi,self.renk,self.agirlik,self.uretim_suresi,self.miktar,self.fiyat)
        
       
                




tugla_25=Tugla(adi="25lik",boyutlar=[10,25,5])
print(tugla_25.renk_listesi[0])

print(tugla_25)
#del(tugla)
class Yutong(Tugla):#inheritance

        def __init__(self,adi="Yutong20lik",boyutlar=[10,20,5],renk_listesi=["Sari","Gri","Turuncu"],renk="Gri",agirlik="Hafif",uretim_suresi=5,miktar=10000,fiyat=5,paket="Paketli"):
            self.adi=adi
            self.boyutlar=boyutlar
            self.renk_listesi=renk_listesi
            self.renk=renk
            self.agirlik=agirlik
            self.uretim_suresi=uretim_suresi
            self.miktar=miktar
            self.fiyat=fiyat
            self.paket=paket #overriding
            
        def paket_secimi(self):
                secim=input("Paketli\Paketsiz")
                if secim== "Paketli":
                        self.paket="Paketli"
                else:
                        self.paket="Paketsiz"              
                
            
        def extra_renk (self):
                self.renk_listesi=self.renk_listesi.append("Mavi")#Yeni fonksiyon ekledik.
       
                
y=Yutong(adi="Yutong_25lik")
print(y)


