ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    }
}  

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

#ogrenciler[number] = {
#    'ad' : name,
#    'soyad' : surname,
#   'telefon' : phone
# }

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
}) 

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
}) 

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
}) 
 

print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[number]

print(f'Aradığınız  öğrenci: {ogrenci["ad"]} {ogrenci["soyad"]} {ogrenci["telefon"]}')


