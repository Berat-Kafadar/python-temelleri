# sayilar = [1,3,5,7,9,12,19,21]

# while sayilar:
#  print(f'{sayilar}')
#  break


##################################

# başla = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))

# sayi = başla

# while sayi < bitis:
#  sayi += 1
#  if sayi % 2 == 0:
#    print(sayi)

######################################

# x = 100

# while x > 0:
#  print(x)
# x -= 1

######################################

# numbers = []

# i = 0

# while i<5:
# sayi= int(input('sayı: '))
# numbers.append(sayi)
# i+=1
# numbers.sort()
# print(numbers)
  
#####################################

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i = 0
while(i<adet):
  name = input('ürün ismi: ')
  price = input('ürün fiyatı: ')
  urunler.append({
    'name': name,
    'price': price
  })
i += 1

for urun in urunler:
  print(f'ürün adı: {urun["name"]} ürün fiyatı {urun["price"]}')


