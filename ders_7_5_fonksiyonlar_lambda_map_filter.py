def square(num): return num ** 2

numbers= [1,3,5,9,10]
result = list(map(square, numbers))
# map() fonksiyonu, bir liste ya da demet gibi iterasyon yapılabilir 
# veri türlerinin her bir verisini bir fonksiyona tek tek parametre 
# olarak göndermek için kullanılır.
print(result)

# veya 

for item in map(square, numbers):
    print(item)

ucUssu = lambda num: num **3
result = list(map(ucUssu, numbers))
print(result)
# Python'da lambda, tek satırlık fonksiyonlardır. 
# Bir ya da daha fazla parametre kabul ederler, ancak tek bir işlem yapabilirler
result = ucUssu(6)
print(result)

check_even = lambda num: num%2 == 0

print(check_even(numbers[4]))