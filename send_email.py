import sys
import os

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.message



from dotenv                                                 import load_dotenv
load_dotenv()


my_email = os.getenv("EMAIL")
smtp_server = os.getenv("SMTP")
port = int(os.getenv("SMTP_PORT"))
password = os.getenv("PASSWORD")


if len(sys.argv) != 6:
    print("Usage: python3 send_email.py <name> <email> <subject> <message> <html_file>")

else:

    name = sys.argv[1]
    email = sys.argv[2]
    subject = sys.argv[3]
    message = sys.argv[4]
    html_file = sys.argv[5]

    try:
        file = open(html_file,mode='r')
        html = file.read()
        html = html.replace("{name}", name)
        html = html.replace("{email}", email)
        html = html.replace("{subject}", subject)
        html = html.replace("{message}", message)
        
        file.close()


        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = my_email
        message["To"] = email
        text = "Use um navegador compativel com HTML5"

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
                        print("SMTP connected...")
                     
                        server.login(my_email, password)
                       
                        server.sendmail(my_email, email,
                                        message.as_string().encode("latin1"))
                       
                        server.quit()
                        print("Email sent")

    except:
        print("File not exists")

    
