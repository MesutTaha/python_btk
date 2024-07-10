# Bir fonksiyona bir özellik eklemek istenildiğinde kullanılırlar

def my_decorator(func):

    def wrapper():
        print("fonksiyondan önce olan islemler")
        func()
        print("fonksiyondan sonraki islmeler")

    return wrapper

def say_hello():
    print("hello")

def say_greeting():
    print("greeting")

sayHello = my_decorator(say_hello)
sayHello()

# veya
print("**********************************************")

@my_decorator # @my_decorator yukardaki islemin aynisini yapmamızı sağliyor
def Say_Hello():
    print("HELLO")

Say_Hello()