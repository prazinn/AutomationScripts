from locust import HttpUser, constant, task, between


class dummy(HttpUser):
    host = "https://custmobileappgw-staging.wlink.com.np"
    wait_time = between(2, 4)

    @task(1)
    def get_users(self):
        getdata = self.client.get('/dummy/getDetail/prajin_fahome')
        print("THIS IS THE RESPONSE OF GETTING SINGLE USER")
        print(getdata)

    @task(2)
    def getall_users(self):
        get_all = self.client.get('/dummy/getAllUserDetails')
        print("THIS IS THE RESPONSE OF GETTING ALL USER")
        print(get_all)

    @task(3)
    def create_user(self):
        data = self.client.post('/dummy/updateReadUserDetail/prajin_fahome')
        print("THIS IS THE RESPONSE OF POST")
        print(data)
        print(data.headers)
