months = ['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа']
randnum = random.randint(0,10)
if randnum <= 2:
	apisay(random.choice(['Когда Путин сольётся','Когда я перестану быть говнокодом','Когда ты сдохнешь']),pack['toho'])
else:
	apisay('Я уверена '+pack['user_text']+' '+str(random.randint(1,31))+' '+random.choice(months)+' '+str(random.randint(2019,2050)),pack['toho'])