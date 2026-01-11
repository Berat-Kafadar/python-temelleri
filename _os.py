import os
import datetime

result = dir(os)
result = os.name

# klasör değiştirme / dizin değiştirme
# os.mkdir("newdirectory")
# result = os.getcwd()
# os.chdir('../..')
# os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir()

# for dosya in os.listdir():
#  if dosya.endswith('.py'):
#    print(dosya)



# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturma tarihi
# result = datetime.datetime.fromtimestamp(result.st_ctime) # son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirme tarihi

# os.system("notes.app")

# path 

result = os.path.abspath("_os.py")
result = os.path.dirname("/Users/beratkafadar/Desktop/python temelleri/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("/Users/beratkafadar/Desktop/python temelleri/_os1.py")
result = os.path.exists("/Users/beratkafadar/Desktop/python temelleri")
result = os.path.isdir("/Users/beratkafadar/Desktop/python temelleri")
result = os.path.isfile("/Users/beratkafadar/Desktop/python temelleri/_os.py")



print(result)
