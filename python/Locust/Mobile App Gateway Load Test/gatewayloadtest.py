from locust import HttpUser, SequentialTaskSet, task, between
from datetime import datetime
import json

# Load the username and token data from a specified JSON file path
def load_user_data(file_path):
    with open(file_path, 'r') as file:
        user_data = json.load(file)
    return user_data
def gettimestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return timestamp

# Specify the path to the JSON file
file_path = r'C:\Python-Selenium\PythonSeleniumProject1\pythonProject1\Locust\pythonProject1\user_data.json'

# Load user data from the JSON file
user_data = load_user_data(file_path)

class UserBehavior(SequentialTaskSet):
    def on_start(self):
        # Assign user data to each Locust user
        self.user_data = user_data.copy()

    @task #1
    def get_online_devices(self):
        if self.user_data:
            user = self.user_data.pop(0)  # Get the next user from the list
            endpoint = f"/v1/appEservice/ftth/{user['username']}/online_devices"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            timestm=gettimestamp()
            print(f"{timestm} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #2
    def get_online_device_new(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/online_devices_new"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #3
    def get_device_status(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/device_status"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #4
    def get_device_online_status(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/device_online_status"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #5
    def get_nokia_radio_wan(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/view_nokia_radio"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #6
    def get_ONU_info(self):
        if self.user_data
        user= self.user_data.pop(0)
        endpoint = f"/v1/appEservice/ftth/{user['username']}/onu_info"
        response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
        print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
        # Add the user back to the end of the list to reuse
        self.user_data.append(user)
    @task #7
    def get_is_nwcc_enabled(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/is_nwcc_enabled"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #8
    def get_beacon_connected_list(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/get_beacon_connected_list"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #9
    def get_view_nokia_mac_acl (self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/device_filtering/{user['username']}/fetch"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #10
    def get_channel_mode (self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/channel/mode"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #11
    def get_nearby_scan_list (self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/nearby_scan_list"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #12
    def get_available_list(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ftth/{user['username']}/available_list"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    #END OF FTTH


    #LOGIN APIs Task 13
    @task #13
    def get_profile(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/profile/me"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #14
    def get_social(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/setSocialLoginActivationStatus"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task #15
    def get_check_app_version(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/app_version/android"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #16
    def get_company_contacts(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/company_contacts"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #17
    def get_document_types(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/get_user_documents"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #18
    def get_image(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/get_images"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #19
    def get_is_allowed_logout(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/is_allow_to_logout"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #20
    def get_ecg(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/ecg"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)

     #_______________FTTH service check Task 21________________
    @task() #21
    def get_ftth_service_check(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/service_available/27.7089543/85.2849333"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #22
    def get_check_nt_hashed(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/check_nt_hash/{user['username']}"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #23
    def get_kyc(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/kyc/{user['username']}/stauts"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)

#______________SIP VoIP Task 24 to Task 27 ___________
    @task() #24    
    def get_sip_support_details(self):   
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/sip/sip_support"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    @task() #25
    def get_suggested_numbers(self):
        if self.user_data:
            user = self.user_data.pop(0)
            endpoint = f"/v1/appEservice/sip/{user['username']}/numbers/suggested"
            response = self.client.get(endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{gettimestamp} Status Code: {response.status_code}, Username: {user['username']}")
            # Add the user back to the end of the list to reuse
            self.user_data.append(user)
    
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "https://custmobileapp-gateway.wlink.com.np"

