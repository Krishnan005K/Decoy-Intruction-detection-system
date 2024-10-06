# Decoy File Monitoring System

## Overview

The **Decoy File Monitoring System** is a Python-based application designed to monitor sensitive files on a system. This project is aimed at enhancing security by tracking unauthorized access to decoy files, alerting the system administrator via email whenever these files are accessed. The system logs user access attempts, providing a clear audit trail for security analysis.

## Features

- **File Monitoring**: Continuously monitors specified decoy files for access events.
- **User Logging**: Captures and logs the username of the person accessing the files.
- **Email Notifications**: Sends real-time email alerts to the administrator when a decoy file is accessed.
- **Logging Mechanism**: Maintains a detailed log of all access attempts for review and analysis.
- **Environment Variable Configuration**: Utilizes a `.env` file to securely store sensitive information such as email credentials and SMTP server details.

## Technologies Used

- **Python**: The programming language used to implement the application.
- **smtplib**: Used for sending email alerts.
- **dotenv**: Utilized to manage environment variables and sensitive information.
- **Logging Module**: For logging access events to a log file.

## Installation

1. **Clone the repository**:

         git clone https://github.com/yourusername/decoy-file-monitoring.git
         cd decoy-file-monitoring
2. **Install required packages**:
  Make sure you have Python 3.x installed. Then install the required packages using:

          pip install -r requirements.txt
3. **Set up the .env file**:
    Create a .env file in the root directory of the project with the following structure:
        
        EMAIL_USER=your_email@example.com
        ADMIN_USER=admin_email@example.com
        EMAIL_PASSWORD=your_email_password
        SMTP_SERVER=smtp.example.com
        SMTP_PORT=587
   
4. **Modify Directory and File List**:
     Update the DECOY_DIR variable in the code to point to the directory where your decoy files are located.
     Modify the DECOY_FILES list to include the names of the files you want to monitor.

## Usage
To start monitoring the decoy files, run the main script:
        python monitor.py
        
The application will begin monitoring the specified directory for access events. Upon detecting access to any of the specified decoy files, it will log the event and send an email alert to the configured administrator email address.

## Logging
All access attempts are logged to a file named decoy_access.log, which includes the following information:

File name accessed

User who accessed the file

Timestamp of the access event

## Example Output
When a decoy file is accessed, the console will display:

      Monitoring decoy files in Very Secret files...
      Decoy File Accessed 
      Sending Mail.... 
      Mail Sent
      And an email notification will be sent to the administrator with the details of the access event.

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
