import emailList

# input the email address the email will be sent from
# use outlook, as gmail no longer supports this without changing settings
sender = "send from this email"
password = 'email password of sender'

# list of email address obtained from google sheet, see emailList.py
recipient = emailList.email_list