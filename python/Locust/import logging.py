import logging
import os

log_file_path = r'C:\AutomationScripts\python\Locust\test_log.txt'

# Ensure the directory exists
log_dir = os.path.dirname(log_file_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This is a test log entry.")
