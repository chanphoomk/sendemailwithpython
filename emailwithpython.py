# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# "EMAIL address of the sender"
fromaddr = "testmail7489@gmail.com"
password = input("What's your password : ")
# "EMAIL address of the receiver"
# toaddr = ["testmail7489@gmail.com","testmail7489@gmail.com"]
toaddr = "testmail7489@gmail.com"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address
msg['To'] = toaddr

# storing the subject 
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail 
#  body = "Body_of_the_mail"
# msg.attach(MIMEText(body, 'plain')) 
text = """\
เรียนผู้อำนวยการที่เคารพ,

How are you?
WE're JMAT Award Team
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# attach the body with the msg instance 
msg.attach(MIMEText(text, 'plain')) 
msg.attach(MIMEText(html, 'html')) 


# open the file to be sent 
filename = "1.pdf"
attachment = open("1.pdf", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, password) 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
# for i in range(len(receiver)): 
# x=0
# while x != len(toaddr):
#     print("SENDING to : ", toaddr[x])
#     s.sendmail(fromaddr, toaddr[x], text) 
#     x+=1

print(" \n Sender : ", fromaddr)
s.sendmail(fromaddr, toaddr, text)
print(" \n Successfully Sent!")

# terminating the session 
s.quit() 
