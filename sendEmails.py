import smtplib
from email.message import Message
from email.header import Header

server = smtplib.SMTP('smtp.gmail.com', 587)
myEmail = "your_email@gmail.com"

# Emails
emailFile = open("emails.txt")
emailString = emailFile.read()
emails = emailString.split("\n")

# Subjects
subFile = open("subjects.txt")
subString = subFile.read()
subjects = subString.split("\n")

server.ehlo()
server.starttls()
server.ehlo()

server.login("your_email_wo_domain", "your_password")

msgString = "Put your email message here."

for x in range(0, len(emails)):
    msg = Message()
    h = Header(subjects[x], 'iso-8859-1')
    msg['Subject'] = h
    msg.set_payload(msgString)
    server.sendmail(myEmail, emails[x], msg.as_string())


