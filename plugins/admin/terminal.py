cmd = pack['user_text'].split('<br>')
with open('data/cmd.sh', 'w') as cl:
	for i in range(len(cmd)):
		cl.write(cmd[i]+'\n')
shell = subprocess.getoutput('chmod 755 data/cmd.sh;bash data/cmd.sh')
apisay(shell,pack['toho'])
