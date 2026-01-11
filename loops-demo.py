# import random 

# hedef = random.randint(0,100)
# tahmin_sayisi = 0

# while True:
 # try:
 #   tahmin = int(input('tahmininizi girin:'))
 #   tahmin_sayisi += 1
 # except ValueError:
 #   print('Lütfen bir sayi girin.')
  
  #if tahmin < hedef:
  #  print('yukarı')
  #elif tahmin > hedef:
  #  print ('aşağı')
  #else: 
  #  print(f'tebrikler sayi : {hedef}')
  #  print(f'{tahmin_sayisi} denemede bildiniz')
  #  break

##################################################

import random
 
sayi = random.randint(1,100)
hak = 5
sayac = 0

while hak > 0:
  hak -= 1
  sayac += 1

  tahmin = int(input('tahmin: '))

  if sayi == tahmin:
    print(f'tebrikler {sayac}  bildiniz. toplam puanınız{100-(20)* sayac-1}')
    break
  elif sayi > tahmin:
    print('yukarı')
  else:
    print('aşağı')
  
  if hak == 0:
    print(f'hakkınız bitti. tutulan sayı: {sayi}')

  