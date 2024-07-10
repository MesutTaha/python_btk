def not_hesapla(satir):

    satir = satir[:-1]# iki satır arasındaki boşluğu yok etmek için 
    liste = satir.split(":")
    ogrenci = liste[0]
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 =int(notlar[1])
    not3 =int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>=90:
        return ogrenci+ ": AA"
    elif ortalama>=85 and ortalama<90:
        return ogrenci+ ": BB"
    
    else:
        return ogrenci+ ": CC"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():

    ad = input("Öğrenci Adi: ")
    soyad = input("Öğrenci SoyAdi: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    # ogrenci = {"ad": ad,
    #            "soyad": soyad,
    #            "not1": not1,
    #            "not2": not2,
    #            "not3": not3}

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        # for i in ogrenci.values():
        #     file.write(i)
        file.write(ad+ " "+ soyad + ":"+ not1+","+not2+"," +not3+"\n")

def notlari_kaydet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = list()
        for i in file:
            liste.append(not_hesapla(i))

        with open("sinav_sonuclari.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i+"\n")

        


try:
    open("sinav_notlari.txt","a", encoding="utf-8")
except FileExistsError:
    print("Dosya bulunamadi")
    open("sinav_notlari.txt","w", encoding="utf-8")
    

while True:
    islem = int(input("1- Notlari oku\n2- Not Gir\n3- Notlari kaydet\n4-Çikis\n"))



    if islem == 1:
        ortalamalari_oku()
    elif islem == 2:
        not_gir()
    elif islem == 3:
        notlari_kaydet()
    elif islem == 4:
        break
    else:
        break
