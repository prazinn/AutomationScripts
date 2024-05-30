from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_task(self):
        self.client.get("/")

    # You can define more tasks here if needed
    # Just decorate them with @task and implement their behavior
    '''
class MyUser(HttpUser):
    wait_time = between(1, 5)  # adjust as needed

    @task
    def my_task(self):
        self.client.get("/your-endpoint")

    # For HTTPS requests, uncomment below and replace host with your HTTPS URL
    # use_tls = True
    # host = "https://your-https-host.com"
'''