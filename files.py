
# dosyayı konuma oluşturur
# dosya içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt", "w")
# file.close()

# file = open("newfile.txt", "w", encoding="utf-8")
# file.write("Sadık Turan")
# file.close()

################################
# "a": (append) ekleme. dosya konumda yoksa oluşturur

# file = open("newfile.txt", "a", encoding="utf-8")
# file.write("Sadık Turan")
# file.close()
#################################
# "x": (create) oluşturma. dosya zaten varsa hata verir
file = open("newfile2.txt", "x", encoding="utf-8")