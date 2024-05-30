from locust import HttpUser, task, between, constant


class MyUser(HttpUser):
    # Set a short wait time between user requests
    wait_time = constant(1)  # In milliseconds, adjust for desired ramp-up

    # Explicitly specify the base URL for API requests
    host = "https://custmobileappgw-staging.wlink.com.np"

    # Define error handling for potential exceptions
    def on_error(self, error):
        print(f"Error encountered: {error}")
        super().on_error(error)  # Call the default error handling

    @task
    def get_detail(self):
        url = "/dummy/getDetail/prajin_fahome"
        # Removed API key related code

    @task
    def get_all_users(self):
        url = "/dummy/getAllUserDetails"
        # Removed API key related code

    @task(weight=2)  # Execute twice as often as other tasks
    def post_wholesome(self):
        url = "/dummy/wholesome"
        # Removed API key related code
        data = {"key": "value"}  # Example data for POST request
        self.client.post(url, headers={}, json=data)


# Set number of users and ramp-up time
num_users = 1000
ramp_up_time = 5  # Adjust for desired ramp-up speed

if __name__ == "__main__":
    from locust import web

    web.run(MyUser, web_port=8089, users=num_users, spawn_rate=num_users / ramp_up_time)
