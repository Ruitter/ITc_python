# Задачи на занятии

print ("Посмотреть задачу 23? y/n")
y = input()
if y == "y" or y == "Y" : # Как сделать так, чтобы считывались данные с ввода? и проверялось на выполнение условий
#Задача 23
	print("Как вас зовут?")
	name = input()
	print("Добро пожаловать, " + name + "!")
	print ("Какой фильм желаете посмотреть?")
	film = input()
	print("Вы выбрали " + film + ", отличный выбор!")
	print("Приятного просмотра, " + name)
else :
	pass

print(" " * 2)

print ("Посмотреть задачу 31? y/n")
y = input()
if y == "y" or y == "Y" :
	txt = "Google создаст специальную команду для поиска багов в особо важных приложениях"
	num_of_words = len(txt.split())
	print (num_of_words)
else : 
	pass

print(" " * 2)

print ("Посмотреть задачу 11? y/n")
y = input()
if y == "y" or y == "Y" :
	txt1 = "Пхакеры слили в сеть данные пакистанской энергетической компании k-Electric"
	print(txt1.title())
else :
	pass

print(" " * 2)

print ("Посмотреть задачу 2? y/n")
y = input()
if y == "y" or y == "Y" :
	txt2 = "GitHub"
	print(txt2)
	print("введите символ, которым хотите разделить строку выше")
	simbol = input().join(txt2)
	print(simbol)
else :
	pass

print(" " * 2)
print ("Посмотреть задачу 5? y/n")
y = input()
if y == "y" or y == "Y" :
	txt4 = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
	print (txt4)
	print("После выполнения условий".upper())
	txt5 = txt4.replace("е", "3")
	print(txt5)
else :
	pass

print(" " * 2)

print ("Посмотреть задачу 0? y/n")
y = input()
if y == "y" or y == "Y" :
	print("Привет, как тебя зовут?")
	name = input()
	print("Рад знакомству, " + name.upper() + ". Меня зовут Сири")
	print("Where do we go now " + name.upper() + "?")
	adress = input()
	print("Okay, lets go to " + adress.lower())
else :
	pass

print(" " * 2)

print ("Посмотреть задачу 1? y/n")
y = input()
if y == "y" or y == "Y" : 
	y = 3 > 2
	print(str(3 > 2) + " - это строка")




