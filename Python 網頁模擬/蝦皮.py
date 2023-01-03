from selenium import webdriver
from time import sleep
import requests
import ddddocr
from webdriver_manager.chrome import ChromeDriverManager
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
while(1):
    username = ""
    password = ""
    url = "https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F"
    driver = webdriver.Chrome("/Users/Public/code/chromedriver")
    driver.get("")
    while True:
        try:
            driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[5]/div/div/button[2]").click()
            break
        except NoSuchElementException:
            sleep(0.01)
    while True:
        try:
            driver.find_element(By.NAME,"loginKey").send_keys(username)
            driver.find_element(By.NAME,"password").send_keys(password)
            break
        except NoSuchElementException:
            sleep(0.01)
    
    sleep(0.5)
    while True:
        try:
            driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/button").click()
            break
        except NoSuchElementException:
            sleep(0.5)
    while True:
        try:
            driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div/div[5]/div/div/button[2]").click()
            break
        except NoSuchElementException:
            sleep(0.01)
    while True:
        try:
            button = driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[1]/div/div[3]/div[2]/div[6]/button[4]")
            break
        except NoSuchElementException:
            sleep(0.1)
    driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[1]/div/div[3]/div[2]/div[6]/button[4]").click()
    sleep(0.2)
    while True:
        try:
            button = driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[3]/div[2]/div[9]/button")
            break
        except NoSuchElementException:
            sleep(0.1)
    driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[3]/div[2]/div[9]/button").click()
    sleep(180)
    break