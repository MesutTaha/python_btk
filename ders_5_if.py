import datetime
tarih = input("Arac trafige cikis tarihi: ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigeCikis

print(f"{fark.days} gun kaldi")