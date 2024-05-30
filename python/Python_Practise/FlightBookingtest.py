from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_flights(origin, destination, departure_date, return_date=None):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open Google Flights
    driver.get("https://www.google.com/flights")

    # Wait for page to load
    time.sleep(2)

    # Find and fill out the origin input field
    origin_input = driver.find_element(By. XPATH, "//input[@placeholder='Where from?']")
    origin_input.clear()
    origin_input.send_keys(origin)
    time.sleep(1)
    origin_input.send_keys(Keys.RETURN)

    # Find and fill out the destination input field
    destination_input = driver.find_element(By. XPATH,"//input[@placeholder='Where to?']")
    destination_input.clear()
    destination_input.send_keys(destination)
    time.sleep(1)
    destination_input.send_keys(Keys.RETURN)

    # Find and fill out the departure date input field
    departure_date_input = driver.find_element(By. XPATH,"//input[@data-flt-ve='dates-oneway-depart']")
    departure_date_input.clear()
    departure_date_input.send_keys(departure_date)
    time.sleep(1)
    departure_date_input.send_keys(Keys.RETURN)

    # If return date is provided, fill out the return date input field
    if return_date:
        return_date_input = driver.find_element(By. XPATH,"//input[@data-flt-ve='dates-oneway-return']")
        return_date_input.clear()
        return_date_input.send_keys(return_date)
        time.sleep(1)
        return_date_input.send_keys(Keys.RETURN)

    # Click the search button
    search_button = driver.find_element(By. XPATH,"//button[@jsname='LgbsSe']")
    search_button.click()

    # Wait for search results to load
    time.sleep(5)

    # Print the URL of the search results page
    print("Search Results URL:", driver.current_url)

    # Close the browser window
    driver.quit()

# Get user input for origin, destination, and departure date
origin = input("Enter origin: ")
destination = input("Enter destination: ")
departure_date = input("Enter departure date (YYYY-MM-DD): ")
return_date = input("Enter return date (optional, leave blank for one-way): ")

# Call the search_flights function with user input
search_flights(origin, destination, departure_date, return_date)
