index = html.fromstring(requests.get('https://furry.booru.org/index.php?page=post&s=list&tags=all&pid='+str(random.randint(0,1731420))).text)
index = index.xpath('//span[@class="thumb"]/a')
url = etree.tostring(index[random.randint(0,len(index)-1)]).decode()
url = 'https://furry.booru.org/'+re.findall('href="(.*)">',url)[0].replace('&amp;','&')

index = html.fromstring(requests.get(url).text)
img = index.xpath('//img[@id="image"]')[0]
img = re.findall('src="(.*)" id',etree.tostring(img).decode())[0]
tags_list = ''
tags = index.xpath('//ul[@id="tag-sidebar"]/li')
del tags[len(tags)-1]
for tag in tags:
	tags_list += re.findall('tags=(.*)">(.*)</a>',etree.tostring(tag).decode())[0][1]+' '

mess = 'Фурри-дрочево подкатило\n----------\nОстальные теги: '+tags_list
pic = requests.get(img).content
sendpic(pic, mess, pack['toho'])
