import time
hesapMesut = {
'ad': 'Mesut',
'hesapNo':'123456',
'bakiye':3000,
'ekHesap': 2000
}


hesapTaha= {
'ad': 'Taha',
'hesapNo':'456321',
'bakiye':3000,
'ekHesap': 2000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    print(f"Cekmek istediginiz tutar: {miktar}")
    if miktar <= hesap['bakiye']:
        print("Paraniz hazirlaniyor lutfen bekleyin...")
        time.sleep(1.0)
        print("Paraniz hazir")
        print(f"Kalan Bakiyeniz: {hesap['bakiye']-miktar}")
    elif miktar <= hesap['bakiye'] + hesap['ekHesap']:
        print("Bakiyeniz yetersiz,\nEk hesap kullanmak icin 'y' ye\nislemi iptal etmek icin 'n' ye basin")
        secim = input()
        while True:
            if secim == 'y' or secim == 'Y':
                print("Paraniz hazirlaniyor lutfen bekleyin...")
                time.sleep(1.0)
                print("Paraniz hazir")
                print("Kalan Bakiyeniz: 0")
                print(f"Ek hesaptaki bakiyeniz: {hesap['ekHesap']-(miktar-hesap['bakiye'])}")
                break
            elif secim == 'n' or secim == 'N':
                print("Bakiyeniz yetersiz\nİşleminiz sonlandiriliyor")
                break
            else:
                print("Hatali tuslama yaptiniz\nLutfen Ek hesap kullanmak icin 'y' ye\nislemi iptal etmek icin 'n' ye basin ")
                secim = input()
                break

paraCek(hesapMesut, 3500)