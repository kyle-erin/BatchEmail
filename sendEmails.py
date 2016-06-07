import smtplib
from email.message import Message
from email.header import Header

server = smtplib.SMTP('smtp.gmail.com', 587)
myEmail = "kyle.erin.phillips@gmail.com"

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

server.login("kyle.erin.phillips", "muffins29")

msgString = "Hello,\nI'm with a group of working professionals that carpool to Microsoft and we're looking" \
            " for a place near work. Is this property still available? Also, if first+last+security deposit is needed, " \
            "is it possible to pay some of that over an extended period of time?\n\nThanks!"

for x in range(0, len(emails)):
    msg = Message()
    h = Header(subjects[x], 'iso-8859-1')
    msg['Subject'] = h
    msg.set_payload(msgString)
    server.sendmail(myEmail, emails[x], msg.as_string())


