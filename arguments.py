#def changeName(n):
#  n = 'ada'

#name = 'yiğit'

#changeName(name)
#print(name)


#def change(n):
 # n[0] = 'istanbul'

#sehirler = ['ankara', 'izmir']

#change(sehirler[:])

#print(sehirler)


# def add(*params):
#  sum = 0

 # for n in params:
#    sum = sum + n
#  return sum

#print(add(10,20))
#print(add(10,20,30))
#print(add(10,20,30,40,50,50))

def displayUser(**args):
  for key, value in args.items():
    print('{} is  {}' .format(key,value))


displayUser(name = 'Çınar', age = 2, city = 'istanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli', phone = '1213213123')
displayUser(name = 'Yiğit', age = 14, city = 'ankara', phone = '1213213123', email='yiğit@gmail.com')

def myFunc(a, b, c ,*args, **kwargs):
  print(a)
  print(b)
  print(c)
  print(args)
  print(kwargs)

myFunc(10,20,30,40,50, key1 = 'value 1' , key2 = 'value 2')
