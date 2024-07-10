
"""
name = "" # false

while not name.strip(): # .strip() baştan ve sondan girilen herhangi bir boşluk karakteri silinir
    # böylece kullanıcı sadece boşluk bırakarak kodu manipüle edemez.
    name = input("Kullanici adinizi giriniz: ")

print(f"Merhaba, {name}") 
"""


"""
ilk_sayi = int(input("Araliktaki ilk sayiyi giriniz: "))
son_sayi = int(input("Araliktaki son sayiyi giriniz: "))

sayilar = ilk_sayi
while sayilar < son_sayi :
    if sayilar % 2 == 1:
        print(sayilar)
    sayilar+=1
"""
"""
i = 0
dizi = list()
while i < 5:
    sayi = int(input("sayi girin: "))
    dizi.append(sayi)
    i += 1
dizi.sort()
print(dizi)
"""

# urun_sayisi = int(input("urun sayisi: "))
# i = 0
# urun_agaci = dict()
# while i < urun_sayisi:
#     urun_adi = input(f"{i+1}. urunun ismini giriniz: ")
#     urun_fiyati = int(input(f"{i+1}. urunun fiyatini giriniz: "))
#     yeni_urun = [[urun_adi, urun_fiyati]] # yeni_urun = [(urun_adi, urun_fiyati)]
#     urun_agaci.update(yeni_urun)
#     i += 1
#     """
#     urunler = list()
#     urunler.append({
#     name: urun_adi
#     price: urun_fiyati
#     }) #  şeklinde de dictionary yapmış oluruz.
#     """
# print(urun_agaci)