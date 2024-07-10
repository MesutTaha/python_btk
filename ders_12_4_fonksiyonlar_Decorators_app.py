import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon "+ func.__name__ + " "+str(finish - start) + " saniye surdu")
    
    return inner

@calculate_time
def usalma(a, b):
    print(math.pow(a, b))
    
@calculate_time
def faktroiyel(num):
    print(math.factorial(num))


usalma(2, 3)
faktroiyel(5)