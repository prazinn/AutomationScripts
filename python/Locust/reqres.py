from datetime import datetime
from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    host = 'https://reqres.in'
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get('/api/users?page=2')
        now = datetime.now()
        print(res.text)
        print(res.status_code)
        print(res.headers)
        print(now)

    @task
    def create_user(self):
        res = self.client.post('/api/users', data='''
        {"name": "Prajin",job": "QA"}
                         ''')
        now = datetime.now()
        print(now)
        print(res.text)
        print(res.status_code)
        print(res.headers)
