#proxies = {'http': 'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}
parse = untangle.parse(requests.get('http://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1000&tags='+user_text.replace(' ','+')).text)
if int(parse.posts['count']) > 0:
	randnum = random.randint(0,len(parse.posts.post))
	mess = 'Бурятские артики\n('+str(randnum)+'/'+str(len(parse.posts.post))+')\n----------\nОстальные теги: '+parse.posts.post[randnum]['tags']
	parse = parse.posts.post[randnum]['file_url']
	pic = requests.get(parse).content
	sendpic(pic, mess, pack['toho'])
else: apisay('Ничего не найдено :(',pack['toho'])
