
# Objext Oriented Programing (OOP)

# class
"""
class Person:
    # attributes (özellik)
    address = "no information"
    # constructor (yapıcı method)
    def __init__(self, name, year):
        # Person classı çağırıldığı anda __init__ metodu çalışır
        # object attributes
        self.name = name
        self.year = year
    # instance methods
    def intro(self):
        print('hello ' + self.name)
    def calculateAge(self):
        return 2024-self.year

# object (instance)

p1 = Person(name="mesut", year=1999)
print("name: {}".format(p1.name))
print(p1.year)
print(p1.address)
print(p1)
intro = p1.intro() 
age = p1.calculateAge()
print(intro)
print(age)
"""


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * pow(self.yaricap, 2)
    

c1 = Circle(yaricap=10)
print(f"alan: {c1.alan_hesapla()}\ncevre: {c1.cevre_hesapla()}")
