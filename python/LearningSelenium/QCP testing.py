import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver.get('https://login.wlink.com.np')
# driver.maximize_window()
# driver.find_element(By.XPATH, '/html/body/main/div/form[1]/div[2]/div/input').send_keys('prajin.shrestha')
# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('wlink123$#')
# driver.find_element(By.XPATH, '/html/body/main/div/form[1]/button/span[1]').click()
# driver.execute_script("window.open('', '_blank');") new tab command
# driver.switch_to.window(driver.window_handles[1])
time.sleep(1.5)

driver.maximize_window()

driver.get("https://fa-tracking.wlink.com.np/qcp/dashboard")
driver.find_element(By.XPATH, '/html/body/main/div/form[1]/div[2]/div/input').send_keys('prajin.shrestha')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('wlink123$#')
driver.find_element(By.XPATH, '/html/body/main/div/form[1]/button/span[1]').click()
num_refreshes = 4

# Loop to refresh the page with a delay
for _ in range(num_refreshes):
    time.sleep(2)
    driver.refresh()

iframe = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/a[4]/li/div').click()
# driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/p/svg/path').click()

