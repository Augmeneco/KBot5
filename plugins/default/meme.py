index = html.fromstring(requests.get('https://meme.booru.org/index.php?page=post&s=list&tags=all&pid='+str(random.randint(0,152400))).text)
index = index.xpath('//span[@class="thumb"]/a')
url = etree.tostring(index[random.randint(0,len(index)-1)]).decode()
url = 'https://meme.booru.org/'+re.findall('href="(.*)">',url)[0].replace('&amp;','&')

index = html.fromstring(requests.get(url).text)
img = index.xpath('//div[@id="note-container"]/img')[0]
img = re.findall('src="(.*)" id',etree.tostring(img).decode())[0]
tags_list = ''
tags = index.xpath('//div[@id="tag_list"]/ul/li')
del tags[len(tags)-1]
for tag in tags:
	tags_list += re.findall('tags=(.*)">',etree.tostring(tag).decode())[0]+' '

mess = 'Мемасик\n----------\nОстальные теги: '+tags_list
pic = requests.get(img).content
sendpic(pic, mess, pack['toho'])
