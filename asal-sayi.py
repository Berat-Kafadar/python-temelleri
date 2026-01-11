
sayi = int(input('sayı: '))
asalmi = True


if sayi == 1:
  asalmi = True

for i in range(2, sayi):
  if(sayi % i == 0):
    asalmi = False
    break

if asalmi:
  print('asaldır')
else:
  print('sayı asal değildir')