from locust import HttpUser, constant, task, between
from datetime import datetime
import logging
import sys
import os

# Set the log file path
log_file_path = r'C:\AutomationScripts\python\Locust\outage_responses.txt'

# Ensure the directory exists
log_dir = os.path.dirname(log_file_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a custom logger
logger = logging.getLogger('outage_logger')
logger.setLevel(logging.INFO)

# Check if handlers are already added to avoid duplicate logs
if not logger.handlers:
    # Create handlers (file and stream)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

# Test logging at startup to ensure file and console output
logger.info("Logging setup is complete, starting test...")

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsb2dpbi53bGluay5jb20ubnAiLCJpYXQiOjE3MjU1MzI3MjAsImV4cCI6MTkyNjg0NTQyOSwibmJmIjoxNzI2ODA5NDI5LCJqdGkiOiJJbEpxR3phVktNWmVyanZlIiwic3ViIjoiYXBvb3JiYS5yYW5hIiwiYXVkIjoiZmEtdHJhY2tpbmcud2xpbmsuY29tLm5wIn0.v9X1_XM0NbmN-EEOwvaOub8uo-L6QiF-yf0Cy3Is5Ss'
headers = {"Authorization": f"Bearer {TOKEN}"}


class Outage(HttpUser):
    host='https://dev-02.wlink.com.np/rapoorba/pgOutage/index.php'
    wait_time = between(2, 4)

    def on_error(self, error):
        print(f"Error Encounted: {error}")
        super().on_error(error)

    def on_start(self):
        # Log when Locust starts
        logger.info("Locust is starting...")

    @task
    def get_apis(self):
        urls = [
            '/api/getOutageUpdateData?subject=templates&state=Ack1',
            '/Accesscontrol/getUserList?search=apoorba',
            '/api/checkUserNetwork?username=apoorba_home',
            '/api/monitorOutage',
            # '/api/getAffectedUsers',
            '/api/fetchingONSData?lat=27.738687&lng=85.3201594',
            '/api/getOutageDetailByTicketId/9896957',
            '/api/getOutageDetailByTicketId/9876933',
            '/api/getOutageDetailByTicketId/9885494',
            '/api/getOutageDetailByTicketId/9684502',
            '/api/getOutageDetailByTicketId/9790323',
            '/api/getOutageDetailByTicketId/9880003',
            '/api/getOutageDetailByTicketId/9889554',
        ]

        for url in urls:
            try:
                response = self.client.get(url, headers=headers)
                logger.info(f'Response from {url}: {response.status_code}')
                logger.info(f'Response text: {response.text}')
            except Exception as e:
                logger.error(f'Error encountered while processing {url}: {str(e)}')                

    @task(5)
    def post_apis(self):
        endpoints = [
            '/api/reportOutage',
            '/api/sendForVerification',
            # *['/api/postNodeUpdateStatus']* 5,
            # *['/api/updateTTStatus']* 5,                        
            # '/api/syncAffectedCustomer',
            # '/api/removeAffectedCustomer',
        ]
        bodies = [
            {'node':'320133','service':'fttx','owner':'Wlink','description':'Outage at 320133','reported_by':'apoorba.rana'},
            {'node':'275280','node_type': 'distribution','reported_by':'apoorba.rana','client_name':'apoorba_home'},      
            # {'node':'1368594','status':'Ack1','type':'distribution'},
            # {'node':'1358890','status':'Ack2','type':'master'},
            # {'node':'377687','status':'Ack2','type':'distribution'},
            # {'node':'733251','status':'Problem Acknowledged','type':'distribution'},
            # {'node':'139824','status':'Ack1','type':'master'},
            # {'ticket_id':'9897501', 'status':'reassign'},
            # {'ticket_id':'9897661', 'status':'assign'},
            # {'ticket_id':'9898025', 'status':'assign'},
            # {'ticket_id':'9885801', 'status':'reassign'},
            # {'ticket_id':'9653746', 'status':'reassign'},   
        ]

        for endpoint, body in zip(endpoints, bodies):
            try:    
                response = self.client.post(endpoint, body, headers=headers)
                logger.info(f'Response from {endpoint}:{response.status_code}')
                logger.info(f'Response text: {response.text}')
            except Exception as e:
                print(f"Error occurred while processing {endpoint}: {str(e)}")

for handler in logging.getLogger().handlers:
    handler.flush()
