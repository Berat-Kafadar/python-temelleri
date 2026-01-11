# 1-100 e kadar 

# x = 0

# while x <= 100:
#  if x % 2 == 1:
#     print(f'sayı tek: {x}')
#  else:
#     print(f'sayi çift: {x}')
#  x += 1

# print('bitti...')


name = '' # false
while not name.strip():
    name = input('isminizi giriniz: ')
print(f'Merhaba, {name}')