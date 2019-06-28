param = {'v':'5.90','q':pack['user_text'],'count':'30','sort':2,'access_token':config['user_token']}
items = requests.post('https://api.vk.com/method/audio.search', data=param).json()['response']['items']

attachment = ''
if len(items) != 0:
	for item in items:
		attachment += 'audio'+str(item['owner_id'])+'_'+str(item['id'])+','
	apisay('Музыка по запросу вашему запросу',pack['toho'],attachment=attachment)
else: apisay('Музыка по запросу не найдена :(',pack['toho'])

