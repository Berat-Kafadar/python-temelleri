#liste = ["1","2","5a","10b","abd","10","50"]

# for i in liste:
#  if i.isdigit():
#   print(i)
#####################################

# import re

# def check_q(girilen_sayi):
#   if len(girilen_sayi) < 1:
#       raise Exception("string en az 1 karakter olmalıdır")
#   elif  re.search("[0-9]", girilen_sayi):
#       raise Exception("string rakam içermemelidir")
#   elif re.search("\s", girilen_sayi):
#       raise Exception("string boşluk içermemelidir")
#   elif re.search("[_@$]", girilen_sayi):
#        raise Exception("string özel karakter içermemelidir")
#   elif re.search("[A-Z]", girilen_sayi):
#      raise Exception("string büyük harf içermemelidir")
#   else:
#      print("string geçerli!") # Hata yoksa onay mesajı

#check_q(girilen_sayi=input(str("bir string giriniz: ")))

# try:
#    check_q(girilen_sayi=input(str("bir string giriniz: ")))
# except Exception as ex:
#    print(ex)
# else:
#   print("string geçerli")


#####################################################

# import re  # Kütüphaneyi en başta içeri aktarmak en iyisidir

# def check_password(psw):
#    if len(psw) < 8:
#       raise Exception("parola en az 8 karakter olmalıdır")
#  elif not re.search("[a-z]", psw):
#     raise Exception("parola küçük harf içermelidir")
# elif not re.search("[A-Z]", psw):
#      raise Exception("parola büyük harf içermelidir")
#  elif not re.search("[0-9]", psw):
#      raise Exception("parola rakam içermelidir")
# elif not re.search("[_@$]", psw):
#      raise Exception("parola özel karakter içermelidir")
#  elif re.search("[ğ, Ğ, ç, Ç, ş, Ş, ü, Ü, ö, Ö, ı, İ]", psw):
#      raise Exception("parola Türkçe karakter içermemelidir")
#  else:
#      print("Parola geçerli!") # Hata yoksa onay mesajı

# --- Ana Program Bloğu (Fonksiyonun Dışında) ---
# check_password(psw=input(str("password giriniz: ")))

# try:
#   check_password(psw=input(str("password giriniz: ")))
# except Exception as ex:
#   print(ex)
# else:
#   print("password geçerli") 


#############################################

def faktoriyel(x):
  x = int(x)


  if x < 0:
    raise ValueError('Negatif değer')
  
  result = 1

  for i in range(1, x+1):
    result *= i

  return result

for x in [5,10,20, -3, "10a"]:
  try:
    y = faktoriyel(x)
  except ValueError as err:
    print(err)
    continue
  print(y)