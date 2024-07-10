import numpy as np

# # 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluştur.
# result = np.array([10,15,30,45,60])
# print(result)
# # 2- (5-15) arasındaki sayılarla numpy dizisi oluştur
# result = np.arange(5,15)
# print(result)
# # 3- (50-100)arasında 5er 5er artarak numpy dizisi oluştur.
# result = np.arange(50,100,5)
# print(result)
# # 4- 10 elemanlı 0 lardan oluşan numpy dizisi oluştur.
# result = np.zeros(10)
# print(result)
# # 5- 10 elemanlı 1 lerdan oluşan numpy dizisi oluştur.
# result = np.ones(10)
# print(result)
# # 6- (0-100) arasında eşit aralıklı 5 sayı üretin
# result = np.linspace(0,100,5)
# print(result)
# # 7- (10-30) arasında rastgele 5 tane tamsayı üretin
# result = np.random.randint(10,30,5)
# print(result)
# # 8- [-1 ile 1] arasında 10 adet sayi üretin
# result = np.random.randn(10)
# print(result)
# # 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluştur.
# numbers= np.random.randint(10,50,size=(3,5))
# # veya
# # numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
#  #10- üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
# print(numbers.sum(axis=0)) # sütun toplamları
# print(numbers.sum(axis=1)) # satır toplamları
# # 11- üretilen matrisin en büyük, en küçük ve ortlaması nedir.
# print(numbers.max()) # en büyük
# print(numbers.min()) # en küçük
# print(numbers.mean()) # ortalama 
# # 12- üretilen matrisin en büyük değerinin indeksi nedir
# print(numbers.argmax()) # en büyük sayı index
# # 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz
# result = np.arange(10,20)
# print(result[0:3])
# # 14- üretilen dizinin elemanlarını tersten yazdırın
# print(result[::-1])
# # 15- üretilen matrisin ilkve son satırını seçiniz
# print(numbers[0])
# print(numbers[-1])
# # 16- üretilen matrisin 2. satır ve 3. sütunundaki elemanı hangisidir
# print(numbers[1,2]) # index numaraları
# # veya
# print(numbers[1][2])
# # 17- üretilen matrisin tüm satırlardaki ilk elemanı seçiniz
# print(numbers[:,0])
# # 18- üretilen matrisin her bir elemanının karesini alınız.
# print(numbers**2)
# # 19- Üretilen matris elamanlarının hangisi pozitif çift sayıdır.
matris = np.random.randint(-50,50,size=(5,5))
print(matris)
poz = matris>0
print(matris[poz])
