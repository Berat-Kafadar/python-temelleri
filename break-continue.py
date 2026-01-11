# name = 'berat kafadar'


# for letter in name:
#  if letter == 'a':
#    continue
#  print(letter)


# x = 0

# while x < 5:
#   x+=1
#   if x == 2:
#     continue
#    print(x)



x = 0
result = 0

while x <= 100:
  x+=1
  if x % 2 == 1:
    continue
  result += x
 
print(f'toplam: {result}')
   
  