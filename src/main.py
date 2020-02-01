from selenium import webdriver
from time import sleep
from json import load
from lxml import etree
import gnugp

with open("/home/julian/Projects/instagram_b0t/credentials.json.gpg") as f:
    credentials = load(f)

with open("/home/julian/Projects/instagram_b0t/src/xpath.txt") as f1:
    print(f1)




# class InstaBot:
#     def __init__(self, username, pw):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://instagram.com")
#         sleep(5)

print(credentials)

#InstaBot(credentials["user_id"],credentials["password"])