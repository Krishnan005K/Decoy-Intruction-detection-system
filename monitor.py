import os
import time
import smtplib
from email.message import EmailMessage
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='decoy_access.log', level=logging.INFO)
LoggedUser=os.getlogin()
DECOY_DIR = "Very Secret files"

DECOY_FILES = ["financial-Data.csv", "secret-API-DATA.txt"]

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
ADMIN_USER= os.getenv('ADMIN_USER')


def send_email_alert(file_accessed, user):
    msg = EmailMessage()
    msg.set_content(f"Decoy File Access Alert!\nFile: {file_accessed}\nUser: {user}\nTime: {time.ctime()}")
    msg['Subject'] = 'Decoy File Access Alert'
    msg['From'] = EMAIL_USER
    msg['To'] = ADMIN_USER
    print("Decoy File Accessed ")
    print("sending mail....")
    time.sleep(1)
    print("mail sent")
    # Sending the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

def monitor_decoy_files():
  
    file_access_times = {}

    for file_name in DECOY_FILES:
        file_path = os.path.join(DECOY_DIR, file_name)
        file_access_times[file_name] = os.path.getatime(file_path)

    while True:
        for file_name in DECOY_FILES:
            file_path = os.path.join(DECOY_DIR, file_name)
            current_access_time = os.path.getatime(file_path)

            if current_access_time != file_access_times[file_name]:
                user = os.getenv("USER", LoggedUser)  
                logging.info(f"Decoy File Accessed: {file_name}, User: {user}, Time: {time.ctime()}")

                send_email_alert(file_name, user)

                file_access_times[file_name] = current_access_time

        time.sleep(5)

if __name__ == "__main__":
    print(f"Monitoring decoy files in {DECOY_DIR}...")
    monitor_decoy_files()
