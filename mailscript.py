import smtplib

def email(sender, receivers, cc, subject, message, login, smtpserver = 'smtp.gmail.com:587'):
	header = 'From: %s\n' % sender
	header += 'To: %s\n' % ','.join(receivers)
	header += 'Cc: %s\n' % ','.join(cc)
	header += 'Subject: %s\n\n' % subject
	message = header + message

	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login, 'dldz acvz ruks ugdl')
	problems = server.sendmail(sender, receivers, message)
	server.quit()
	return problems

sends = raw_input('Enter sender address: ')
recs = []
temp = ''
while temp != 'done':
	recs.append(temp)
	temp = raw_input('Enter a receiver email, or \'done\' if finished: ')
sub = raw_input('Enter the subject of the email: ')
mess = raw_input('Enter the message you wish to send: ')
mess += '\n\n**Sent from a python script!!!**'
email(sends, recs, cc = [], subject = sub, message = mess, login = 'dsyandrewdeng')
