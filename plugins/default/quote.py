if 'reply_message' in longpoll[pack['userid']]['object']:
	fwd_messages = []
	fwd_messages.append(longpoll[pack['userid']]['object']['reply_message'])
else:
	fwd_messages = longpoll[pack['userid']]['object']['fwd_messages']	

img = Image.new('RGB', (500,10000), color = (255,255,255))
imgByteArr = BytesIO()
offset_y = 0
last_id = 0

for message in fwd_messages:
	if message['from_id'] < 0:
		user_info = requests.post('https://api.vk.com/method/groups.getById',data={'access_token':config['group_token'],'v':'5.90','group_ids':message['from_id']}).json()['response'][0]
		name = user_info['name']
	else:
		user_info = requests.post('https://api.vk.com/method/users.get',data={'access_token':config['group_token'],'v':'5.90','fields':'photo_50','user_ids':message['from_id']}).json()['response'][0]
		name = user_info['first_name']+' '+user_info['last_name']
	
	text = message['text']
	
	font_regular = ImageFont.truetype('data/Roboto-Regular.ttf', 17)
	font_medium = ImageFont.truetype('data/Roboto-Medium.ttf', 18)
	draw = ImageDraw.Draw(img)
	
	
	if last_id != message['from_id']:
		ava = user_info['photo_50']
		ava = requests.get(ava,stream=True).raw
		ava = Image.open(ava)
		ava = ava.resize([50,50])
		img.paste(ava,[10,10+offset_y,60,60+offset_y])
		draw.text([70,14+offset_y],name,font=font_medium,fill=(66,100,139))
	
	textnew = textwrap.fill(text, 50).split('\n')
	y = 35
	text_size = 0
	if last_id == message['from_id']:
		offset_y -= 30
	for wrap in textnew:
		draw.text([70,y+offset_y],wrap,font=font_regular,fill=(0,0,0))
		text_size += draw.textsize(wrap,font=font_regular)[1]
		y += 19
		
	offset_y += text_size+40
	last_id = message['from_id']
	
img = img.crop([0,0,img.size[0],offset_y+10])
img.save(imgByteArr,format='PNG')
sendpic(imgByteArr.getvalue(),'Готово',pack['toho'])
