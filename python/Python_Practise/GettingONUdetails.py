import time
from selenium import webdriver
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def close_success_message():
    success_window.destroy()
def login_to_website(username, password, customer):
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

        # Open the website
        driver.get('https://esupport.wlink.com.np')
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="form1"]/table/tbody/tr[5]/td[2]/input').click()

        # Wait for a moment to let the page load
        time.sleep(2)
        if driver.find_element(By.XPATH,'//*[@id="capture"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[3]/a'):
            # success_message = tk.messagebox.showinfo("Success", "Login successful!")
            #
            # # messagebox.showinfo("Success", "Login successful!")
            # root.after(1000, close_success_message)
            root.destroy()
        driver.find_element(By.XPATH, '//*[@id="capture"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[3]/a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="client_user_name"]').send_keys(customer)

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="client_user_name"]').send_keys(Keys.RETURN)

        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="view_ftth_details"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="view_onu_credentials_details"]').click()
        time.sleep(3)
        onu_username = driver.find_element(By.XPATH, '//*[@id="ONU-details"]/div/table/tbody/tr[2]/td[1]').text
        onu_pwd = driver.find_element(By.XPATH, '//*[@id="ONU-details"]/div/table/tbody/tr[2]/td[2]').text
        driver.find_element(By.XPATH, '//*[@id="ftth_info_new"]/div[2]/table[2]/tbody/tr[6]/td[1]/a').click()

        original_handle = driver.current_window_handle
        all_handle = driver.window_handles
        for handle in all_handle:
            if handle != original_handle:
                driver.switch_to.window(handle)
                break

        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(onu_username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(onu_pwd)

        driver.find_element(By.XPATH, '//*[@id="loginBT"]').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="div_menu_left"]/ul[2]/li[1]/a').click()

        driver.find_element(By.XPATH, '//*[@id="div_menu_left"]/ul[2]/li[6]/a').click()
        time.sleep(5)

        iframe = driver.find_element(By.XPATH, '//*[@id="mainFrame"]')
        driver.switch_to.frame(iframe)
        Wifi_SSID = driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div[2]/div/input').get_attribute("value")

        SSID_Status = driver.find_element(By.XPATH, '/html/body/div/form/div[5]/div[2]/div/select').get_attribute(
            'value')

        SSID_Broadcast = driver.find_element(By.XPATH, '/html/body/div/form/div[5]/div[2]/div/select').get_attribute('value')

    except Exception as e:
        messagebox.showerror("Error", f"Login/Password Invalid")

def on_submit():
    # Retrieve the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()
    customer = customer_entry.get()

    # Pass the credentials to the login function
    login_to_website(username, password, customer)

# Create main window
root = tk.Tk()
root.title("Esupport Login")

# Create frame for styling
style_frame = ttk.Frame(root)
style_frame.grid(row=2, column=2)

# Set style options
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
style.configure('TButton', background='#336699', foreground='black', font=('Arial', 12))

# Create labels and entry fields for username and password
username_label = ttk.Label(style_frame, text='Username:')
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = ttk.Entry(style_frame, width=40, font=('Arial', 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = ttk.Label(style_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = ttk.Entry(style_frame, show="*", width=40, font=('Arial', 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

customer_label = ttk.Label(style_frame, text='Customer Username:')
customer_label.grid(row=2, column=0, padx=10, pady=10)

customer_entry = ttk.Entry(style_frame, width=40, font=('Arial', 12))
customer_entry.grid(row=2, column=1, padx=10, pady=10)

# Create submit button
submit_button = ttk.Button(style_frame, text="Submit", command=on_submit)
submit_button.grid(row=3, columnspan=2, pady=10)

# Run the GUI
root.mainloop()


















# Create labels and entry fields for username and password
# tk.Label(root, text="Username").grid(row=0, column=0)
# username_entry = tk.Entry(root, width=50)
# username_entry.grid(row=0, column=1)
#
# tk.Label(root, text="Password").grid(row=1, column=0)
# password_entry = tk.Entry(root, width=50, show="*")
# password_entry.grid(row=1, column=1)
#
# # Create submit button
# submit_button = tk.Button(root, text="Submit", command=on_submit)
# submit_button.grid(row=2, columnspan=2)
#
# # Run the GUI
# root.mainloop()










