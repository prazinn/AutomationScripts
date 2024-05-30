from locust import HttpUser, SequentialTaskSet, task, between
from datetime import datetime
import json

def load_user_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

file_path = r'user_data.json'
user_data = load_user_data(file_path)

endpoints = [
    "/v1/appEservice/ftth/{username}/online_devices",
    "/v1/appEservice/ftth/{username}/online_devices_new",
    "/v1/appEservice/ftth/{username}/device_status",
    "/v1/appEservice/ftth/{username}/device_online_status",
    "/v1/appEservice/ftth/{username}/view_nokia_radio",
    "/v1/appEservice/ftth/{username}/onu_info",
    "/v1/appEservice/ftth/{username}/is_nwcc_enabled",
    "/v1/appEservice/ftth/{username}/get_beacon_connected_list",
    "/v1/appEservice/device_filtering/{username}/fetch",
    "/v1/appEservice/ftth/{username}/channel/mode",
    "/v1/appEservice/ftth/{username}/nearby_scan_list",
    "/v1/appEservice/ftth/{username}/available_list",
    "/v1/appEservice/profile/me",
    "/v1/appEservice/setSocialLoginActivationStatus",
    "/v1/appEservice/app_version/android",
    "/v1/appEservice/company_contacts",
    "/v1/appEservice/get_user_documents",
    "/v1/appEservice/get_images",
    "/v1/appEservice/is_allow_to_logout",
    "/v1/appEservice/ecg",
    "/v1/appEservice/service_available/27.7089543/85.2849333",
    "/v1/appEservice/check_nt_hash/{username}",
    "/v1/appEservice/kyc/{username}/stauts",
    "/v1/appEservice/sip/sip_support",
    "/v1/appEservice/sip/{username}/numbers/suggested",
    "/v1/appEservice/sip/{username}/numbers/available/200",
    "/v1/appEservice/sip/{username}/subscription",
    "/v1/appEservice/support/{username}/all_tickets_with_compensation",
    "/v1/appEservice/support/{username}/problem_types",
    "/v1/appEservice/support/{username}/get_graph",
    "/v1/appEservice/support/{username}/outage",
    "/v1/appEservice/support/{username}/get-pending-tickets",
    "/v1/appEservice/support/{username}/field_location_reports/1",
    "/v1/appEservice/support/{username}/field/track/device_id",
    "/v1/appEservice/wl-benefits/default-outlets",
    "/v1/appEservice/wl-benefits/outlets-by-filter/googleMap/9.90866,9.875565",
    "/v1/appEservice/wl-benefits/outlet-detail/6204",
    "/v1/appEservice/wl-benefits/background-configuration",
    "/v1/appEservice/available_free_wifi_zones/27.6711212/85.3446311",
    "/v1/appEservice/customer/{username}/profile",
    "/v1/appEservice/customer/{username}/realtime_bw",
    "/v1/appEservice/customer/{username}/info",
    "/v1/appEservice/customer/{username}/transactions",
    "/v1/appEservice/customer/{username}/transactions_with_renew_detail",
    "/v1/appEservice/customer/{username}/account",
    "/v1/appEservice/customer/{username}/fup_flag_notifier",
    "/v1/appEservice/customer/{username}/fup_status",
    "/v1/appEservice/customer/{username}/documents",
    "/v1/appEservice/customer/{username}/documents/pdf",
    "/v1/appEservice/customer/{username}/show_bandwidth?pay_plan=1254",
    "/v1/appEservice/customer/{username}/internet_usage/2024-01-01/2024-03-24",
    "/v1/appEservice/customer/{username}/nt_hash_credentials",
    "/v1/appEservice/customer/{username}/full_detail",
    "/v1/appEservice/diagnostic/{username}/detail-by-requestid/64887f80b24b8f0cfa2a5215",
    "/v1/appEservice/diagnostic/{username}/detail-by-username",
    "/v1/appEservice/diagnostic/{username}/diagnostic-summary-report/64887f80b24b8f0cfa2a5215",
    "/v1/appEservice/nettv/{username}/info",
    "/v1/appEservice/nettv/{username}/payment/stb-details",
    "/v1/appEservice/nettv/{username}/payment/stb-box-details/00226D9E5518",
    "/v1/appEservice/refer_offer/{username}/refer_offer_banner",
    "/v1/appEservice/refer_offer/{username}/refer_offer_terms_conditions",
    "/v2/boost/{username}/isEligible",
    "/v2/boost/{username}/validToProvision",
    "/v2/boost/{username}/package",
    "/v2/boost/{username}/daysremaining",
    "/v2/payment/{username}/payment-details",
    "/v2/notification/{username}",
]
class UserBehavior(SequentialTaskSet):
    def on_start(self):
        self.user_data = user_data.copy()
    def perform_task(self, endpoint):
        if self.user_data:
            user = self.user_data.pop(0)
            formatted_endpoint = endpoint.format(username=user['username'])
            response = self.client.get(formatted_endpoint, headers={"Authorization": f"Bearer {user['token']}"})
            print(f"{get_timestamp()} Status Code: {response.status_code}, Username: {user['username']}")
            self.user_data.append(user)
    @task
    def run_tasks(self):
        for endpoint in endpoints:
            self.perform_task(endpoint)
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "https://custmobileapp-gateway.wlink.com.np"