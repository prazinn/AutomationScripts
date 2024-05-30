from locust import HttpUser, constant, task, between
from datetime import datetime


TOKEN ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vZ3dtb2JpbGUvdjEvYXBwRXNlcnZpY2UvbG9naW4iLCJpYXQiOjE3MTY3NDIzNTAsImV4cCI6MTcxNjgyODc1MCwibmJmIjoxNzE2NzQyMzUwLCJqdGkiOiJiZWszd3Bza3NDN2lnZWV4Iiwic3ViIjoiMTcxODc3MzQiLCJwcnYiOiJkNWZlNDA3OWZkZGZlMjNmMjY5MjFiOWZjYzk4NTBlMzBjYjdiMzU3IiwiY2VsbF9udW1iZXIiOiJsbWs0OXRIazZsaUxrb2ZqSDBOTVZBPT0ifQ.6P-CeslmGxvagVXG0yzm1d_HzNq4Adtm5tSYv6fAy0I'
headers = {"Authorization": f"Bearer {TOKEN}"}

class FTTH(HttpUser):
    host = "https://custmobileapp.worldlink.com.np/app"
    wait_time = between(2, 4)

    def on_error(self, error):
        print(f"Error encountered: {error}")
        super().on_error(error)  # Call the default error handling

    @task
    def execute_tasks(self):
        urls = [
            '/v1/appEservice/ftth/phonesupport_kalash/online_devices',
            '/v1/appEservice/ftth/phonesupport_kalash/online_devices_new',
            '/v1/appEservice/ftth/phonesupport_kalash/device_status',
            '/v1/appEservice/ftth/phonesupport_kalash/device_online_status',
            '/v1/appEservice/ftth/phonesupport_kalash/view_nokia_radio',
            '/v1/appEservice/ftth/phonesupport_kalash/onu_info',
            '/v1/appEservice/ftth/phonesupport_kalash/is_nwcc_enabled',
            '/v1/appEservice/ftth/phonesupport_kalash/get_beacon_connected_list',
            '/v1/appEservice/device_filtering/phonesupport_kalash/fetch',
            '/v1/appEservice/ftth/phonesupport_kalash/channel/mode',
            '/v1/appEservice/ftth/phonesupport_kalash/channel/near-by-scan-list',
            '/v1/appEservice/ftth/phonesupport_kalash/channel/available-list',
            '/v1/appEservice/me',
            '/v1/appEservice/setSocialLoginActivationStatus',
            '/v1/appEservice/app_version/android',
            '/v1/appEservice/company_contacts',
            '/v1/appEservice/get_user_documents',
            '/v1/appEservice/get_images',
            '/v1/appEservice/is_allow_to_logout',
            '/v1/appEservice/ecg',
            '/v1/appEservice/service_available/27.7089543/85.2849333',
            '/v1/appEservice/check_nt_hash/phonesupport_kalash',
            '/v1/appEservice/kyc/phonesupport_kalash/status',
            '/v1/appEservice/sip/sip_support',
            '/v1/appEservice/sip/phonesupport_kalash/numbers/suggested',
            '/v1/appEservice/sip/phonesupport_kalash/numbers/available/200',
            '/v1/appEservice/sip/phonesupport_kalash/subscription',
            '/v1/appEservice/support/phonesupport_kalash/all_tickets_with_compensation',
            '/v1/appEservice/support/phonesupport_kalash/problem_types',
            '/v1/appEservice/support/phonesupport_kalash/get_graph',
            '/v1/appEservice/support/phonesupport_kalash/outage',
            '/v1/appEservice/support/phonesupport_kalash/get-pending-tickets',
            '/v1/appEservice/support/phonesupport_kalash/field_location_reports/1',
            '/v1/appEservice/support/phonesupport_kalash/field/track/device_id',
            '/v1/appEservice/wl-benefits/default-outlets',
            '/v1/appEservice/wl-benefits/outlets-by-filter/googleMap/9.90866,9.875565',
            '/v1/appEservice/wl-benefits/outlet-detail/6204',
            '/v1/appEservice/wl-benefits/background-configuration',
            '/v1/appEservice/available_free_wifi_zones/27.6711212/85.3446311',
            '/v1/appEservice/customer/phonesupport_kalash/profile',
            '/v1/appEservice/customer/phonesupport_kalash/realtime_bw',
            '/v1/appEservice/customer/phonesupport_kalash/info',
            '/v1/appEservice/customer/phonesupport_kalash/transactions',
            '/v1/appEservice/customer/phonesupport_kalash/transactions_with_renew_detail',
            '/v1/appEservice/customer/phonesupport_kalash/account',
            '/v1/appEservice/customer/phonesupport_kalash/fup_flag_notifier',
            '/v1/appEservice/customer/phonesupport_kalash/fup_status',
            '/v1/appEservice/customer/phonesupport_kalash/documents',
            '/v1/appEservice/customer/phonesupport_kalash/documents/pdf',
            '/v1/appEservice/customer/phonesupport_kalash/show_bandwidth?pay_plan=1254',
            '/v1/appEservice/customer/phonesupport_kalash/internet_usage/2024-01-01/2024-03-24',
            '/v1/appEservice/customer/phonesupport_kalash/nt_hash_credentials',
            '/v1/appEservice/customer/phonesupport_kalash/full_detail',
            '/v1/appEservice/diagnostic/phonesupport_kalash/detail-by-requestid/64887f80b24b8f0cfa2a5215',
            '/v1/appEservice/diagnostic/phonesupport_kalash/detail-by-username',
            '/v1/appEservice/diagnostic/phonesupport_kalash/diagnostic-summary-report/64887f80b24b8f0cfa2a5215',
            # Add other URLs here as needed
        ]

        for url in urls:
            response = self.client.get(url, headers=headers)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            print(timestamp)
            print(f'This is the response of {url}')
            print(response)
