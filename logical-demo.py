 #x = 101

# result = 0 < x < 100

# result = (x > 0) and (x % 2 == 0)

# mail = 'beratkfdr@gmail.com'
# password = '12345'

# result = (mail == 'beratkfdr@gmail.com') and (password == '12345')

# x = 1
# y = 2
# z = 3 

# result = (y > z > x)

# x = int(input("vize 1 not: "))
# y = int(input("vize2 not: "))
# z = int(input("final notu: "))

# toplam = (x * 0.30) + (y * 0.30) + (z * 0.40)


# print(f"dersten notunuz {toplam} ve dersten geçme durumunuz {toplam>=50} ve ortalama önemli değil {toplam>=70}")

name = (input("adınız: "))
kg = int(input("kilonuzu girini: "))
hg = float(input("boyunuzu giriniz: "))


index = (kg / (hg ** 2))


index = (kg) / (hg ** 2)
zayif = (index >= 0) and ( index <= 18.4)
normal = (index>24.9) and (index <= 24.9)
kilolu = (index> 24.9) and (index <= 29.9)
obez = (index>= 29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayif: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')


