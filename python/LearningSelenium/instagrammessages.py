from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://instagram.com")
driver.maximize_window()

driver.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('prazinnnn._')