param = {'v':'5.90','q':pack['user_text'],'count':'30','access_token':config['user_token']}
items = requests.post('https://api.vk.com/method/docs.search', data=param).json()['response']['items']

attachment = ''
if len(items) != 0:
	for item in items:
		attachment += 'doc'+str(item['owner_id'])+'_'+str(item['id'])+','
	apisay('Документы по вашему запросу',pack['toho'],attachment=attachment)
else: apisay('Документы по запросу не найдены :(',pack['toho'])