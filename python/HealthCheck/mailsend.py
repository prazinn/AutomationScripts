import smtplib

sender_email= "qcp_alert@worldlink.com.np"
receiver_email= "prajin.shrestha@worldlink.com.np"
message ="QCP ALERT"

try:
    server=smtplib.SMTP("smtp.wlink.com.np", 25)
    server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
    print("Test Mail")
except Exception as e:
    print(f"Error sending mail:{e}")
finally:
    if server:
        server.quit()