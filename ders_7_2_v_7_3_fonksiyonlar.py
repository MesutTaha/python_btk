"""
def sayHello():
    print("Hello")
sayHello()
"""
"""
def sayMyName(name = "Kullanici Adi"): # eğer fonksiyon içerisine name değeri atanmazsa otomatik olarak "Kullanici Adi" yazılır.
    print("Your name is "+ name)

sayMyName("Mesut")
"""
"""
def totalNumbers(num1, num2):
    return num1+num2

result= totalNumbers(25,int(input("Sayi gir")))
print(result)
"""
"""
def add(*params): # girilen parametre kadar sayilari ekler
# tek yildiz (*) class'i tuple formatta yapar.
    return sum(params)
print(add(10,20))
print(add(10,20,90,85))
print(add(10,20,90,85,89,12,15,45,62,36,78))
"""
"""
def displayUser(**args): # Tıpkı yukarıdaki *params gibi birden fazla
# parametre için (**) yıldız kullanılır. 
# Bu yıldızlar classa dictionary özellik kazandırır.
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name= "Mesut", age=47, city="istanbul")
displayUser(name= "Taha", age=47, city="London", phone="4561331")
displayUser(name= "Fırat", age=47, city="Paris",phone="4561331", e_mail="firat@gmail.com")
"""

def myFunction(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    toplam = sum(args)
    print("Toplam: {}".format(toplam))

myFunction(10,20,85,69,75,89, isim= "Kale", konum= "Kolombiya", saat= 15)
