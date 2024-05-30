import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://monitoring.wlink.com.np')
driver.maximize_window()

#Using Credentials for Login.
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/input[1]').send_keys('prajin.shrestha')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/input[2]').send_keys('wlink123$#')
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/ul/li[2]/ul/li[2]/button').click()


time.sleep(4)
#Clicking Support Section which is in Hover

reports = driver.find_element(By.XPATH, '/html/body/div[1]/aside/section/ul/li[6]/a/i[1]')
support_dashboard = driver.find_element(By.XPATH, '/html/body/div[1]/aside/section/ul/li[6]/ul/li[2]/a/span')

actions = ActionChains(driver)
actions.move_to_element(reports).move_to_element(support_dashboard).click().perform()

today = datetime.date.today()
print(today.strftime("%m/%d/%Y"))
current=today.strftime("%m/%d/%Y")

# #Clicking Problemwise trend
driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="startdate1"]').send_keys(current)
driver.find_element(By.XPATH, '//*[@id="enddate1"]').send_keys(current)
driver.find_element(By.XPATH, '//*[@id="myform1"]/div[1]/div[3]/select').send_keys('Phone Support CSR')
driver.find_element(By.XPATH,'//*[@id="myform1"]/button').click()

time.sleep(5)
iframe = driver.find_element(By.XPATH, '//*[@id="data-body1"]/div')
iframe = driver.find_element(By.XPATH, '//*[@id="data-body1"]/div/div[2]')
driver.find_element(By.XPATH, '//*[@id="get-hourwise"]/thead/tr/th[2]').click()

driver.execute_script("window.open('', '_blank');")
driver.switch_to.window(driver.window_handles[1])

# driver.get('https://ameyoapp.wlink.com.np:8443/app/')
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="gwt-uid-1"]').send_keys("prajin.shrestha@worldlink.com.np")
# driver.find_element(By.XPATH,'//*[@id="gwt-uid-2"]').send_keys("wlink123$#")
# driver.find_element(By.XPATH,'//*[@id="ameyo-body"]/div[3]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/form/div/div[7]/div/button').click()
# time.sleep(1.75)
# if driver.find_element(By.XPATH,'//*[@id="automationButton1"]/span'):
#     driver.find_element(By.XPATH,'//*[@id="automationButton1"]/span').click()
