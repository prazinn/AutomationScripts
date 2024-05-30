from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://tt.wlink.com.np')

driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '/html/body/section/form/p[3]/button').click()

