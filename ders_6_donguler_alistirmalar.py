
import random 
sayi = random.randint(1, 100)
print(sayi)
puan = 100
hak = int(input("Kac hak kullanarak bilebilirsiniz: "))
i = 0
durum = True and i < hak

while durum:
    in_sayi = int(input(f"Sayiyi bulmak icin {i+1}. denemenizi girin: "))
    if in_sayi == sayi:
        print(f"Tebrikler {i+1}. denemenizde {sayi} degerini buldunuz\n Puaniniz {(hak-i)*100/hak}")
        break
    elif in_sayi < sayi:
        print(f"Daha BUYUK sayi girin\n Kalan hak {hak-(i+1)}") 
    else:
        print(f"Daha KUCUK sayi girin\n Kalan hak {hak-(i+1)}") 
    i+=1
    if i == hak:
        print("Haklariniz tukendi\n puaniniz 0")
        break

"""
sayi = int(input("Sayi girin: "))

kalan = list()
for i in range(2, sayi):
    if sayi % i == 0:
        kalan.append(i)

if kalan: # Dizi dolu veya boş olduğunu böyle anlayabilirsin.
    print(f"{sayi} sayisi {tuple(kalan)} sayi veya sayilarina bolunebilir")
else:
    print(f"{sayi} sayisi asal sayidir.")
"""