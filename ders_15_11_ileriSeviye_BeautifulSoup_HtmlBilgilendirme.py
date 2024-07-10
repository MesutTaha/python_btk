html_doc = """
<!-- İLK İŞLEM İÇİN ÖNCE CTRL+1 (!) İŞARETİNİ KOY BAŞLANGIÇ İŞLEMŞERİNİ YAPIYOR-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id="header"><!-- başlık-->
        Python Kursu
    </h1>
    <div class="grup 1"><!--Grup oluşturmak için-->

    
        <h2>
            Programlama
        </h2>
        <ul><!-- liste-->
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup 2"><!--Grup oluşturmak için-->

        <h2>
            Modüller
        </h2>
        <ul><!-- liste-->
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="th2.png">
    <a class="sister" href="http://example1.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example3.com/lacie" id="link2">Lacie</a>
</body>
</html>

"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') # Parse: Ayrıştırmak

result = soup.prettify()
result = soup.title # <title>ilk web sayfam</title>
result = soup.head
result = soup.title.name # title
result = soup.title.string # ilk web sayfam

result = soup.h2 # sadece ilk h2 bilgilerini getirir
result = soup.find_all('h2') # tüm h2 bilgilerini getirir
result = soup.find_all('h2')[0] # sadece 0. indexteki h2 bilgilerini getirir
result = soup.find_all('h2')[1] # sadece 1. indexteki h2 bilgilerini getirir
result = soup.find_all('div')[0].ul
result = soup.find_all('div')[0].ul.li # <li>Menü 1</li>
result = soup.find_all('div')[0].ul.find_all('li') # [<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]
result = soup.div.findChildren()
result = soup.div.findNextSibling()

result = soup.find_all('a')

for link in result:
    # print(link)
    # <a class="sister" href="http://example1.com/lacie" id="link2">Lacie</a>
    # <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>
    # <a class="sister" href="http://example3.com/lacie" id="link2">Lacie</a>
    print(link.get('href'))
    # http://example1.com/lacie
    # http://example2.com/lacie
    # http://example3.com/lacie
