# Selenium bir web otomasyon kütüphanesidir.
# Selenium ile bir web sitesini ziyaret edip etkileşimde bulunabiliriz.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as op
import time

chrome_options = Options()
edge_options = op()
chrome_options.add_experimental_option("detach", True) # girilen urlyi (browser'ı) sürekli açık tutmak için. bu olmazsa kendi kendine kapanır.
edge_options.add_experimental_option("detach", True) # girilen urlyi sürekli açık tutmak için yapılması gerekir
# driver= webdriver.Chrome()
driver= webdriver.Chrome(options=edge_options)
url = "https://www.youtube.com/"
# url = "https://www.udemy.com/course/ielts-band-7-preparation-course/learn/lecture/23983958#content"

driver.get(url)
time.sleep(1)
driver.maximize_window()

url = "https://www.youtube.com/c/SaboSatran%C3%A7"
driver.get(url)
print(driver.title)
if "Sabo Satranç - YouTube" in driver.title:
    driver.save_screenshot(f"{driver.title}.png")
time.sleep(2)
driver.back() # sayfada geri gider
#driver.save_screenshot("deneme.png")
#print(driver.title)
#time.sleep(2)
# driver.close()

