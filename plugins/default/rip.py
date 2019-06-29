if pack['user_text'] == '':
	apisay('Текст то напиши',pack['toho'])
	exit()
out = ''
if len(pack['user_text'].split(' ')) > 70:
	apisay('Сообщение слишком больше, я не хочу чтобы яндекс наказали меня :(',pack['toho'])
	exit()
for word in pack['user_text'].split(' '):
	result = requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='+config['yandex_key']+'&lang=ru-ru&text='+word).json()
	if len(result['def']) != 0:
		out += result['def'][0]['tr'][random.randint(0,len(result['def'][0]['tr'])-1)]['text']+' '
	else:
		out += word+' '
apisay(out,pack['toho'])

'''if pack['user_text'] == '':
	apisay('Текст то напиши',pack['toho'])
	exit()

tries = 0
while True:
	tries += 1
	id = requests.post('https://api.sinoni.men/',data={'text':pack['user_text'],'token':'tolya','lang':'ru'}).json()['result']['id']
	ret = requests.post('https://api.sinoni.men/',data={'token':'tolya','id':id}).json()
	if 'error' not in ret:
		ret = ret['result']['text']
		break
	else:
		continue
	if tries == 100:
		apisay('Что-то пошло не так :|',pack['toho'])
		exit()

apisay(ret,pack['toho'])'''