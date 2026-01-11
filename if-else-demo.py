# name = input('isminizi giriniz: ')
# yaş = int(input('yaşınızı giriniz: '))
# eğitim = input('eğitim durumunuzu giriniz: ')

# if (yaş >= 18):
 #  if (eğitim ==  'lise' or 'üniversite'):
  #  print('ehliyet alabilirsiniz')
 #  else:
  #  print('ehliyet alma hakkınız yoktur')

#########################################################


# yazılı = int(input('yazılı notunu giriniz: '))
# sözlü = int(input('sözlü notunu giriniz: '))
  

# ortalama = (yazılı + sözlü) / 2

# if (ortalama < 24):
 # print('0')
# else:
 #  if(ortalama < 44):
  #  print('1')
 # else:
 #   if(ortalama < 54):
  #    print('2')
  #  else:
   #   if(ortalama < 69):
    #    print('3')
   #   else:
    #    if(ortalama < 84):
     #     print('4')
     #   else:
      #    if(ortalama < 100):
       #     print('5')
          
################################################3######


import datetime

tarih = input(('aracınız hangi tarihte trafiğe çıktı (2019/8/9): '))
tarih = tarih.split('/')
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now
fark = simdi - trafigeCikis
print(fark) 

if tarih<= 365:
  print('1.servis araalığı')
elif tarih> 365 and tarih <= 365*2:
      print('2. servis aralığı')
elif tarih>365*2 and tarih<=365*3:
    print('3. servis aralığı')
else: 
    print('hatalı bakım')  