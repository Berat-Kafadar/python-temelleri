mylist = [1, 2, 3]
myString = 'my string'

print(len(myString))
print(len(mylist)) 
print(type(mylist))
print(type(myString))



class Movie():
   def __init__(self, title, director, duration):
      self.title = title
      self.director = director
      self.duration = duration
      print('movie object created')

   def __str__(self):
      return f"{self.title} by {self.director}"
   
   def __len__(self):
      return self.duration

   def __del__(self):
      print('movie object deleted')

m = Movie('film adı', 'yönetmen adı', 120)

# print(str(mylist))
print(str(m))
# print(len(mylist))
# print(len(m))  # Hata verir çünkü Movie sınıfında __len__ metodu tanımlı değil

