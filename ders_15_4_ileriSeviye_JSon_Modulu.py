# Sadece pythona özel bir yapı değil
# Databaseden veriler bi anrdoid veya web uygulamasına json tipinde taşınabilir.
# Cihazlar arasında ortak bir veri taşıma objesi

import json

person_string = '{"name": "Ali", "languages": ["python", "C#"]}' # string yapıda veri

# JSon string to Dict

# result = json.loads(person_string) # string yapıdan dictionary yapısına çevrildi.
# print(type(result)) # dict

# with open("ders_15_4_ileriSeviye_JSon_Modulu_person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



# JSon Dict to string

person_dict = {
    "name": "Ali", 
    "languages": ["python", "C#"]

}

# result = json.dumps(person_dict) # dictionary to string
# print(result)
# print(type(result))


# with open("ders_15_4_ileriSeviye_JSon_Modulu_person.json", "w") as f: # dosyaya veri gönderme
#     json.dump(person_dict, f) # dictionary to string

person_dict = json.loads(person_string) # string to dict

result = json.dumps(person_dict, indent=10, sort_keys= True) # Çıktıda görüntü olarak daha iyi
print(person_dict)
print(result)

"""
json.dump ve json.dumps Temel Farklar:
Çıktı Tipi:

json.dumps: JSON formatında bir dize döner.
json.dump: JSON verisini bir dosyaya yazar.

Kullanım Amacı:

json.dumps: JSON verisini bir dize olarak kullanmak için.
json.dump: JSON verisini bir dosyaya yazmak için.

"""
