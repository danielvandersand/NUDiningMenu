import creds
import realdining
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import time

today = date.today()
# this is the menu for each dining hall
# see realdining.py for how this is done through the web API
message_str = realdining.message_str


# this constructs the email, and uses the information in creds to see the sender
def email_new(x):
    message = MIMEMultipart()
    message['Subject'] = "Menus %s" % str(today)
    message['From'] = creds.sender
    message['To'] = x


    mess_str = MIMEText(message_str)
    message.attach(mess_str)
    # only valid SMTP with offie365
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(creds.sender, x, message.as_string())


# this goes through each email in the recipient array and sends an email to that address
if __name__ == '__main__':
    for i in creds.recipient:
        email_new(i)
        # needs to sleep for 2 seconds because google spreadsheet API only allows 100 calls/min
        time.sleep(2)