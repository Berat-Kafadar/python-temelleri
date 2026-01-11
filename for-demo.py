# sayilar =[1,3,5,7,9,12,19,21]


# for sayilar in sayilar:
#  print(f"hangi sayılar 3 ün katıdır: {sayilar} ve {(sayilar % 3 == 0)}")

###########################################

# toplam = 0


# for sayilar in sayilar:
#    toplam += sayilar
#   print(f"sayıların toplamı: {toplam}")

############################

#for sayilar in sayilar:
# if sayilar % 2 == 1:
#   print(f"tek sayılar yazdır: {sayilar}")


##############################

# sehirler = ['kocaeli', 'istanbul', 'ankara' , 'izmir', 'rize']


# for sehir in sehirler:
#  if (len(sehir) <= 5):
# print(sehir)

#####################################

urunler = [
  {'name': 'samsung S6', 'price': '3000'},
  {'name': 'samsung S7', 'price': '4000'},
  {'name': 'samsung S8', 'price': '5000'},
  {'name': 'samsung S9', 'price': '6000'},
  {'name': 'samsung S10', 'price': '7000'}
          ]

 # toplam = 0
 # for urun in urunler:
 # fiyat = int(urun['price'])
 # toplam += fiyat
 # print(f"ürünlerin toplamı: {toplam}")

  
for  urun in urunler:
  fiyat = int(urun['price'])
  if fiyat <= 5000:
     print(f"ürünler 5000 altı {urun}")
  
 