if 'photo' in longpoll[pack['userid']]['object']['attachments'][0]:
	apisay('Жмыхаю картинку... создание шок контента может занять до 20 секунд',pack['toho'])
	ret = longpoll[pack['userid']]['object']['attachments'][0]['photo']['sizes']
	num = 0
	for size in ret:
		if size['width'] > num:
			num = size['width']
			url = size['url']
	ret = requests.get(url).content
	img_size = Image.open(BytesIO(ret))
	size = img_size.size
	img_size.close()
	
	open('/mnt/tmpfs/'+str(pack['userid'])+'.jpg','wb').write(ret)
	os.system('convert /mnt/tmpfs/'+str(pack['userid'])+'.jpg  -liquid-rescale 50x50%\!  /mnt/tmpfs/'+str(pack['userid'])+'_out.jpg')
	image_obj = Image.open('/mnt/tmpfs/'+str(pack['userid'])+'_out.jpg')
	imgByteArr = BytesIO()
	image_obj = image_obj.resize(size)
	image_obj.save(imgByteArr,format='PNG')
	sendpic(imgByteArr.getvalue(),'Готово',pack['toho'])
	os.system('rm /mnt/tmpfs/'+str(pack['userid'])+'_out.jpg')
	os.system('rm /mnt/tmpfs/'+str(pack['userid'])+'.jpg')
	image_obj.close()
else:
	apisay('Картинку сунуть забыл',pack['toho'])
