import requests, json, sqlite3, os, sys, psutil, threading, re, time, random, datetime, untangle, subprocess, textwrap
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back, Style

config = json.loads(open('config/bot.cfg','r').read())
cmds = json.loads(open('config/cmds.cfg','r').read())
commands = {}
users_db = sqlite3.connect('data/users.db')
token = config['group_token']
def apisay(text,toho,attachment=None,keyboard={"buttons":[],"one_time":True}):
	try:
		requests.post('https://api.vk.com/method/messages.send',data={'access_token':token,'v':'5.80','peer_id':toho,'message':text,'attachment':attachment,'keyboard':json.dumps(keyboard,ensure_ascii=False)}).json()
	except:
		print(datetime.datetime.today().strftime("%H:%M:%S")+' | ['+Fore.RED+'+'+Style.RESET_ALL+'] Ошибка отправки сообщения в '+str(pack['toho']))
def sendpic(pic,mess,toho,keyboard={"buttons":[],"one_time":True}):
	try:
		ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
		try:
			with open(pic, 'rb') as f:
				ret = requests.post(ret['response']['upload_url'],files={'file1': f}).json()
		except:
			ret = requests.post(ret['response']['upload_url'],files={'photo':('photo.png',pic,'image/png')}).json()
		ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).json()
		requests.post('https://api.vk.com/method/messages.send',data={'attachment':'photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id']),'message':mess,'v':'5.80','peer_id':str(toho),'access_token':str(token),'keyboard':json.dumps(keyboard)})
	except KeyError:
		print(datetime.datetime.today().strftime("%H:%M:%S")+' | ['+Fore.RED+'+'+Style.RESET_ALL+'] Ошибка отправки сообщения в '+str(pack['toho']))
		apisay('Что-то пошло не так :(',toho)
				
def do_cmd(code,pack):
	exec(code)
			
for path in os.listdir('plugins'):
	commands[path] = {}
	if os.path.isdir('plugins/'+path):
		for plugin in os.listdir('plugins/'+path):
			commands[path][plugin] = open('plugins/'+path+'/'+plugin,'r').read()

uses_kb = 0
start_time = time.monotonic()	
longpoll = {}

while True:
	active = False
	try:
		response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').json()
		ts = response['ts']
	except Exception as error:	
		if error == KeyboardInterrupt:
			os._exit(0)
		try:
			lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':config['group_token'],'v':'5.80','group_id':config['group_id']}).json()['response']
		except Exception as error:	
			if error == KeyboardInterrupt:
				os._exit(0)
			continue
			
		ts = lpb['ts']
		continue

	for result in response['updates']:
		longpoll[result['object']['from_id']] = result
		text = result['object']['text']
		payload = None
		msgid = result['object']['conversation_message_id']
		
		
		if 'payload' in result['object']:
			payload = result['object']['payload']
		if '@kbot5' in text:
			text = re.sub('\[club\d*\|@kbot5\]','@kbot5',text)
		text_split = text.split(' ')
		if text_split[0].lower() in config['names'] and len(text_split) >= 2:
			active = True
		if payload == '{"command":"start"}':
			active = True
			text = '@kbot5 помощь'
			text_split = text.split(' ')
		if len(text_split) > 2: 
			user_replace_text = re.findall('\S* \S* ',text)
			if len(user_replace_text) != 0:
				user_text = text.replace(user_replace_text[0],'')
		else: user_text = ''
		if text.lower() == 'f' and result['object']['from_id'] > 0: apisay('F',result['object']['peer_id'],attachment='photo-158856938_457255856')
		
		if active:
			toho = result['object']['peer_id']
			userid = result['object']['from_id']
			pack = {}
			pack['text'] = text
			pack['toho'] = toho
			pack['userid'] = userid
			pack['payload'] = payload
			pack['msgid'] = msgid
			pack['user_text'] = user_text
			pack['text_split'] = text_split
			
			print(datetime.datetime.today().strftime("%H:%M:%S")+' | ['+Fore.GREEN+'+'+Style.RESET_ALL+'] Упоминание Кбота в '+str(pack['toho'])+' с текстом '+pack['text'])
			uses_kb += 1
			
			lastmsgid = msgid
			users_db_tmp = users_db.cursor().execute('SELECT * FROM users WHERE id = '+str(userid)).fetchall()
			
			if len(users_db_tmp) != 0:
				user_mode = users_db_tmp[0][1]
			else: user_mode = 1
			if len(text_split) < 2: continue
			text_split[1] = text_split[1].lower()
			if text_split[1] in cmds:
				if cmds[text_split[1]][0] == 'admin' and user_mode == 3:
					threading.Thread(target=do_cmd,args=(commands['admin'][cmds[text_split[1]][1]],pack)).start()
					continue
				elif cmds[text_split[1]][0] == 'admin' and user_mode != 3:
					apisay('Пшол вон из админки',toho)
					continue
				if cmds[text_split[1]][0] == 'vip' and (user_mode == 3 or user_mode == 2):
					threading.Thread(target=do_cmd,args=(commands['vip'][cmds[text_split[1]][1]],pack)).start()
					continue
				elif cmds[text_split[1]][0] == 'admin' and (user_mode != 3 or user_mode != 2):
					apisay('У вас нет доступа к вип командам',toho)
					continue
				if user_mode == 0:
					apisay('Вам бан',toho)
					continue
				if user_mode > 0:
					threading.Thread(target=do_cmd,args=(commands['default'][cmds[text_split[1]][1]],pack)).start()		
					continue			
			else:
				if text_split[1] in ['поиск','библиотека','читать с начала','читать с указанной главы','удалить мангу','выход','34gif','34pic']:
					continue 
				speak = requests.post('https://isinkin-bot-api.herokuapp.com/1/talk',data={'q':text.replace(text.split(' ')[0],'')}).json()
				if 'text' in speak: apisay(speak['text'],toho)
				else: apisay('Команда не найдена :(', toho)
