import smtplib
from email.message import Message
from email.header import Header


# Settings for gmail accounts
server = smtplib.SMTP('smtp.gmail.com', 587)

# Your email address
email_data = open("email_address.txt").read()
email_data = email_data.split("\n")
if len(email_data) < 2:
    exit("Email not properly set.")

myEmail = email_data[0]
password = email_data[1]

# Emails
emailFile = open("emails.txt")
emailString = emailFile.read()
emails = emailString.split("\n")
if len(emails) == 0:
    exit("No email addresses.")

# Subjects
subFile = open("subjects.txt")
subString = subFile.read()
subjects = subString.split("\n")
if len(subjects) == 0:
    exit("No subjects.")

# Message
mFile = open("message.txt")
msgString = mFile.read()
if len(msgString) == 0:
    exit("No message set")

server.ehlo()
server.starttls()
server.ehlo()

username = myEmail.split("@")[0]
server.login(username, password)

for x in range(0, len(emails)):
    msg = Message()
    h = Header(subjects[x], 'iso-8859-1')
    msg['Subject'] = h
    msg.set_payload(msgString)
    server.sendmail(myEmail, emails[x], msg.as_string())


