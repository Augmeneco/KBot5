if pack['user_text'] == '': pack['user_text'] = 'b'
try:
	thread = requests.get('https://2ch.hk/'+pack['user_text']+'/'+str(random.randint(0,9)).replace('0','index')+'.json').json()['threads']
except:
	apisay('Такой борды не существует',pack['toho'])
	exit()
thread = thread[len(thread)-1]
url = 'https://2ch.hk/'+pack['user_text']+'/res/'+thread['posts'][0]['num']+'.html'
text = 'Оригинал: '+url+'\n'+BeautifulSoup(thread['posts'][0]['comment'].replace('<br>','\n'), "lxml").text
img = 'https://2ch.hk'+thread['posts'][0]['files'][0]['path']
img = requests.get(img).content
sendpic(img, text, pack['toho'])
