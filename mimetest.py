import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#setup message stuff
msg = MIMEMultipart()
msg['From'] = input('Enter sender\'s email: ')
receivers = []
temp = ''
while temp != 'done':
	receivers.append(temp)
	temp = input('Enter a new receiver, or \'done\' if done: ')
msg['To'] = ', '.join(receivers)
msg['Subject'] = input('Enter a subject for the mail: ')

for x in os.listdir(os.getcwd()):
	if (x.endswith(".jpg")):
		msg.attach(MIMEImage(open(x, 'rb').read()))
		continue

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('dsyandrewdeng@gmail.com', 'dldz acvz ruks ugdl')
server.send_message(msg)
server.quit()
