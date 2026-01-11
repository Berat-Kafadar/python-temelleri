website = "https://www.beratkfdr.com" 
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (2024)"

result = len(course)
length = len(website)


result = website[7:10]

result = website[22:25]
result = website[length-3:length]
 
result = course[-15:-1]

result = course [::1]

name, surname, age, job = "Berkay", "Kafadar", 32, "Mühendis"
result =  "benim adım"+ name + " " + surname + ". yaşım " +str(age) + " ve mesleğim " + job
result = 'benim adım {0} {1}. yaşım {2} ve mesleğim {3}'.format(name, surname, age, job)
result = f"benim adım {name} {surname}. yaşım {age} ve mesleğim {job}"

s = "Hello World"
s = s[0:6] + 'W' + s[-4:] 
s.replace('w', 'W')

result = 'abc' * 3


print(s)


print(result)