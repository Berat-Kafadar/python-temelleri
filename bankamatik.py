





SadıkHesap = {
  'ad': 'Sadık Turan',
  'hesapNo' : '123456',
  'bakiye': 3000,
  'ekHesap': 2000
}

BeratHesap = {
  'ad': 'Berat Kafadar',
  'hesapNo' : '12345678',
  'bakiye': 1000,
  'ekHesap': 2000
}


def paraCek(hesap, miktar):
  print(f"Merhaba {hesap['ad']}")

  if (hesap['bakiye'] >= miktar):
    hesap['bakiye'] -= miktar
    print('paranızı alabilirsiniz')
    bakiyeSorgula(hesap)
  else:
    toplam = hesap['bakiye'] + hesap ['ekHesap']

    if (toplam >= miktar):
      ekHesapKullanımı = input('ek hesap kullanılsın mı (e/h): ')

      if ekHesapKullanımı == 'e':
        
        ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
        hesap['bakiye'] = 0
        hesap['ekHesap'] -= ekhesapKullanilacakMiktar
        print('paranızı alabilirsiniz')
        bakiyeSorgula(hesap)
      else:
        print(f'{hesap['hesapNo']} nolu hesanıbınızda {hesap['bakiye']} bulunmaktadır')
    else:
      print('üzgünüz bakiye yetersiz')


def bakiyeSorgula(hesap):
  print(f'{hesap['hesapNo']} nolu hesabınız {hesap['bakiye']} tl bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} Tl bulunmaktadır')

paraCek(SadıkHesap, 3000)
bakiyeSorgula(SadıkHesap)

print('*************')

paraCek(SadıkHesap, 3000)
paraCek(SadıkHesap, 2000)