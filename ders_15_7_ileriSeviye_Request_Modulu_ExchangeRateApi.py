import requests
import json

api_key = "7154d6ab71b01ea3ee202946"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ") # USD, TRY
alinan_doviz = input("Alinan Doviz: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc = json.loads(sonuc.text)
print("{} {} paranın {} karşılığı {} miktardır".format(miktar, bozulan_doviz, alinan_doviz,miktar * sonuc["conversion_rates"][alinan_doviz]))





