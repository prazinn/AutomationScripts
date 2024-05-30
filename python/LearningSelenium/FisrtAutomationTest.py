import time
import subprocess
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://esupport.wlink.com.np")
driver.maximize_window()
# driver.find_element(By.XPATH('//*[@id="username"]')).send_keys('prajin.shrestha')
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('prajin.shrestha')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('wlink123$#')
driver.find_element(By.XPATH, '//*[@id="form1"]/table/tbody/tr[5]/td[2]/input').click()
driver.find_element(By.XPATH, '//*[@id="capture"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="client_user_name"]').send_keys('prajin_fahome')

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="client_user_name"]').send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="view_ftth_details"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="view_onu_credentials_details"]').click()
time.sleep(3)
onu_username = driver.find_element(By.XPATH, '//*[@id="ONU-details"]/div/table/tbody/tr[2]/td[1]').text
print('The ONU Username is',onu_username)
onu_pwd = driver.find_element(By.XPATH, '//*[@id="ONU-details"]/div/table/tbody/tr[2]/td[2]').text
driver.find_element(By.XPATH, '//*[@id="ftth_info_new"]/div[2]/table[2]/tbody/tr[6]/td[1]/a').click()
print('The ONU Password is',onu_pwd)

original_handle = driver.current_window_handle
all_handle = driver.window_handles
for handle in all_handle:
    if handle!=original_handle:
        driver.switch_to.window(handle)
        break

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(onu_username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(onu_pwd)

driver.find_element(By.XPATH, '//*[@id="loginBT"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="div_menu_left"]/ul[2]/li[1]/a').click()

driver.find_element(By.XPATH, '//*[@id="div_menu_left"]/ul[2]/li[6]/a').click()
time.sleep(7)

iframe = driver.find_element(By.XPATH, '//*[@id="mainFrame"]')
driver.switch_to.frame(iframe)
Wifi_SSID = driver.find_element(By.XPATH,'/html/body/div/form/div[3]/div[2]/div/input').get_attribute("value")

bold= 'Your 2.4Ghz wifi Status:'

print('\033[1m'+ bold)
print('\033[0m'+"Your Wifi name is:", Wifi_SSID)
SSID_Status = driver.find_element(By.XPATH, '/html/body/div/form/div[5]/div[2]/div/select').get_attribute('value')
if SSID_Status == '1' :
    print("Your SSID Status is Enabled")
else :
    print("Your SSID Status is Disabled")

SSID_Broadcast = driver.find_element(By
                                     .XPATH, '/html/body/div/form/div[5]/div[2]/div/select').get_attribute('value')
if SSID_Broadcast == '1' :
    print("Your SSID is currently broadcasted")
else :
    print("Your SSID is not currently broadcasted")