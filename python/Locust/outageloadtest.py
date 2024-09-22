from locust import HttpUser, constant, task, between
from datetime import datetime

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsb2dpbi53bGluay5jb20ubnAiLCJpYXQiOjE3MjU1MzI3MjAsImV4cCI6MTkyNjg0NTQyOSwibmJmIjoxNzI2ODA5NDI5LCJqdGkiOiJJbEpxR3phVktNWmVyanZlIiwic3ViIjoiYXBvb3JiYS5yYW5hIiwiYXVkIjoiZmEtdHJhY2tpbmcud2xpbmsuY29tLm5wIn0.v9X1_XM0NbmN-EEOwvaOub8uo-L6QiF-yf0Cy3Is5Ss'
headers = {"Authorization": f"Bearer {TOKEN}"}

class Outage(HttpUser):
    host='https://dev-02.wlink.com.np/rapoorba/pgOutage/index.php'
    wait_time = between(2, 4)

    def on_error(self, error):
        print(f"Error Encounted: {error}")
        super().on_error(error)

    @task
    def hit_apis(self):
        self.client.get('/api/getOutageUpdateData?subject=templates&state=Ack1')