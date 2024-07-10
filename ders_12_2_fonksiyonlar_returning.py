# def usalma(number):
#     def inner (power):
#         return number**power
    
#     return inner


# two = usalma(2)
# print(two(3))
#*******************************************************************************************
# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolü {1} sayfasına ulasabilir".format(role, page)
#         else:
#             return "{0} rolü {1} sayfasına ulasamaz".format(role, page)
    
#     return inner


# admin_user = yetki_sorgula("Product Edit")
# print(admin_user("Admin"))

# common_user = yetki_sorgula("Product Edit")
# print(common_user("User"))
#******************************************************************************************

def islem(islem_adi):
    def toplam(*args):  # sınırsız sayıda argüman = *args
        toplama = 0
        for i in args:
            toplama = toplama + i
        
        return toplama
        
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim = carpim * i
        
        return carpim
    

    if islem_adi == "toplama":
        return toplam
    else: 
        return carpma
    

toplama = islem("toplama")

print(toplama(45,55,800))

carpma = islem("carpma")

print(carpma(5,9,10))
    


