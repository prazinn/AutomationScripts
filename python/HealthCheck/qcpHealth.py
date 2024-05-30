import smtplib

import requests
from datetime import datetime
import time

# Replace with your API details
API_URL = "https://fa-tracking.wlink.com.np/qcp/api/v3/health-service"
CONNECTION_LIMIT = 1

# Replace with your email details
SENDER_EMAIL = "QCP_ALERT@worldlink.com.np"
RECEIVER_EMAIL = "prajin.shrestha@worldlink.com.np"

# Replace with your mail server details (if not using Gmail)
MAIL_SERVER = "smtp.wlink.com.np"  # Replace with your server hostname or IP (if using your server)
MAIL_SERVER_PORT = 25  # Replace with port number (if using your server)
USE_SSL = False  # Set to True if your server requires SSL (if using your server)


def fetch_api_data():
    """Fetches data from the health check API."""

    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise error for non-200 status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None


def save_to_file(data, filename="QCP_CHECK.txt"):
    """Saves the provided data to a text file with the given filename and prepends a timestamp."""

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
    data_with_timestamp = f"{timestamp}\n{data}"  # Prepend timestamp to data

    try:
        # Open the file in append mode ('a')
        with open(filename, "a") as file:
            file.write(data_with_timestamp + "\n")  # Append with newline
        print(f"API response appended to: {filename}")
    except OSError as e:
        print(f"Error saving data to file: {e}")


def read_connection_count(filename):
    """Reads the connection count from the saved response file."""

    try:
        with open(filename, "r") as file:
            data = file.read()
        connection_count = None
        # Assuming connection_count is still on a separate line after timestamp
        for line in data.splitlines():
            if line.startswith("connection_count"):
                connection_count = int(line.split(":")[1].strip())
                print({connection_count})
                break
        return connection_count

    except (OSError, ValueError) as e:
        print(f"Error reading connection count: {e}")
        return None


def send_email_alert(connection_count):
    """Sends an email notification if the connection count exceeds the limit."""

    global server
    message = f"Health check alert: Connection count at {connection_count} exceeding limit of {CONNECTION_LIMIT} at {datetime.now()}"

    try:
        # Connect to the mail server (adjust based on your server configuration)
        if USE_SSL:
            server = smtplib.SMTP_SSL(smtp.wlink.com.np, 25)
        else:
            server = smtplib.SMTP('smtp.wlink.com.np', 25)
        # Include authentication if required by your server
        # server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Uncomment if needed
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.encode('utf-8'))
        print(f"Email sent using your mail server: {message}")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        if server:
            server.quit()  # Ensure proper server connection closure


def main():
    """Runs the main logic of fetching data, checking connection count, and sending alerts."""

    while True:
        api_data = fetch_api_data()
        if api_data is not None:
            save_to_file(api_data)
            connection_count = read_connection_count("QCP_CHECK.txt")
            if connection_count is not None and connection_count > CONNECTION_LIMIT:
                send_email_alert(connection_count)

        # Schedule next check in 30 minutes (1800 seconds)
        time.sleep(1800)


if __name__ == "__main__":
    main()
