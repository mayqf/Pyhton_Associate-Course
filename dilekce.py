dilekce= """
                                                                  Tarih:{}


                                    T.C.
                               {} UNIVERSITESI
                         {} Fakultesi Dekanligina

                         
        Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede belirtilen mazeretim gereğince {} Eğitim-Öğretim Yili {} yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.
Bilgilerinizi ve gereğini arz ederim.

        
İmza             :
Adi-Soyadi       :{}
T.C.Kimlik No    :{}
Adres            :{}
Tel.             :{}
Ekler            :{} """


Tarih= input("Tarih: ")
Universite= input ("Universite adi: ")
Fakulte=input("Fakulte Adi: ")
Bolum=input("Bolum-Adi: ")
Adi_Soyadi=input("Adi-Soyadi: ")
Ogrenci_No=input("Ogrenci-No: ")
Eğitim_Öğretim_Yili=("Eğitim-Öğretim Yılı: ")
Yariyil=input("Yariyil: ")
T_C_Kimlik_No=input("T.C.Kimlik_No: ")
Adres= input("Adres: ")
Tel= input ("Tel: ")
Ekler= input("Ekler: ")

print(dilekce.format(Tarih, Universite,Fakulte, Bolum, Adi_Soyadi, Ogrenci_No,
Eğitim_Öğretim_Yili, Yariyil, T_C_Kimlik_No, Adres,Tel,Ekler))

                         
