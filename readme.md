## Before ##
Before using this program, you have to enable "Allow less secure apps" in your google account security settings.
## How To ##
### email_address.txt ###
Your email address on line 1, and your password on line 2

### emails.txt ###
Put a newline separated list of email recipient address

### message.txt ###
Put a custom message you want sent to all recipients

### subjects.txt ###
Put a newline separated list of subjects, subject at line 2 will correspond to email recipient at line 2 in emails.txt


### sendEmails.py ###
Run this after all configurations are set, and all email addresses listed in emails.txt will receive an email containing
the message in message.txt with a corresponding subject in subjects.txt sent from the email address listed in email_address.txt