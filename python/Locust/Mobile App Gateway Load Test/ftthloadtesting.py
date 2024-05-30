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


        #FTTH APIs TASK 1 to TASK 12
    @task() #1
    def get_online_devices(self):
        getonlinedevicesurl = '/v1/appEservice/ftth/phonesupport_kalash/online_devices'
        getonlinedevices = self.client.get(getonlinedevicesurl, headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_online_devices')
        print(getonlinedevices)
        

    @task() #2
    def get_online_devices_new(self):
        get_online_devices_new = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/online_devices_new', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the responsne of get_online_devices_new')
        print(get_online_devices_new)

    @task() #3
    def get_device_status(self):
        get_device_status = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/device_status', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_device_status')
        print(get_device_status)

    @task() #4
    def get_device_online_status(self):
        get_device_online_status = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/device_online_status', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of the get_device_online_status')
        print(get_device_online_status)

    @task() #5
    def get_nokia_radio_wan(self):
        get_nokia_radio_wan = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/view_nokia_radio', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_nokia_radio_wan')
        print(get_nokia_radio_wan)

    @task() #6
    def get_ONU_info(self):
        get_ONU_info = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/onu_info', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_ONU_info')
        print(get_ONU_info)

    @task() #7
    def get_is_nwcc_enabled(self):
        get_is_nwcc_enabled = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/is_nwcc_enabled', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_is_nwcc_enabled')
        print(get_is_nwcc_enabled)
    
    @task() #8
    def get_beacon_connected_list(self):
        get_beacon_connected_list = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/get_beacon_connected_list', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M%S")
        print(timestamp)
        print('This is the response of get_beacon_connected_list')
        print(get_beacon_connected_list)

    @task() #9
    def get_view_nokia_mac_acl (self):
        get_view_nokia_mac_acl = self.client.get('/v1/appEservice/device_filtering/phonesupport_kalash/fetch')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_view_nokia_mac_acl')
        print(get_view_nokia_mac_acl)
    
    @task() #10
    def get_channel_mode (self):
        get_channel_mode = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/channel/mode', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_channel_mode')
        print(get_channel_mode)

    @task() #11
    def get_nearby_scan_list (self):
        get_nearby_scan_list = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/channel/near-by-scan-list', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_nearby_scan_list')
        print(get_nearby_scan_list)
    
    @task() #12
    def get_available_list (self):
        get_available_list = self.client.get('/v1/appEservice/ftth/phonesupport_kalash/channel/available-list', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_available_list')
        print(get_available_list)
    
    #END OF FTTH


    #LOGIN APIs Task 13
    
    @task() #13
    def get_profile (self):
        get_profile = self.client.get('/v1/appEservice/me', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_profile')
        print(get_profile)

    @task() #14
    def get_social (self):
        get_social = self.client.get('/v1/appEservice/setSocialLoginActivationStatus', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_social')
        print(get_social)

    #CONFIG APIS Task 15 to Task 20
    @task() #15
    def get_check_app_version(self):
        get_check_app_version = self.client.get('/v1/appEservice/app_version/android', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_check_app_version')
        print(get_check_app_version)

    @task() #16
    def get_company_contacts(self):
        get_company_contacts = self.client.get('/v1/appEservice/company_contacts', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_company_contacts')
        print(get_company_contacts)

    @task() #17
    def get_document_types(self):
        get_document_types = self.client.get('/v1/appEservice/get_user_documents', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_document_types')
        print(get_document_types)

    @task() #18
    def get_image(self):
        get_image = self.client.get('/v1/appEservice/get_images', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_image')
        print(get_image)

    @task() #19
    def get_is_allowed_logout(self):
        get_is_allowed_logout = self.client.get('/v1/appEservice/is_allow_to_logout', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_is_allowed_logout')
        print(get_is_allowed_logout)
    
    @task() #20
    def get_ecg(self):
        get_ecg = self.client.get('/v1/appEservice/ecg', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_ecg')
        print(get_ecg)
    
    #_______________FTTH service check Task 21________________
    @task() #21
    def get_ftth_service_check(self):
        get_ftth_service_check = self.client.get('/v1/appEservice/service_available/27.7089543/85.2849333', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_ftth_service_check')
        print(get_ftth_service_check)

    #____________Check NT hash Task 22_______________
    @task() #22
    def get_check_nt_hashed(self):
        get_check_nt_hashed = self.client.get('/v1/appEservice/check_nt_hash/phonesupport_kalash',headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_check_nt_hashed')
        print(get_check_nt_hashed)

    #____________GET KYC Task 23________
    
    @task() #23
    def get_kyc(self):
        get_kyc = self.client.get('/v1/appEservice/kyc/phonesupport_kalash/status', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_kyc')
        print(get_kyc)

    
    #______________SIP VoIP Task 24 to Task 27 ___________
    @task() #24    
    def get_sip_support_details(self):
        get_sip_support_details = self.client.get('/v1/appEservice/sip/sip_support', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_sip_support_details')
        print(get_sip_support_details)

    @task() #25
    def get_suggested_numbers(self):
        get_suggested_numbers = self.client.get('/v1/appEservice/sip/phonesupport_kalash/numbers/suggested', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_suggested_numbers')
        print(get_suggested_numbers)
    
    @task() #26
    def get_available_numbers(self):
        get_available_numbers = self.client.get('/v1/appEservice/sip/phonesupport_kalash/numbers/available/200', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_available_numbers')
        print(get_available_numbers)

    @task() #27
    def get_subscription_status(self):
        get_subscription_status = self.client.get('/v1/appEservice/sip/phonesupport_kalash/subscription', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_subscription_status')
        print(get_subscription_status)

    #________________Support Task 28 to Task 34__________________________
    
    @task() #28
    def get_all_tickets_compensation(self):
        get_all_tickets_compensation = self.client.get('/v1/appEservice/support/phonesupport_kalash/all_tickets_with_compensation', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_all_tickets_compensation')
        print(get_all_tickets_compensation)
    
    @task() #29
    def get_problem_type_list(self):
        get_problem_type_list = self.client.get('/v1/appEservice/support/phonesupport_kalash/problem_types', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_problem_type_list')
        print(get_problem_type_list)
    
    @task() #30
    def get_graph(self):
        get_graph = self.client.get('/v1/appEservice/support/phonesupport_kalash/get_graph', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_graph')
        print(get_graph)

    @task() #31
    def get_outage(self):
        get_outage = self.client.get('/v1/appEservice/support/phonesupport_kalash/outage', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_outage')
        print(get_outage)

    @task() #32
    def get_pending_tickets(self):
        get_pending_tickets = self.client.get('/v1/appEservice/support/phonesupport_kalash/get-pending-tickets', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_pending_tickets')
        print(get_pending_tickets)
    
    @task() #33
    def get_field_location_reports(self):
        get_field_location_reports = self.client.get('/v1/appEservice/support/phonesupport_kalash/field_location_reports/1', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_field_location_reports')
        print(get_field_location_reports)
    
    @task() #34
    def get_field_track(self):
        get_field_track = self.client.get('/v1/appEservice/support/phonesupport_kalash/field/track/device_id')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_field_track')
        print(get_field_track)

    #________________WL Benefits Task 35 to Task 38________________
    
    @task() #35
    def get_default_outlet(self):
        get_default_outlet = self.client.get('/v1/appEservice/wl-benefits/default-outlets', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_default_outlet')
        print(get_default_outlet)

    @task() #36
    def get_outlets_by_filter(self):
        get_outlets_by_filter = self.client.get('/v1/appEservice/wl-benefits/outlets-by-filter/googleMap/9.90866,9.875565', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_outlets_by_filter')
        print(get_outlets_by_filter)

    @task() #37
    def get_outlet_detail(self):
        get_outlet_detail = self.client.get('/v1/appEservice/wl-benefits/outlet-detail/6204', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_outlet_detail')
        print(get_outlet_detail)
    
    @task() #38
    def get_background_config(self):
        get_background_config = self.client.get('/v1/appEservice/wl-benefits/background-configuration', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_background_config')
        print(get_background_config)
    

    #_______________Customer API form Task 39 to Task 55 _______________
    
    @task() #39
    def available_free_wifi_zone(self):
        get_available_free_wifi_zone = self.client.get('/v1/appEservice/available_free_wifi_zones/27.6711212/85.3446311', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of available_free_wifi_zone')
        print(get_available_free_wifi_zone)

    @task() #40
    def get_fetch_profile(self):
        get_fetch_profile = self.client.get('/v1/appEservice/customer/phonesupport_kalash/profile', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_fetch_profile')
        print(get_fetch_profile)

    @task() #41
    def get_real_time_bandwidth(self):
        get_real_time_bandwidth = self.client.get('/v1/appEservice/customer/phonesupport_kalash/realtime_bw', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_real_time_bandwidth')
        print(get_real_time_bandwidth)
    
    @task() #42
    def get_customer_info(self):
        get_customer_info = self.client.get('/v1/appEservice/customer/phonesupport_kalash/info', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_info')
        print(get_customer_info)

    @task() #43
    def get_transactions(self):
        get_transactions = self.client.get('/v1/appEservice/customer/phonesupport_kalash/transactions', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_transactions')
        print(get_transactions)

    @task() #44
    def get_transactions_with_renew_detail(self):
        get_transactions_with_renew_detail = self.client.get('/v1/appEservice/customer/phonesupport_kalash/transactions_with_renew_detail', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_transactions_with_renew_detail')
        print(get_transactions_with_renew_detail)

    @task() #45
    def get_customer_account(self):
        get_customer_account = self.client.get('/v1/appEservice/customer/phonesupport_kalash/account', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_account')
        print(get_customer_account)
    
    @task() #46
    def get_customer_FUP_flag_notifier(self):
        get_customer_FUP_flag_notifier = self.client.get('/v1/appEservice/customer/phonesupport_kalash/fup_flag_notifier', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_FUP_flag_notifier')
        print(get_customer_FUP_flag_notifier)
    
    @task() #47
    def get_customer_FUP_status(self):
        get_customer_FUP_status = self.client.get('/v1/appEservice/customer/phonesupport_kalash/fup_status', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_FUP_status')
        print(get_customer_FUP_status)

    @task() #48
    def get_customer_documents(self):
        get_customer_documents = self.client.get('/v1/appEservice/customer/phonesupport_kalash/documents', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_documents')
        print(get_customer_documents)

    @task() #49
    def get_customer_documents_type(self):
        get_customer_documents_type = self.client.get('/v1/appEservice/customer/phonesupport_kalash/documents/pdf', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_documents_type')
        print(get_customer_documents_type)    

    @task() #50
    def get_show_bandwidth(self):
        get_show_bandwidth = self.client.get('/v1/appEservice/customer/phonesupport_kalash/show_bandwidth?pay_plan=1254', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_show_bandwidth')
        print(get_show_bandwidth)

    @task() #51
    def get_show_internet_usage(self):
        get_show_internet_usage = self.client.get('/v1/appEservice/customer/phonesupport_kalash/internet_usage/2024-01-01/2024-03-24', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_show_internet_usage')
        print(get_show_internet_usage)   

    @task() #52
    def get_customer_NT_hash_password(self):
        get_customer_NT_hash_password = self.client.get('/v1/appEservice/customer/phonesupport_kalash/nt_hash_credentials', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_NT_hash_password')
        print(get_customer_NT_hash_password)

    @task() #53
    def get_customer_full_details(self):
        get_customer_full_details = self.client.get('/v1/appEservice/customer/phonesupport_kalash/full_detail', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_customer_full_details')
        print(get_customer_full_details)   


    #______________________Diagnostic Task 56 to Task 58________________________
    @task() #54
    def get_diagnostic_info_by_req_id(self):
        get_diagnostic_info_by_req_id = self.client.get('/v1/appEservice/diagnostic/phonesupport_kalash/detail-by-requestid/64887f80b24b8f0cfa2a5215', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_diagnostic_info_by_req_id')
        print(get_diagnostic_info_by_req_id)

    @task() #55
    def get_diagnostic_info_by_username(self):
        get_diagnostic_info_by_username = self.client.get('/v1/appEservice/diagnostic/phonesupport_kalash/detail-by-username', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_diagnostic_info_by_username')
        print(get_diagnostic_info_by_username)     

    @task() #56
    def get_diagnostic_summary(self):
        get_diagnostic_summary = self.client.get('/v1/appEservice/diagnostic/phonesupport_kalash/diagnostic-summary-report/64887f80b24b8f0cfa2a5215', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_diagnostic_summary')
        print(get_diagnostic_summary)


    #____________________Nettv Details Task 57 to Task 59___________________________

    @task() #57
    def get_nettv_details(self):
        get_nettv_details = self.client.get('/v1/appEservice/nettv/phonesupport_kalash/info', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_nettv_details')
        print(get_nettv_details)

    @task() #58
    def get_stb_detail(self):
        get_stb_detail = self.client.get('/v1/appEservice/nettv/phonesupport_kalash/payment/stb-details', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_stb_detail')
        print(get_stb_detail)

    @task() #59
    def get_stb_box_detail(self):
        get_stb_box_detail = self.client.get('/v1/appEservice/nettv/phonesupport_kalash/payment/stb-box-details/00226D9E5518', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_stb_box_detail')
        print(get_stb_box_detail)

    #_____________________Refer Offer Task 60 to Task 61_______________

    @task() #60
    def get_offer_banner(self):
        get_offer_banner = self.client.get('/v1/appEservice/refer_offer/phonesupport_kalash/refer_offer_banner', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_offer_banner')
        print(get_offer_banner)

    @task() #61
    def get_refer_offer_terms_conditions(self):
        get_refer_offer_terms_conditions = self.client.get('/v1/appEservice/refer_offer/phonesupport_kalash/refer_offer_terms_conditions', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_refer_offer_terms_conditions')
        print(get_refer_offer_terms_conditions)


    #__________V2 Routes Speed Boost task 64 to task________
    @task()
    def get_client_eligibility(self):
        get_client_eligibility = self.client.get('/v2/boost/phonesupport_kalash/isEligible', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_client_eligibility)
    
    @task()
    def get_valid_to_provision(self):
        get_valid_to_provision = self.client.get('/v2/boost/phonesupport_kalash/validToProvision', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_valid_to_provision)

    @task()
    def get_package_details(self):
        get_package_details = self.client.get('/v2/boost/phonesupport_kalash/package', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_package_details)

    @task()
    def get_days_remaining(self):
        get_days_remaining = self.client.get('/v2/boost/phonesupport_kalash/daysremaining', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_days_remaining)
    
    @task()
    def get_payment_details(self):
        get_payment_details = self.client.get('/v2/payment/phonesupport_kalash/payment-details', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_payment_details)

    @task()
    def get_fetch_notification(self):
        get_fetch_notification = self.client.get('/v2/notification/phonesupport_kalash', headers=headers)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        print(timestamp)
        print('This is the response of get_client_eligibility')
        print(get_fetch_notification)
    
    # @task()
    # def create_user(self):
    #     data = self.client.post('/dummy/updateReadUserDetail/phonesupport_kalash')
    #     print("THIS IS THE RESPONSE OF POST")
    #     print(data)
    #     print(data.headers)
