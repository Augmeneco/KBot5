cmd = pack['user_text'].replace('»','	')
cmd = cmd.split('<br>')
with open('data/py.py', 'w') as cl:
	for i in range(len(cmd)):
		cl.write(cmd[i]+'\n')
shell = subprocess.getoutput('chmod 755 data/py.py;python3 data/py.py')
apisay(shell,pack['toho'])