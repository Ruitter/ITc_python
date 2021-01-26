"""Попросить пользователя ввести текст. 
В результате вывести процент букв в верхнем регистре (заглавные) и в нижнем регистре (прописные)."""

print("Начнем? Введите текст")
x = input()
y = len(x)
print("Общее количество символов " + str(y))
y1 = x.count(" ")

big = 0
small = 0
for i in x :
 	if 'a' <= i <= 'z' : #Englsih
 		small += 1
 	if 'A' <= i <= 'Z' : # English
 		big += 1
 	if 'А' <= i <= 'Я' : # Russian
 		big += 1
 	if 'а' <= i <= 'я' : # Russian
 		small += 1
 	else :
 		pass
print("Больших букв " + str(big))
print("Маленьких букв" + str(small))
print("Пробелов и др.символов " + str(y - big - small))
