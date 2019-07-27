longpoll[pack['userid']]=result

if 'photo' in longpoll[pack['userid']]['object']['attachments'][0]:
	ret = longpoll[pack['userid']]['object']['attachments'][0]['photo']['sizes']
	num = 0
	for size in ret:
		if size['width'] > num:
			num = size['width']
			url = size['url']
	pic = requests.get('http://lunach.ru/?cum=&url='+url).content
	sendpic(pic,'Готово!',pack['toho'])
else:
	apisay('Картинку забыл сунуть',pack['toho'])