import smtplib
import getpass
from email.mime.text import MIMEText
def send_email():
    try:

        sender_address = 'manishabadhe773@gmail.com'
        recipients = ['manishabadhe773@gmail.com','manishabadhe09@gmail.com']
        print("Enter your App Password:")
        password = getpass.getpass()
        subject = 'AI Mafia - Machine Learning'
        msg = '''
            Hello Everyone!
            I am doing a project of email sending using python...
            Regards,
            Manisha..!
        '''
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_address, password)
        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = sender_address
        msg['To'] = ', '.join(recipients)
        
        server.sendmail(sender_address, recipients,msg.as_string())
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
send_email()