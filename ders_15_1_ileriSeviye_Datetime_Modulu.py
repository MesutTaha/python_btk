# import datetime
# from datetime import date
# from datetime import time

from datetime import datetime
from datetime import timedelta

simdi = datetime.now()

result = datetime.now() # saat ve tarih bilgisi
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = datetime.ctime(simdi) # daha detaylı çıktı verir (Tue May 28 13:13:16 2024)
result = datetime.strftime(simdi, '%Y') # yıl
result = datetime.strftime(simdi, '%X') # Saat
result = datetime.strftime(simdi, '%d') # Gun (ayın kaçında olduğumuz)
result = datetime.strftime(simdi, '%A') # Gun (haftanın günü)
result = datetime.strftime(simdi, '%B') # ay
result = datetime.strftime(simdi, '%Y %B %A')

t = '28 Mayis 2024'
gun, ay, yil = t.split()

print(gun)
print(ay)
print(yil)

t = "28 May 2024 hour 13:19:25"
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)
yil = dt.year
print(yil)

birthday = datetime(1999,2,22,12,30,10)# bilgisayarlar için milat 1970'tir yani 1970 den küçük tarihlerde hata verir
result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = simdi - birthday # timedelta
# result = result.days # gün cinsinden aradaki fark 
result = result.seconds #saniye cinsinden aradaki fark
result = simdi + timedelta(days= 10)
print(result)

