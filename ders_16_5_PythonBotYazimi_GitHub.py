from ders_16_5_PythonBotYazimi_GitHubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class GitHub:
    def __init__(self, username, password):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=self.chrome_options)
        self.username = username
        self.password = password
        self.url  = "https://github.com/login"
        self.followers = []

    def signIn(self):
        self.browser.get(self.url)
        time.sleep(2)

        username = self.browser.find_element(By.XPATH, '//input[@id="login_field"]')
        password = self.browser.find_element(By.XPATH, '//input[@id="password"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        button = self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
        # button.send_keys(Keys.ENTER)
        button.click() # üstte yorum satırındaki kodla da bu kodla da butona tıklanabiliyor.
    
    def getFollowers(self):
        self.url = "https://github.com/MesutTaha?tab=followers"
        self.browser.get(self.url)
        time.sleep(1)
        self.loadFollowers()

        
    
    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed") # (d-table table-fixed) başına ve ortasına nokta koymayı unutma
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text) # span.f4.Link--primary şeklinde de yazılabilir

github = GitHub(username, password)
github.signIn()
github.getFollowers()
print(github.followers)