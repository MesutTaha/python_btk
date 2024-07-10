# bellekte yer işgal etmeyen iterator üretir.
# oluşturduğumuz değeri anlık kullandıktan sonra herhangi 
# bir şekilde depo etmek istemiyorsak (değere geri dönmeyeceksek)
# generator metodu kullanılır.



# def cube():
#     for i in range(5):
#         yield i ** 3 # generator


# for i in cube():
#     print(i)


liste = [i**3 for i in range(1,5)] # liste (bellekte yer tutar)
generator = (i**3 for i in range(1,5)) # generator (bellekte yer tutmaz)

print(liste)
print(type(liste))
print(generator)
print(type(generator))
print(next(generator))
