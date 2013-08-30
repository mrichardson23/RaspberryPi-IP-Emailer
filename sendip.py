# Put your email address here:
myAddress = 'address_here@gmail.com'

# Put your email password here:
pw = 'password_here'

# Put your SMTP server and port here (leave alone for gmail):
smtpServer = 'smtp.gmail.com'
smtpPort = 587

# Import email modules to send the email
import smtplib
from email.mime.text import MIMEText

# Import socket lib to get the IP address
import socket

# This is what gets your IP as a string (from Stackoverflow):
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
ipString = s.getsockname()[0]
s.close

# Set up the message:
msg = MIMEText("The Raspberry Pi's IP is " + ipString)
msg['From'] = myAddress
msg['To'] = myAddress
msg['Subject'] = "The Raspberry Pi's IP is " + ipString

# Connect to the server and send the message
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(myAddress, pw)
server.sendmail(myAddress, myAddress,msg.as_string())
server.quit()