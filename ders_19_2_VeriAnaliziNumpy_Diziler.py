import numpy as np

# result = np.arange(1,10) # 1-10 arasında dizi oluştur -10 dahil değil-
# print(result)

# result = np.arange(10,100, 5) # 10-100 arasında dizi oluştur -100 dahil değil- adım sayısı 5
# print(result)

# result = np.zeros(10) # 0 lardan oluşan belirtilen miktarda dizi
# print(result)

# result = np.ones(10) # 1 lerdan oluşan belirtilen miktarda dizi
# print(result)

# result = np.linspace(0, 100, 5) # 0la 100 arasında 5 eşit parçaya bölünmüş bir şekilde dizi
# print(result)

# result = np.linspace(0, 5, 5) # 0la 5 arasında 5 eşit parçaya bölünmüş bir şekilde dizi
# print(result)

# result = np.random.randint(0,10) # 0 la 10 arasında -10 hariç- rastgele int sayı
# print(result)

# result = np.random.randint(20) # 0 la 20 arasında -20 hariç- rastgele int sayı
# print(result)

# result = np.random.randint(0, 20, 3) # 0 la 20 arasında -20 hariç- rastgele 3 adet int sayı
# print(result)

# result = np.random.rand(5) # 0 la 1 arasında 5 adet sayı
# print(result)

# result = np.random.randn(5) # 0 la 1 arasında 5 adet negatif sayılar da dahil sayı
# print(result)

# np_array = np.arange(50) # 50 ye kadar olan dizi
# result = np_array.reshape(5,10) # (5,10) matris
# print(result)

# np_array = np.arange(50) # 50 ye kadar olan dizi
# np_multi = np_array.reshape(5,10) # (5,10) matris
# print(np_multi.sum(axis=0)) # yukardan aşağıya toplar
# print(np_multi.sum(axis=1)) # soldan sağa toplar

rnd_numbers =np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()
result2 = rnd_numbers.min()
result3 = rnd_numbers.mean() # ortalama
result4 = rnd_numbers.argmax() # max sayısının index numarasını gösterir
result5 = rnd_numbers.argmin() # min sayısının index numarasını gösterir
print(result)
print(result2)
print(result3)
print(result4)
print(result5)