#a = int(input("sayi 1 gir: "))
#b = int(input("sayi 2 gir: "))

#if a > b : 
 # print("a b den büyüktür: ")

#elif b > a: 
 # print("b a dan büyüktür: ")

#else:
 # print("a ve b birbirine eşittir")

#a = int(input("vize1 notu: "))
#b = int(input("vize2 notu: "))
#c = int(input("final notu: "))

#ortalama = (a * 0.30) + (b * 0.30) + (c * 0.40)

#print(f"öğrenci notu: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

#a = int(input("bir sayı giriniz: "))

#tek = (a % 2) == 1
#cift = (a % 2) == 0
#print(f"sayı tektir: {tek} sayi çifttir: {cift}")


#sayi = int(input('sayı: '))
#pozitifmi = (sayi > 0)
#print(f"girilen sayının pozitif olma durumu: {pozitifmi}")
           
email = 'beratkfdr@gmail.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f"girilen email ve password {isEmail} {isPassword} ")