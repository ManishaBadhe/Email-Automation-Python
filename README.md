# Email Automation using Python  

This project demonstrates how to send emails using Python, focusing on secure authentication, multi-recipient support, and professional email formatting using the MIME protocol.  

## Features  
- Secure authentication with Gmail's app password.  
- Supports multiple recipients.  
- Email formatting using `email.mime.text.MIMEText`.  
- Simple and user-friendly script.  

## How It Works  
1. Users are prompted to enter their app password securely via `getpass`.  
2. The script establishes a connection to Gmail's SMTP server.  
3. An email is sent to all recipients listed in the script with a predefined subject and message body.  

## Requirements  
To run this project, you need:  
- Python 3.x  
- Access to a Gmail account with an app password configured.  

### Python Libraries Used  
- `smtplib`: For sending emails.  
- `getpass`: For secure password input.  
- `email.mime.text`: For email formatting.  

## Setup Instructions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/ManishaBadhe/email-automation-python.git
