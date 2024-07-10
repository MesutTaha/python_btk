import numpy as np

numbers = np.array([[0,5,10],[15, 20,25],[50,75,85]])
print(numbers)
# result = numbers[0][2]
# print(result)
# result = numbers[0,2]
# print(result)

# result = numbers[:,2] # tüm gruplardaki 2. indexi al -(:) ifadesi tüm satırlara etki eder- 10,25,85
# print(result)

# result = numbers[:,0] # 0,15,50
# print(result)

# result = numbers[:,0:2] # tüm satılardaki 0-2. indeks arasındaki sayılar (2 dahil değil)
# print(result)

# result = numbers[-1, :] # sonuncu satırdaki tüm kolonları al anlamına gelir- 50,75,85 
# print(result)


arr1 = np.arange(0,10)
arr2 = arr1

arr2[0] = 20 # arr2 de bir değişiklik yapıldığı zaman arr1 de değişir. çünkü aynı adresteki alanı işgal ediyorlar (REFERANS KOPYALAMA)
"""
(REFERANS KOPYALAMA)
Python'da referans kopyalama, bir nesnenin kendisinin değil de, bellek adresinin kopyalanmasıdır. 
Bu durum, özellikle listeler ve diğer mutable (değiştirilebilir) veri tiplerinde önemlidir. 
Referans kopyalama, nesnenin farklı bir adı altında aynı bellek alanına işaret etmesini sağlar. 
Bu, bir nesne üzerinde yapılan değişikliklerin, o nesnenin tüm referansları tarafından görüleceği anlamına gelir.
"""
print(arr1)
print(arr2)

arr2 = arr1.copy() # bu yöntemle arr1'deki değerler değişmez
arr2[0] = 40
print(arr1)
print(arr2)