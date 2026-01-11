def not_hesapla(satir):
    satir = satir.strip()
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1+not2+not3) / 3

    if ortalama>=90 and ortalama<=100:
      harf = "AA"
    elif ortalama>=85 and ortalama<=89:
      harf = "BA"
    elif ortalama>=65:
      harf = "CC"
    else:
      harf = "FF"


    return ogrenciAdi + ": " + harf + "\n"

def ortalamalari_oku():
  with open("sinav_notlari.txt","r", encoding="utf-8") as file:
     for satir in file:
       if satir.strip():
         print(not_hesapla(satir))

def not_gir():
  ad = input('Öğrenci adı:')
  soyad = input('Öğrenci Soyadı:')
  not1 =  input('Öğrenci Notu1:')
  not2 =  input('Öğrenci Notu2:')
  not3 =  input('Öğrenci Notu3:')

  with open("sinav_notlari.txt","a", encoding="utf-8") as file:
    file.write(ad+ '' + soyad+ ':'+not1+','+not2+','+not3+'\n')

def notlari_kayitet():
  with open('sinav_notlari.txt','r',encoding="utf-8") as file:
    liste = []
  
    for i in file:
        liste.append(not_hesapla(i))
  
  with open("sonuçlar.txt","w",encoding="utf-8") as file2:
    for i in liste:
      file2.write(i)

  

while True:
  islem = input('\n1- Notları oku\n2- Not Gir\n3- Notları Kayıt et\n4- Çıkıs')


  if islem == '1':
    ortalamalari_oku()
  elif islem == '2':
    not_gir()
  elif islem == '3':
    notlari_kayitet()
  elif islem == '4':
    print("Çıkış yapılıyor...")
    break
  else:
    print("hatalı seçim, tekrar deneyin")