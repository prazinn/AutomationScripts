import requests
import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime

API_URL = 'https://fa-tracking.wlink.com.np/qcp/api/v3/health-service'
CONNECTION_LIMIT= 250

SENDER_EMAIL = 'QCP_AERT@worldlink.com.np'
RCEIVER_EMAIL = 'prajin.shrestha@worldlink.com.np'


def send_email(message):
    """Sends an email notification"""
    email = MIMEText(message, 'plain')
    email['subject']='HEALTH CHECK ALERT- HIGH CONNECTION COUNT'
    email['From'] = SENDER_EMAIL
    email['To'] = RCEIVER_EMAIL
    server = smtplib.SMTP('smtp.wlink.com.np', 25)


def check_connections():
    """    Fetches connection count from the API and sends email if over limit."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        print (data)

        connection_count = data.get('')
        if connection_count is None:
            print(f"API response didn't contain 'connection count' key")
            return
        if connection_count > CONNECTION_LIMIT:
            message = f"HEALTH CHECK ALERT: CONNECTION COUNT at {connection_count} EXCEEDING LIMIT OF {CONNECTION_LIMIT} at {datetime.now()}"
            send_email(message)
            print(f'EMAIL SENT SUCESSFULLY to {RCEIVER_EMAIL}')
        else:
            print(f'Connection count : {connection_count}(Within Limit')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
if __name__ == "__main__":
    while True:
        check_connections()
        # Schedule next check in 30 minutes (1800 seconds)
        time.sleep(1800)
