print ("Посмотреть задачу 1? y/n")
y = input()
if y == "y" or y == "Y" :
	set1 = {123, 456}
	set2 = {'asd', 'zxc', 'dfg'}
	set3 = {'tyu', 'ghj', 'vbn'}
	global_set = {set1 , set2, set3}
	print(global_set)
else :
	pass

print ("Посмотреть задачу 3? y/n")
y = input()
if y == "y" or y == "Y" :
	names = {'Ali', 'Kayrat', 'Teacher', "Anything", 'Cat'}
	print(names)
	print('Добавьте 1 элемент в список')
	names.add(input())
	print(names)
	print('Delete one word random')
	names.pop()
	print(names)
else :
	pass

print ("Посмотреть задачу 000? y/n")
y = input()
if y == "y" or y == "Y" :
	menu = {
		'lagman': 120,
		'plov': 120,
		'borsh': 100 }
	print(menu)	
	menu ['besh_barmak'] = 130
	menu ['lagman'] = 135
	del menu ['borsh']
	print(menu)
else :
	pass

print ("Посмотреть задачу 10? y/n")
y = input()
if y == "y" or y == "Y" :
	menu = {
		'lagman': 120,
		'plov': 120,
		'borsh': 100 }
	print(menu)
	menu ['drinks'] = ['Coka-Cola', 'Fanta', 'Sprite']
	print(menu)
else :
	pass

print ("Посмотреть задачу 020? y/n")
y = input()
if y == "y" or y == "Y" :
	set_work = {'add', 'remove', 'clear', 'update', 'pop', 'copy'}
	dict_work = {'clear', 'keys', 'items', 'get', 'copy'}
	print(set_work)
	print(dict_work)
	print(set_work.intersection(dict_work))
else :
	pass

print ("Посмотреть задачу 31? y/n")
y = input()
if y == "y" or y == "Y" :
	dic = {}
	x = len(dic)
	for x in range (3) :
		print ('Введите имя пользователя')
		a = input()
		print('Введите пароль')
		b = input()
		dic[a] = b
		print(dic)
else :
	pass








