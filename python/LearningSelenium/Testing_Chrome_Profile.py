from undetected_chromedriver2 import Chrome, ChromeOptions
import time

profile_directory = "/home/apoorba/.config/google-chrome/Default"
chrome_path = "/usr/bin/chromedriver"  # Ensure this path is accurate

chrome_options = ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_directory}")
chrome_options.add_argument("--start-maximized")

driver = Chrome(driver_executable_path=chrome_path, options=chrome_options)

driver.get("https://www.google.com")
time.sleep(10)
driver.quit()