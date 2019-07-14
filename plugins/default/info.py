import random
random.seed(sum([ord(x) for x in pack['user_text']]))
apisay('Вероятность того, что '+pack['user_text']+' равна '+str(random.randint(0,146))+'%',pack['toho'])