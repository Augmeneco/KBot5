if 'photo' in longpoll[pack['userid']]['object']['attachments'][0]:
	ret = longpoll[pack['userid']]['object']['attachments'][0]['photo']['sizes']
	num = 0
	for size in ret:
		if size['width'] > num:
			num = size['width']
			url = size['url']
	index = requests.get('https://yandex.ru/images/search?url='+url+'&rpt=imageview').text
	index = html.fromstring(index)
	tags = index.xpath('//div[@class="tags__wrapper"]/a')
	out = ''
	for tag in tags:
		out += '• '+BeautifulSoup(etree.tostring(tag).decode(),'lxml').text+'\n'
	
	apisay('Я думаю на изображении что-то из этого: \n'+out,pack['toho'])
else:
	apisay('Картинку сунуть забыл',pack['toho'])
