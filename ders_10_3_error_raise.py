# Raise , bir hata (exception) yükseltmek ve programın normal akışını bozmak için 
# kullanılan bir Python ifadesidir. Hatalar, programın normal çalışma akışını engelleyen 
# durumları temsil eder ve bu hataların uygun bir şekilde ele alınması, 
# programın sağlıklı ve öngörülebilir bir şekilde çalışmasını sağlar.



# x = 10

# if x > 5: 
#     raise Exception("x, 5'ten buyuk olamaz")


def check_password(psw):
    import re
    if len(psw)<7:
        raise Exception("Parola en az 7 karakterden olusmalidir")
    
    # re.search metodu, aranılan bir içeriğin ilgili metin içerisinde olup olmadığını kontrol eder.
    elif not re.search("[a-z]", psw):
        raise Exception("Parola kucuk harf icermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola buyuk harf icermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam icermelidir.")
    elif not re.search("[_@&%+$]", psw):
        raise Exception("Parola alpha numeric deger icermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola bosluk icermemelidir.")
    
password= "12456sadA@"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Gecerli parola")
