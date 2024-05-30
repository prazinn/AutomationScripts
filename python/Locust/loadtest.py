from locust import HttpUser, constant, task, between
from datetime import datetime

TOKEN ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vY3VzdG1vYmlsZWFwcC1nYXRld2F5LndsaW5rLmNvbS5ucC92MS9hcHBFc2VydmljZS9sb2dpbiIsImlhdCI6MTcxNjM4OTAwOSwiZXhwIjoxNzE2NDc1NDA5LCJuYmYiOjE3MTYzODkwMDksImp0aSI6IlZmVDZlVjg2U0NNeGwxVDAiLCJzdWIiOiIxNzA4MzgwOSIsInBydiI6ImQ1ZmU0MDc5ZmRkZmUyM2YyNjkyMWI5ZmNjOTg1MGUzMGNiN2IzNTciLCJjZWxsX251bWJlciI6ImxtazQ5dEhrNmxpTGtvZmpIME5NVkE9PSJ9.vHE_R6XUUGHjREHg0LK0HA6z9xhY-Ns4Tt40i1NiyN4'
headers = {"Authorization": f"Bearer {TOKEN}"}

TOKEN1 ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vY3VzdG1vYmlsZWFwcC1nYXRld2F5LndsaW5rLmNvbS5ucC92MS9hcHBFc2VydmljZS9sb2dpbiIsImlhdCI6MTcxNjM4OTE3NSwiZXhwIjoxNzE2NDc1NTc1LCJuYmYiOjE3MTYzODkxNzUsImp0aSI6InN6Nm52V29sWHFtbkpReE0iLCJzdWIiOiIxNzA4MzgxMCIsInBydiI6ImQ1ZmU0MDc5ZmRkZmUyM2YyNjkyMWI5ZmNjOTg1MGUzMGNiN2IzNTciLCJjZWxsX251bWJlciI6IlZ5V2s0WUM5a0tKeVI2QzZZZ0diRUE9PSJ9.EZ6s-CAw-dEKjnKCreqbhyxs5xRqZaChBKNpihS--J8'
headers1 = {"Authorization": f"Bearer {TOKEN1}"}


class FTTH(HttpUser):
    host = "https://custmobileapp-gateway.wlink.com.np"
    wait_time = between(2, 4)


    def on_error(self, error):
        print(f"Error encountered: {error}")
        super().on_error(error)  # Call the default error handling

    @task() #53
    def get_customer_full_details(self):
        get_customer_full_details = self.client.get('/v1/appEservice/customer/phonesupport_kalash/full_detail', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details')
        print(get_customer_full_details)   

    @task()
    def get_customer_full_details1(self):
        get_customer_full_details1 = self.client.get('/v1/appEservice/customer/prajin_fahome/full_detail', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details')
        print(get_customer_full_details1)  

    @task()
    def get_customer_full_details2(self):
        get_customer_full_details2 = self.client.get('/v1/appEservice/customer/raju_poudel_mc/full_detail', headers=headers1)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details raju_poudel_mc')
        print(get_customer_full_details2) 
    
    @task()
    def get_customer_full_details3(self):
        get_customer_full_details3 = self.client.get('/v1/appEservice/customer/pramodk_fkkvt/full_detail', headers=headers1)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details pramodk_fkkvt')
        print(get_customer_full_details3)

    @task()
    def get_customer_full_details4(self):
        get_customer_full_details4 = self.client.get('/v1/appEservice/customer/pramodk_home/full_detail', headers=headers1)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details pramodk_home')
        print(get_customer_full_details4)