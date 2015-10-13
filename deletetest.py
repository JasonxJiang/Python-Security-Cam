import os

remove = 'rm '
for x in os.listdir(os.getcwd()):
	if (x.endswith(".jpg")):
		os.system('rm ' + x)
