import re, __main__, os

def color(text,color):
	colors = {
		'black':'\u001b[30m',
		'red':'\u001b[31m',
		'green':'\u001b[32m',
		'yellow':'\u001b[33m',
		'blue':'\u001b[34m',
		'magenta':'\u001b[35m',
		'cyan':'\u001b[36m',
		'white':'\u001b[37m',
		'reset':'\u001b[0m'
	}	
	return colors[color]  +  str(text)  +  colors['reset']
def af(string):
	stuff = set(re.findall('\^.*?\^',string))
	newstring = string
	for x in stuff:
		if x != '%%':
			getvar = eval('' + x.replace('^',''))
			newstring = newstring.replace(str(x),str(getvar))
	stuff = set(re.findall('{.*?}',string))
	newstring = newstring
	for x in stuff:
		if x != '{}':
			getvar = eval('__main__.' + x.replace('{','').replace('}',''))
			newstring = newstring.replace(str(x),str(getvar))
	return newstring.replace('{','').replace('}','')
def clear():
	try:
		os.system('clear')
	except:
		pass
# def banner(text, height, border='='):
# 	rows, columns = os.popen('stty size', 'r').read().split()
# 	wi, hi = int(columns), int(rows)
# 	print(border*wi)
# 	text = text.split()
# 	count = 0
# 	adder = []
# 	for x in text:
# 		count = count + 1
# 		adder.append(x)
# 		if count%(5) == 0:
# 			if len(adder) > 0:
# 				print(border,end='')
# 				freespace = wi-2
# 				lnofstr = len(''.join(adder))+len(adder)
# 				pr = int((freespace-lnofstr)/2)
# 				print(' '*pr,end='')
# 				for b in adder:
# 					print(b,end=' ')
# 				print(' '*pr,end='')
# 				print(border+'\n',end='')
# 				adder = []
# 	print(border*wi)