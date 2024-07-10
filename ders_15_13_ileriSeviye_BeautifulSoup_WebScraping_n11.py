import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
html = requests.get(url, headers=header).content

soup = BeautifulSoup(html,'html.parser')

result = soup.find_all("li", {"class":"column"})
for i in result:
    # link = i.a.get('href')
    p_name =i.a.h3.text
    price = i.find('div', {'class':'priceContainer'}).find_all('span')[-1].ins.text.strip('TL') # strip belirtilen ifadeyi temadan çıkarır (artık ücretin yanında TL yazmayacak)
    
    print(f'{p_name} MODEL BİLGİSAYAR {price}')
    