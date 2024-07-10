from ders_17_1_Instagram_UserInfo import user, password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=self.chrome_options)
        self.followers = []
        self.username = username
        self.password = password
    
    def singIn(self):
        self.url = "https://www.instagram.com/"
        self.browser.get(self.url)
        
        time.sleep(2)
        username = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(self.username)
        password.send_keys(self.password)

        button = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        button.click()
    
    def verileriKaydetme(self):
        self.url ="https://www.instagram.com/accounts/onetap/?next=%2F"
        self.browser.get(self.url)
     
        self.browser.find_element(By.CLASS_NAME, 'x1i10hfl').click()

    def getFollowers(self):
        self.url ="https://www.instagram.com/mesutdnleyci/"
        self.browser.get(self.url)
       
        # self.browser.find_elements(By.CSS_SELECTOR, 'li.xl565be.x1m39q7l.x1uw6ca5.x2pgyrj')[1].find_element(By.TAG_NAME, "a").click()
        self.browser.find_element(By.CSS_SELECTOR, "a[href='/mesutdnleyci/followers/']").click()
        time.sleep(3)
        elements = self.browser.find_elements(By.CLASS_NAME, 'x1rg5ohu')

        for i in elements:
            link = i.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
            print(link)

instagram_account = Instagram(user, password)
instagram_account.singIn()
time.sleep(10)
instagram_account.verileriKaydetme()
time.sleep(10)
instagram_account.getFollowers()