import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
result = numbers1 + numbers2
print(numbers1)
print(numbers2)
# print(result)

# result =np.sin(numbers1)
# print(result)

# result = np.cos(numbers2)
# print(result)

# result = np.sqrt(numbers1)
# print(result)

# result = np.log(numbers2)
# print(result)

# multinumbers1 = numbers1.reshape(2,3)
# multinumbers2 = numbers2.reshape(2,3)
# print(multinumbers1)
# print(multinumbers2)

# result = np.vstack((multinumbers1,multinumbers2)) # iki matrisi alt alta yazar -(vstack) v:vertical- (2,3) x(2,3): (4,3)
# print(result)

# result = np.hstack((multinumbers1,multinumbers2)) # iki matrisi yan yana yazar -hstack h:horizontal- (2,3) x(2,3): (2,6)
# print(result)

result = numbers1 >=50 # örn: [ True False  True  True  True  True] boolean şeklinde tüm elemanları teker teker yazar
print(result)

result = numbers2 %2 ==0 # örn: [ True  True False  True  True False] boolean şeklinde tüm elemanları teker teker yazar
print(result[2]) #örn: True
print(numbers2[result]) # numbers2 içersinde True değerini sağlayan indexlerdeki sayilari yazdirir. örn: numbers2=[87 60 26 82 63 48] -> print(numbers2[result])=[60 26 82 48]
