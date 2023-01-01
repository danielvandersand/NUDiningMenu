# NUDiningMenu
Python script that gets the daily Northwestern dining hall menu and sends it to a list of emails.
<br />
<br />

**Code Walkthrough**
<br />
<br />

The message:
The message of the email, or the dining hall menus are coming from realdining.py. First, the info from DineOnCampus's API is retrieved. Next, the data is converted to json. The relevant information is obtained and a single string containing all of the menu's data is produced.
<br />
<br />

The list of emails:
First of all, emails are gathered into a google spreadsheet by means of a google form. When setting up the google spreadsheet API, a json file with sensitive information is created. I named it nudiningmenu.json, and removed the private informaiton for obvious reasons. Within emailProcess.py, all that happens is a for loop goes through every email address and adds it to a list.
<br />
<br />

The sensitive info:
I would recommend creating a file similar to creds.py that contains all of the sensitve info, like the email address you are sending from's password.
<br />
<br />
Bringing it all together:
emailProcess.py brings everyting together by setting up an email with the sensitive info and the message from realdining.py. In the execution, each email from the email list is sent by a for loop.
<br />
<br />

**Setup on Linux server:**
<br />
I am running this on a Linux server, using crontab to run at 7am every morning.
To run this on a Linux machine, ensure python3 is installed and run the following command in terminal:
<br />
pip install oauth2client gspread
<br />
<br />
I then cloned the code form my GitHub repo with the command:
<br />
git clone (url to my code)
<br />
<br />
After this, I used nano and input all of my sensitive info.
<br />
Next, set up the cronjob using:
<br />
crontab -e
<br />
Input something that looks like the following 
<br />
0 7 * * * /usr/bin/python3 /home/(directory to your executable file)
<br />
<br />
to schedule the code to run at 7 every morning. I found <https://crontab.guru/> to be helpful.
<br />
<br />

**Potential Issues:**
<br />

When I first tried running my code on the Linux server using cronjob, the file I wanted to execute didn't have the correct permissions. Therefore, I recommend pip installing everything within a virtual environment. Read <https://docs.python.org/3/tutorial/venv.html> for documentation.
