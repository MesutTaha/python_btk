# global scope
x = 'global x'

def func():
    # local scope
    # eğer foknsiyon icerisinde x tanimlnamzsa fonksiyon globaldeki x degerini kullanir
    x = 'local x'
    print(x)

print(x)
func()

#*****************************************************************

# globaldeki x degerini fonksiyon icerisinde degistirmek için

x = 50 

def degistir():
    global x 
    x = 100
    print(x)


# fonksiyondan önce x i yazdirirsam yine 50 sayisi yazdirilir
print(x) # 50
degistir() # 100
print(x) # 100
#*********************************************************************