parse = untangle.parse('http://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1000&tags='+user_text.replace(' ','+'))
randnum = random.randint(0,len(parse.posts.post))
mess = 'Бурятские артики по запросу\n('+str(randnum)+'/'+str(len(parse.posts.post))+')\n----------\nОстальные теги: '+parse.posts.post[randnum]['tags']
parse = parse.posts.post[randnum]['file_url']
pic = requests.get(parse).content

sendpic(pic, mess, pack['toho'])


