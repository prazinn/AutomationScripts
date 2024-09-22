import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.minimize_window()
#Taking username to create instant follow up
username = input('Enter Username to create instant follow up: ')
driver.maximize_window()
#Logging in to CFU
driver.get('https://cfu.wlink.com.np')
driver.maximize_window()
driver.find_element(By.XPATH, '/html/body/main/div/form[1]/div[2]/div/input' ).send_keys('prajin.shrestha')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Wlink123$#')
driver.find_element(By.XPATH, '/html/body/main/div/form[1]/button/span[1]').click()
#Login Complete

# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/header/div/button[1]').click()
time.sleep(2.5)
# driver.find_element(By.XPATH, '/html/body/div[4]/div[3]')
# driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]')
# driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div[1]/ul/a[4]/div[2]/span').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/button/span[1]').click()
time.sleep(1.5)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div/div[1]/button/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(username)
driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[3]/button[2]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="problemCategory"]').click()
# driver.find_element(By.XPATH, '//*[@id="problemCategory"]')
element=driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul')
element.send_keys(Keys.ARROW_DOWN*3, Keys.ENTER, Keys.TAB, Keys.ARROW_DOWN*12, Keys.ENTER, Keys.TAB*2, Keys.RETURN)
time.sleep(2)
