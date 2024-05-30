from locust import HttpUser, task, between
import requests

class MyUser(HttpUser):
    wait_time = between(1, 5)
    @task(1)
    def home(self):
        res = self.client.get("")