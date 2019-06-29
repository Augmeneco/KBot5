from PIL import Image
longpoll[pack['userid']]=result

if 'photo' in longpoll[pack['userid']]['object']['attachments'][0]:
	ret = longpoll[pack['userid']]['object']['attachments'][0]['photo']['sizes']
	num = 0
	for size in ret:
		if size['width'] > num:
			num = size['width']
			url = size['url']
	ret = requests.get(url).content
	image_obj = Image.open(BytesIO(ret))
	imgByteArr = BytesIO()
	if 'лол' in pack['user_text']:
		image2 = image_obj.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
		image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
		image_obj.paste(image2,(int(image_obj.size[0]/2),0))
		image_obj.save(imgByteArr,format='PNG')
		sendpic(imgByteArr.getvalue(),'',pack['toho'])
	else:
		image2 = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		image2 = image2.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
		image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
		image_obj = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		image_obj.paste(image2,(int(image_obj.size[0]/2),0))
		image_obj.save(imgByteArr,format='PNG')
		sendpic(imgByteArr.getvalue(),'',pack['toho'])
