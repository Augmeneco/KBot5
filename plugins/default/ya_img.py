headers = {'User-Agent': 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16'}
proxies = {'http': 'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}

result = requests.get('https://yandex.ru/images/smart/search?p='+str(random.randint(0,99))+'&text='+pack['user_text'].replace(' ','+')+'&rpt=image_smart',headers=headers).text

index = html.fromstring(result)
index = index.xpath('//a[@class="serp-item"]')
success = 0
attach = []
for img in index:
	if success > 10:
		break
	img = etree.tostring(img).decode().lower()
	img = re.findall('img_url=(.*).(png|jpg|jpeg)',img)[0]
	try:
		pic = requests.get(img[0].replace('%3a',':')+'.'+img[1]).content
		if 'body' not in str(pic):
			ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
			ret = requests.post(ret['response']['upload_url'],files={'photo':('photo.png',pic,'image/png')}).json()
			ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).json()
			attach.append('photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id']))
			success += 1
	except Exception as error:
		if 'Connection reset by peer' in str(error):
			pic = requests.get(img[0].replace('%3a',':')+'.'+img[1],proxies=proxies).content
			if 'body' not in str(pic):
				ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
				ret = requests.post(ret['response']['upload_url'],files={'photo':('photo.png',pic,'image/png')}).json()
				ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).json()
				attach.append('photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id']))
				success += 1
				
requests.post('https://api.vk.com/method/messages.send',data={'attachment':','.join(attach),'message':'Картинки по запросу '+pack['user_text']+':','v':'5.80','peer_id':toho,'access_token':token})
