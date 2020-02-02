from selenium import webdriver
from time import sleep
from json import load

with open("/home/julian/Projects/instagram_b0t/credentials.json") as f:
    credentials = load(f)

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@class = \"_2hvTZ pexuQ zyHYP\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@class=\"_2hvTZ pexuQ zyHYP\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@class = \"sqdOP  L3NKy   y3zKF     \"]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@class = \"aOOlW   HoLwm \"]").click()
        sleep(5)

InstaBot(credentials["user_id"],credentials["password"])