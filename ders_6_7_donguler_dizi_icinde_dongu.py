
numbers = list()

for x in range(10):
    numbers.append(x)
print(numbers)

# veya
    
sayilar = [x for x in range(10)]
print(sayilar)

#////////////////////////////////////////////////////
"""
numbers = list()
for x in range(10):
    numbers.append(x**2)
print(numbers)

# veya
    
sayilar = [x**2 for x in range(10)]
print(sayilar)
"""
# ////////////////////////////////////////////////////
"""
numbers = list()
for x in range(10):
    if x % 3 == 0:
        numbers.append(x**2)
print(numbers)

# veya
    
sayilar = [x**2 for x in range(10) if x % 3 ==0]
print(sayilar)
"""
#/////////////////////////////////////////////////////
"""
myString = "Hello"
myList = list() 

for letter in myString:
    myList.append(letter)
print(myList)

myList2 = [letter2 for letter2 in myString]
print(myList2)
"""
# ////////////////////////////////////////////////////
"""
years = [1956, 1985,1962,1947,1999]

yas = [2024- year for year in years]
print(yas)
"""
# ////////////////////////////////////////////////////
"""
results = list()
for x in range(0,3):
    for y in range(3):
        results.append((x,y))
print(results)
# veya
        
results2 = list()
results2 = [(x,y) for x in range(3) for y in range(3)]
print(results2)
"""