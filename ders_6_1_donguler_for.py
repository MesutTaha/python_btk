sayilar= [1,3,5,7,9,12,19,21]

# 1- sayilar listesindeki hangi sayilar 3'ün katidir?
# 2- sayilar listesindeki sayilarin toplamı kaçtır
toplam = 0
for i in sayilar:
    if i % 3 == 0:
        print(f'{i} ucun kati \n') # 1-
    toplam = toplam + i # 2- 
    if i%2 == 1:
        print(f'{i} tek sayisinin karesi: {pow(i,2)}')

print(f'sayilar listesindeki sayilarin toplami: {toplam}')
