# Detaylı bilgi için https://selenium-python.readthedocs.io/locating-elements.html#
# adresini ziyaret et (sondaki # işareti linke dahil)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://tr.aliexpress.com/?gatewayAdapt=glo2tur" # https://www.google.com https://github.com/ https://music.youtube.com/ 
driver.get(url) 
driver.maximize_window()
time.sleep(1)
searchInput = driver.find_element(By.XPATH, '//input[@id="search-words"]') # //textarea[@id="APjFqb"] [@id="input"]  normalde XPATH //*[@id="input"] şeklinde geliyor, (*) yerine incele kısmında belirtilen özelliği yazman lazım örn: //input[@id="search-words"], //textarea[@id="APjFqb"], //input[@id="input"]
time.sleep(1)
searchInput.send_keys("bilgisayar")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR, "list--gallery--C2f2tvm search-item-card-wrapper-gallery a h3")

for elements in results:
    print(elements.text)


driver.close()