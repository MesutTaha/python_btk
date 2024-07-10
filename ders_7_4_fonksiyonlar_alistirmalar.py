"""
def kelimeYaz(kelime, defa):
# Gönderilen kelimeyi belirtilen kez ekranda yazdirma
    i = 0
    while i< defa:
        print(kelime)
        i+=1

kelimeYaz("lale", 2)

# veya 

def kelimeYaz2(kelime, defa):
# Gönderilen kelimeyi belirtilen kez ekranda yazdirma
    print(kelime * defa)

kelimeYaz2("lale\n", 2)
"""
"""
def makeItList(*args):
# Kendine gönderilen sinirsiz sayidaki parametreyi bir listeye çevirme
    a = list(args)
    print(type(args))
    print(a)
    print(type(a))
    return a

makeItList(13565,12,45,12,78,542,"kalem","lol",486)

def findPrimeNumbers(a, b):
    primeNumbers= list()
    for i in range(a, b+1):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                primeNumbers.append(i)
                break
    print(primeNumbers)

findPrimeNumbers(17, 20)

def tamBolenler(sayi):
    bolen = list()

    for i in range(1, sayi+1):
        if sayi % i ==0:
            bolen.append(i)
    print(bolen)

tamBolenler(6)
"""