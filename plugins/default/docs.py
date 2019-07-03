param = {'v':'5.90','q':pack['user_text'],'count':'0','access_token':config['user_token']}
count = requests.post('https://api.vk.com/method/docs.search', data=param).json()['response']['count']
if count > 10: count = count-10
if count < 11: count = 0
param = {'v':'5.90','q':pack['user_text'],'offset':random.randint(0,count),'count':'10','access_token':config['user_token']}
items = requests.post('https://api.vk.com/method/docs.search', data=param).json()['response']['items']

attachment = ''
if len(items) != 0:
	for item in items:
		attachment += 'doc'+str(item['owner_id'])+'_'+str(item['id'])+','
	apisay('Документы по вашему запросу',pack['toho'],attachment=attachment)
else: apisay('Документы по запросу не найдены :(',pack['toho'])
