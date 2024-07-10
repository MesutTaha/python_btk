"""
Python'daki requests modülü, HTTP istekleri göndermek ve yanıtları almak için kullanılan 
bir kütüphanedir. Bu kütüphane, API'lerle, web servisleriyle veya genel olarak web 
sayfalarıyla etkileşim kurmayı kolaylaştırır. requests modülü, HTTP/1.1'e uygun isteklerde
 bulunmanızı ve bu isteklerin yanıtlarını kolayca işlemenizi sağlar.

"""
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
print(result) # <Response [200]> başarılı anlamına geliyor

for i in result:
    # print(i)
    # print(i["title"])
    if i["userId"] == 1:
        print(i["userId"])
        print(i["title"])