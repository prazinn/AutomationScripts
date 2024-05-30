import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://tt.wlink.com.np')
driver.minimize_window()
#Entering the credentials for login
exchangeid = input('Enter username: ')
exchangepw = getpass.getpass('Enter password: ')
linkname = input('Enter the word of the ticket that you want to close: ')
print(linkname)
driver.maximize_window()

driver.find_element(By. XPATH, '//*[@id="username"]').send_keys(exchangeid)
driver.find_element(By. XPATH, '//*[@id="password"]').send_keys(exchangepw)
driver.find_element(By. XPATH, '/html/body/section/form/p[3]/button').click()
time.sleep(1.8)

driver.find_element(By.XPATH, '//*[@id="tabs"]/div[2]/div[1]/ul[2]/li[3]/p').click()
original_handle = driver.current_window_handle
time.sleep(2)
while True:
    outage_links = driver.find_elements(By.PARTIAL_LINK_TEXT, linkname)

    # Check if there are no elements on the page, break the loop
    if not outage_links:
        break

    # Click each link
    for link in outage_links:
        if link:
            link.click()

    all_handles = driver.window_handles

    # Skip the original tab, assuming it's where you logged in
    ticket_tabs = all_handles[1:]

    # Iterate through ticket tabs, close tickets, and close tabs
    for handle in ticket_tabs:
        driver.switch_to.window(handle)
        time.sleep(3)
        # Implement your ticket closure logic here (replace with your specific steps)
        try:
            if driver.find_element(By.XPATH, '//*[@id="acceptTicket"]'):
                driver.find_element(By.XPATH, '//*[@id="acceptTicket"]').click()
                time.sleep(2)

                wait = WebDriverWait(driver, 10)
                alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

                # Get the text of the alert (optional)
                alert_text = alert.text
                print("Alert text:", alert_text)

                # Accept (click OK) on the alert
                alert.accept()

                driver.find_element(By.XPATH, '//*[@id="close_btn"]').click()
                driver.find_element(By.XPATH, '//*[@id="closeForm"]')
                form = driver.find_element(By.XPATH, '//*[@id="closeForm"]/form/ul/li[2]/div/div[1]/input')
                form.send_keys('Outage', Keys.ENTER, Keys.TAB * 2, '0', Keys.TAB, '1', Keys.TAB, '0', Keys.TAB, 'Solved',
                               Keys.TAB,
                               Keys.ENTER)
                driver.close()
            else:
                driver.close()
        except NoSuchElementException:
            driver.close() #Closes the tab if XPATH is not found.

    # Switch back to the original window and refresh
    driver.switch_to.window(original_handle)
    driver.refresh()
