# ky - value

# 41 = koceali, 34 = istanbul

#sehirler = ['kocaeli', 'istanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('kocaeli')])
#print(plakalar[sehirler.index('istanbul')])

 # print(plakalar['kocaeli']) = 41
 # print(plakalar['istanbul']) =  34


#plakalar = {'kocaeli': 41, 'istanbul': 34}
#print(plakalar['kocaeli'])
#print(plakalar['istanbul'])

#plakalar['ankara'] = 6
#plakalar['kocaeli'] = 'new value'

#print(plakalar)


import email


users = {
    'beratkafadar': {
        'age': 21,
        'roles': ['admin', 'user'],
        'email': 'sadik@email.com',
        'address': 'kocaeli',
        'phone': '1231231'
    },
    'sefakafadar': {
        'age': 22,
        'roles': ['admin', 'user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231231'
    }
}
print(users['beratkafadar']['age'])
print(users['beratkafadar']['email'])
print(users['beratkafadar']['address']) 