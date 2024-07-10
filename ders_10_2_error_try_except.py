# print(a) => NameError
# int('1a2') =< ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e)=>SyntacError

while True:

    try:
        x = int(input('x: '))
        y= int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlis bilgi girildi', ex)

    else:
        break    

    finally:
        print('try except sonlandi')
# except (ZeroDivisionError, ValueError)as e:
#     print('yanlis bilgi girildi\n',e)
# Yorum satırı yapmak için istediğin satıları seç ve CTRL+k+CTRL+c

# veya
""" except ZeroDivisionError:
    print('y için 0 degeri girilemez')

except ValueError:
    print('x ve y için sayisal degerler girilmeli') """


    
