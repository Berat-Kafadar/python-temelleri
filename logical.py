x = 5

hak = 5
devam = 'e'


result = 5 < x < 10


print(result)

# and

# true, true => true
# true, false => false

result = (x > 5) and (x < 10)

result = (hak > 0) and (devam == 'e')

# or

result = (x > 0) and (x % 2 == 0)

# true, false => true
# true, true => true
# false, false => false

# not 

# x, 5-10 arasında olan bir çift sayı mı ?

result = ((x>5) or (x<10)) and (x%2==0)

result = not(x > 0)

print(result)


