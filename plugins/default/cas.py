if 'photo' in longpoll[pack['userid']]['object']['attachments'][0]:
	ret = longpoll[pack['userid']]['object']['attachments'][0]['photo']['sizes']
	num = 0
	for size in ret:
		if size['width'] > num:
			num = size['width']
			url = size['url']
	ret = requests.get(url).content
	open('/tmp/'+str(pack['userid'])+'.jpg','wb').write(ret)
	os.system('convert /tmp/'+str(pack['userid'])+'.jpg  -liquid-rescale 50x50%\!  /tmp/'+str(pack['userid'])+'_out.jpg')
	sendpic('/tmp/'+str(pack['userid'])+'_out.jpg','Готово',pack['toho'])
	