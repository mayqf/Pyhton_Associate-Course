sözlük = {"kitap" : "book",
"bilgisayar" : "computer",
"programlama": "programming"}
def ara(sözcük):
      hata = "{} kelimesi sözlükte yok!"
      print(sözlük.get(sözcük, hata.format(sözcük)))
def ekle(sözcük, anlam):
      mesaj = "{} kelimesi sözlüğe eklendi!"
      sözlük[sözcük] = anlam
      print(mesaj.format(sözcük))
def sil(sözcük):
      try:
            sözlük.pop(sözcük)
      except KeyError as err:
            print(err, "kelimesi bulunamadı!")
      else:
            print("{} kelimesi sözlükten silindi!".format(sözcük))
#BURAYA DİKKAT!!!
if __name__ == '__main__':
      no = input('Yapmak istediğiniz işlemin numarasını girin: ')
      print('1. Sözlükte kelime ara')
      print('2. Sözlüğe kelime ekle')
      print('3. Sözlükten kelime sil')
      if no == '1':
            sözcük = input('Aradığınız sözcük: ')
            ara(sözcük)
      elif no == '2':
            sözcük = input('Ekleyeceğiniz sözcük: ')
            anlam = input('Eklediğiniz sözcüğün anlamı: ')
            ekle(sözcük, anlam)
      elif no == '3':
            sözcük = input('Sileceğiniz sözcük: ')
            sil(sözcük)
      else:
            print('Yanlış işlem')
