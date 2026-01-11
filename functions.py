# def sayHello(name = 'user'):
 # return 'hello '  + name

#msg = sayHello('Çınar')
#msg = sayHello('Ada')

#print(msg)

#def total(num1, num2):
 # return num1 + num2
#
#result = (total(10,20))
#print(result)

#def yasHesapla(dogumYili):
 # return 2019 - dogumYili

#ageCinar = yasHesapla(2017)
#ageAda = yasHesapla(2010)
#ageSena = yasHesapla(1999)

#print(ageCinar,ageAda, ageSena)
def yasHesapla(dogumYili):
  return 2025 - dogumYili

def EmekliligeKacYilKaldi(dogumYili, isim):
  yas = yasHesapla(dogumYili)
  emeklilik = 65 - yas
  
  if emeklilik > 0:
    print(f'emekliliğinize {emeklilik} yıl kaldı')
  else:
    print('zaten emekli oldunuz')
  
  EmekliligeKacYilKaldi(1983, 'Ali')
  EmekliligeKacYilKaldi(1950, 'Ahmet')
  EmekliligeKacYilKaldi(1974, 'Yağmur')

 