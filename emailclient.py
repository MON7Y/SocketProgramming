import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you?"
msg = MIMEText(body)
msg['From'] = "abc@gmail.com" #use any valid email in place of abc@gmail.com
msg['To'] = "pqr@gmail.com" #use any valid email in place of pqr@gmail.com
msg['Subject'] = "Hello!!!"

server = smtplib.SMTP('smtp.gmail.com',587) #gmail SMTP server information 587 is default port

server.starttls()

server.login("abc@gmail.com","abc123") #Enter valid Email address and password.

server.send_message(msg)

print("Mail Sent")

server.quit()


