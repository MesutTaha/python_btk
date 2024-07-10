import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
html = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

#result = soup.find('div', {'id': '__next'}).find('main', {'role':'main'}).find('div',{'class': 'ipc-page-content-container'}).find('section', {'class':'ipc-page-background'}).find('section', {'class':'ipc-page-section'}).find('div',{'role': 'tabpanel'})

result = soup.find('ul', {'class': 'ipc-metadata-list'}).find_all('li')

# print(type(result))
for i in result:
    element = i.find('h3', {'class':'ipc-title__text'})
    if element is not None: # if element: le aynı anlama geliyor.
        film = element.text
        print(film)