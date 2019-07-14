print(longpoll[pack['userid']]['object'])
if 'reply_message' in longpoll[pack['userid']]['object']:
	kickid = longpoll[pack['userid']]['object']['reply_message']['from_id']
else:
	kickid = longpoll[pack['userid']]['object']['fwd_messages'][0]['from_id']
data = {'access_token':config['group_token'],'chat_id':pack['toho']-2000000000,'member_id':kickid,'v':'5.90'}
requests.post('https://api.vk.com/method/messages.removeChatUser',data=data)
