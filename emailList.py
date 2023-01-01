from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time

# scope, creds, and client are standard code for google's API
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('nudiningmenu.json', scope)
client = gspread.authorize(creds)


# this will allow us to get the data from the spreadsheet
# input the name of your spreadsheet here
python_list = client.open('Name of spreadsheet').sheet1

# this gets every email input into the google sheet and puts it into a list of strings
i = 2
email_list = []
while python_list.cell(i,2).value != None:
    time.sleep(2)
    email_list.append(python_list.cell(i,2).value)
    i = i + 1
