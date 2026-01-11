# x = 10

# if x > 5:
 # raise Exception("x 5 den büyük değer alamaz")

""" import re  # Kütüphaneyi en başta içeri aktarmak en iyisidir

def check_password(psw):
    if len(psw) < 8:
        raise Exception("parola en az 8 karakter olmalıdır")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("parola özel karakter içermelidir")
    elif re.search("\s", psw):
        raise Exception("parola boşluk içermemelidir")
    else:
        print("Parola geçerli!") # Hata yoksa onay mesajı

# --- Ana Program Bloğu (Fonksiyonun Dışında) ---

password = "12345678aA_" 

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Parola geçerli!")
finally:
    print("validation tamamlandı.") """


class Person:
  def __init__(self, name, year):
    if len(name) > 10:
        raise Exception("name alanı fazla karakter içeriyor.")
    else:
       self.name = name

p = Person("Ali", 1989)