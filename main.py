import requests, json, sqlite3, os, sys, psutil, threading, re, time, random, datetime, untangle
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
sys.path.append('plugins')

config = json.loads(open('config/bot.cfg','r').read())
cmds = json.loads(open('config/cmds.cfg','r').read())
commands = {}
token = config['group_token']
def apisay(text,toho,attachment=None,keyboard={"buttons":[],"one_time":True}):
	return requests.post('https://api.vk.com/method/messages.send',data={'access_token':token,'v':'5.80','peer_id':toho,'message':text,'attachment':attachment,'keyboard':json.dumps(keyboard,ensure_ascii=False)}).json()
def sendpic(pic,mess,toho,keyboard={"buttons":[],"one_time":True}):
	ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
	ret = requests.post(ret['response']['upload_url'],files={'photo':('photo.png',pic,'image/png')}).json()
	ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).json()
	requests.post('https://api.vk.com/method/messages.send',data={'attachment':'photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id']),'message':mess,'v':'5.80','peer_id':str(toho),'access_token':str(token),'keyboard':json.dumps(keyboard)})
def do_cmd(code,pack):
	exec(code)
			
for path in os.listdir('plugins'):
	commands[path] = {}
	if os.path.isdir('plugins/'+path):
		for plugin in os.listdir('plugins/'+path):
			commands[path][plugin] = open('plugins/'+path+'/'+plugin,'r').read()

start_time = time.monotonic()	
while True:
	active = False
	try:
		response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').json()
		ts = response['ts']
	except Exception as error:
		if error == KeyboardInterrupt:
			sys.exit(0)
		lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':config['group_token'],'v':'5.80','group_id':config['group_id']}).json()['response']
		ts = lpb['ts']
		continue

	for result in response['updates']:
		text = result['object']['text']
		payload = None
		msgid = result['object']['conversation_message_id']
		if 'payload' in result['object']:
			payload = result['object']['payload']
		if '@kbot5' in text:
			text = re.sub('\[club\d*\|@kbot5\]','@kbot5',text)
		text_split = text.split(' ')
		if text_split[0].lower() in config['names']:
			active = True
		if payload == '{"command":"start"}':
			active = True
			text = '@kbot5 помощь'
			text_split = text.split(' ')
		if len(text_split) > 2: user_text = text.replace(re.findall('\S* \S* ',text)[0],'')
		else: user_text = ''
		if text == 'F' and result['object']['from_id'] > 0: apisay('F',result['object']['peer_id'])
		
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
			lastmsgid = msgid
			if text_split[1] in cmds:
				threading.Thread(target=do_cmd,args=(commands[cmds[text_split[1]][0]][cmds[text_split[1]][1]],pack)).start()
