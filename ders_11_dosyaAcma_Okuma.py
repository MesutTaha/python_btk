# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
# Dosya içersindeki bilgileri siler!!! ve istenen şeyi yazar.
"""
file = open("newfile.txt","w")
file.close() # dosyayı kapatmamızın amacı işimiz bittikten sonra kaynakları kullanmaya devam etmesini engellemek
"""
"""
file = open("C:/Users/mesut_rhuqwru/Desktop/newfile.txt","w")
print(file)
file.close()
"""
"""
file= open("newfile.txt","w",encoding="utf-8")
file.write("Mesut Taha Dinleyici2")
print(file)
file.close()
"""

# "a": (Append) ekleme modu. Dosya konumda yoksa oluşturur.
"""
file = open("newfile.txt","a",encoding="utf-8")
file.write("\n2")
file.close()
"""
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
"""
file = open("newfile2.txt","x",encoding="utf-8")
file.close()
"""

# "r": (Read) okuma. 
# varsayılan. open("newfile.txt") = open("newfile.txt","r")
# dosya konumda yoksa hata verir.
"""
try:
    file = open("newfile.txt")
except FileNotFoundError:
    print("Dosya bulunamadi")
finally:
    print("Dosya Kapatildi")
    file.close()
"""

# file = open("newfile.txt","r",encoding="utf-8") ********************************************************
# for döngüsü
"""
for i in file:
    print(i,end="")# end="" satırlar arası boşluğu önlüyor
"""
# read() fonksiyonu
# read(5) gibi sayı yazılırsa ilk 5 harfi alır
"""
content = file.read()
print(content)
"""
#readline() fonksiyonu sadece bir satırı okur
"""
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""
# readlines() foksiyonu her bir satırdaki bilgiyi liste elemanı olarak yazar.
"""
liste = file.readlines()
print(liste)
print(liste[0],end="")
print(liste[8])
file.close()
"""
# with komutu
"""
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)# seek(int) komutu kürsöre konum atar.
    print(file.tell()) # tell()fonk. kürsör(imleç)in en son bulunduğu konumu gösterir.
"""
# r+ hem yazma hem okuma aynı anda
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(90)
    file.write("\nGalatasaray")
"""
# Sayfa sonuna ekleme
"""
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nGalatasaray")
"""

# Sayfa Başına ekleme
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    content= file.read()
    content = "Cİmbom\n" + content
    file.seek(0)
    file.write(content) 
"""
# Sayfa ortasında güncelleme.

with open("newfile.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(2, "MTD\n")
    file.seek(0)
    
    # LİSTEYİ DOSYAYA YAZDRIMAK İÇİN
    """
    for i in liste: 
        file.write(i)
    """
    # veya

    file.writelines(liste)
