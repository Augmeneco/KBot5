proxies = {'http': 'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}
blacklist = '-anthro+-fur+-scat*+-darling_in_the_franxx+-furry+-dragon+-guro+-animal_penis+-animal+-wolf+-fox+-webm+-my_little_pony+-monster*+-3d+-animal*+-ant+-insects+-mammal+-horse+-blotch+-deer+-real*+-shit+-everlasting_summer+-copro*+-wtf+'
parse = untangle.parse(requests.get('https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1000&tags='+blacklist+user_text.replace(' ','+'),proxies=proxies).text)
if int(parse.posts['count']) > 0:
	randnum = random.randint(0,len(parse.posts.post))
	mess = 'Дрочевня подкатила\n('+str(randnum)+'/'+str(len(parse.posts.post))+')\n----------\nОстальные теги: '+parse.posts.post[randnum]['tags']
	parse = parse.posts.post[randnum]['file_url']
	pic = requests.get(parse,proxies=proxies).content
	sendpic(pic, mess, pack['toho'])
else: apisay('Ничего не найдено :(',pack['toho'])
