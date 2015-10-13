import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 10006))

connection = s.makefile('rb')
try:
	cmdline = ['vlc', '--demux', 'h264', '-']
	player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
	
	while 1:
		data = connection.read(1024)
		if not data:
			break
		player.stdin.write(data)
finally:
	connection.close()
	s.close()
	player.terminate()
