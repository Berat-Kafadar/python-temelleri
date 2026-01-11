# def yazdir(kelime, adet):
#  print(kelime * adet)

# yazdir(' Merhaba ', 50)

############################################

# def listeyeCevir(*params):
#  liste = []

#  for param in params:
#    liste.append(param)
  
#  return liste

# result = listeyeCevir(50,123,23,4,'meraba')
# print(result)

#########################################

# def asalSayılariBul(sayi1, sayi2):
#  for sayi in range(sayi1, sayi2 + 1):
#    if sayi > 1:
#      asal_mi = True
#      for i in range(2, sayi):
#        if (sayi % i == 0):
 #         asal_mi = False
 #         break
 #     if asal_mi:
 #       print(sayi)

# sayi1 = int(input('sayi 1: '))
# sayi2 = int(input('sayi 2: '))

# asalSayılariBul(sayi1, sayi2)

##########################################



def tamBolenlerBul(sayi):
  tamBolenler = []
  for i in range(2, sayi):
        if (sayi % i == 0):
          tamBolenler.append(i)
  return tamBolenler
  
print(tamBolenlerBul(20))



