liste = ["1","2","3","4","5a","10b","abc", "85", "8op8", "52"]

# 1 - Liste elemanları içersindeki sayısal değerleri bulunuz
"""
sayilar = [eleman for eleman in liste if eleman.isnumeric()==True]
print(sayilar)

#veya
sayi_listesi = []
harf_listesi = []

for eleman in liste:
    try:
        # Elemanı integer'a dönüştürmeye çalış
        sayi = int(eleman)
        # Dönüşüm başarılı ise, elemanı sayı listesine ekle
        sayi_listesi.append(sayi)
    except ValueError:
        # Dönüşüm başarısız ise, elemanı harf listesine ekle
        harf_listesi.append(eleman)

print("Sayılar:", sayi_listesi)
print("Harfler:", harf_listesi)
"""

# 2 - Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın

"""
while True:
    girdi = input("Sayi Girin: ")

    if girdi == "q":
        break
    
    try: 
        result = float(girdi)
        print("Girilen SAYIII:", result)
    except ValueError:
        print("Sayisal Deger Giriniz")
        #continue
"""
    
# 3 - Girilen parola içinde türkçe karakter hatası veriniz
"""
import re
def check_pass(psw):
    if re.search("[çÇğĞıİöÖşŞüÜ]",psw):
        raise Exception("Parola Türkçe karakter içeremez!!!")
    
while True:

    password = input("Parola Giriniz: ")
    try:
        check_pass(password)
    except Exception as ex:
        print(ex)
        continue
    else:
        print("Şifre Geçerli")

    finally:
        print("Teşekkürler")

"""
# 4 - Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin

def faktoriyel(n):
    # Faktöriyel hesaplama
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Negatif Değer")
    elif not int(n):
        raise TypeError("Numeric Değer Giriniz")
    else:
        return n * faktoriyel(n-1)

while True:

    deger = input("faktoriyel hesabi için sayi girin: ")

    try: 
        sayi = int(deger)
        fakt = faktoriyel(sayi)
        print("Girilen Sayinin Faktoriyeli:", fakt)
    
    except Exception as ex:
        print("HATA:", ex)
        continue
