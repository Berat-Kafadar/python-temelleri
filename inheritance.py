# Inheritance (kalıtım): Miras alma



# person => name, lastname, age ,eat(), run(), drink()
# student(person), Teacher(person)


# Animal => dog(animal), cat(animal)


class Person():
  def __init__(self, fname, lname):
    self.firstName = fname
    self.lastName = lname
    print('person created')

  def who_am_i(self):
      print('I am a person')
  
  def eat(self):
      print('I am eating')
  
  def bike(self):
     print('I am biking')

class Student(Person):
  def __init__(self, fname, lname, number):
    Person.__init__(self, fname, lname)
    self.studentNumber = number
    print('Student created')
  
  # override
  def who_am_i(self):
     print('I am a student')

  def sayHello(self):
     print('Hello I am a student')

class Teacher(Person):
   def __init__(self,fname,lname,branch):
      super().__init__(fname, lname)
      self.branch = branch

   def who_am_i(self):
      print(f'I am a {self.branch} teacher')

p1 = Person('Ali', 'Yılmaz')
s1 = Student('Ayşe', 'Demir', 1256)
t1 = Teacher('serkan', 'yılmaz', 'mathematics')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
p1.bike()
s1.bike()
s1.sayHello()