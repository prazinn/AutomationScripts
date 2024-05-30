from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.minimize_window()
trip_type = input('If your trip type is Round Trip, Press 1' '. If your trip type is One Way, Press 2: ')
where_from = input('Enter the place where you want to book the flight from: ')
where_to = input('Enter the place where you want to book the flight to: ')
# if trip_type == '1':
#     dep_date = input('Enter the Departure Date\033[1m E.g(Feb 1) \033[0m')
#     ret_date = input('Enter the Return Date')
# elif trip_type == '2':
#     dep_date = input('Enter the Departure Date\033[1m E.g(Feb 1) \033[0m')
driver.maximize_window()

driver.get('https://www.google.com/travel/flights')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]')

if trip_type == '2':
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div['
                        '1]/div/div[1]/div[1]/div/div/div/div[1]').click()
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div['
                        '1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]').click()
elif trip_type == '1':
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div['
                        '1]/div/div[1]/div[1]/div/div/div/div[1]').click()
    driver.find_element(By.XPATH,
                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div['
                        '1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[1]').click()

where_from_form = driver.find_element(By.XPATH, '//*[@id="i21"]/div[1]/div/div/div[1]/div/div/input')
where_from_form.clear()
time.sleep(1)
where_from_form.send_keys(where_from)
time.sleep(1)
where_from_form.send_keys(Keys.DOWN*2, Keys.TAB)
time.sleep(1)
# where_from_form.send_keys(Keys.TAB*3)

