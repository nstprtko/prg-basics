import re

file_name="email.txt"
pattern_sender = r'^From:\s*.*<([^<>\s]+@[^<>\s]+\.[a-zA-Z]{2,})>\s*$'
recipient_pattern = r'^To:\s*.*<([^<>\s]+@[^<>\s]+\.[a-zA-Z]{2,})>\s*$'
subject_pattern = r'^Subject:\s*(.+)$'
body_pattern = r'\n\n(.*)'

with open(file_name, "r") as file:
    email_content = file.read()

sender_match = re.search(pattern_sender, email_content, re.MULTILINE)
if sender_match:
    sender = sender_match.group(1)
    print(sender)

else:
    print('not found')

recipient_match = re.search(recipient_pattern, email_content, re.MULTILINE)
if recipient_match:
    recepient = recipient_match.group(1)
    print(recepient)

else:
    print('not found')


subject_match = re.search(subject_pattern, email_content, re.MULTILINE)
if subject_match:
    subject = subject_match.group(1)
    print(subject)

else:
    print('not found')

body_match = re.search(body_pattern, email_content, re.DOTALL)
if body_match:
    body = body_match.group(1).strip()
    print(body)

else:
    print('not found')

