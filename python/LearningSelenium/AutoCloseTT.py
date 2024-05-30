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
linkname = input('Enter the word of the ticket(s) that you want to close: ')
page=input('Enter the page that you want to run the script on(1, 2 or 3?): ')
driver.maximize_window()

driver.find_element(By. XPATH, '//*[@id="username"]').send_keys(exchangeid)
driver.find_element(By. XPATH, '//*[@id="password"]').send_keys(exchangepw)
driver.find_element(By. XPATH, '/html/body/section/form/p[3]/button').click()
time.sleep(2)


#Clicking the page number
if page == 1:
    driver.find_element(By.XPATH, '//*[@id="ajaxLoadData"]/div[1]/a[2]').click()
if page == 2:
    driver.find_element(By.XPATH, '//*[@id="ajaxLoadData"]/div[1]/a[1]').click()
else:
    driver.find_element(By.XPATH, '//*[@id="ajaxLoadData"]/div[1]/a[3]').click()

#Clicking My Tickets
# driver.find_element(By.XPATH, '//*[@id="tabs"]/div[2]/div[1]/ul[2]/li[3]/p').click()
# time.sleep(2)
original_handle = driver.current_window_handle

#____________________________ Handwritten Code____________________________#
outage_links = driver.find_elements(By.PARTIAL_LINK_TEXT,linkname)

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
            form.send_keys('Outage', Keys.ENTER, Keys.TAB * 2, '0', Keys.TAB, '1', Keys.TAB, '0', Keys.TAB, 'Solved', Keys.TAB,
                           Keys.ENTER)
            driver.close()

        else:

            driver.close()
    except NoSuchElementException:
        driver.close()
driver.switch_to.window(original_handle)
driver.refresh()


    # Wait for confirmation or success message (implement robust waiting mechanism)
    # try:
    #     WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/ul/li[1]/span'))  # Replace with relevant selector
    #     )
    # except TimeoutException:
    #     print("Error closing ticket on tab", handle)
    #
    # # Close the current tab
    # driver.close()

# Switch back to the original tab (optional, if used in login)
# driver.switch_to.window(original_handle)

# Quit WebDriver
# driver.quit()


# original_handle = driver.current_window_handle
# all_handle = driver.window_handles
# for handle in all_handle:
#     if handle!=original_handle:
#         driver.switch_to.window(handle)
#         break






#___________________Accpeting and closing tickets______________________________

# driver.find_element(By.XPATH, '//*[@id="acceptTicket"]').click()
# time.sleep(2.5)
#
# wait = WebDriverWait(driver, 10)
# alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
#
# # Get the text of the alert (optional)
# alert_text = alert.text
# print("Alert text:", alert_text)
#
# # Accept (click OK) on the alert
# alert.accept()


#_________________Closing Ticket_________________________
# driver.find_element(By.XPATH, '//*[@id="close_btn"]').click()
# driver.find_element(By.XPATH, '//*[@id="closeForm"]')
# form = driver.find_element(By.XPATH, '//*[@id="closeForm"]/form/ul/li[2]/div/div[1]/input')
# form.send_keys('Outage', Keys.ENTER, Keys.TAB * 2, '0', Keys.TAB, '0', Keys.TAB, '10', Keys.TAB, 'Solved', Keys.TAB,
#                Keys.ENTER, Keys.CONTROL + W)