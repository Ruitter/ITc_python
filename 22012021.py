print("Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].")
print("Выведите все элементы, которые больше 5.")
print("Решение:")
print("")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list(a):
   if i > 5 :
    print(i)

print(" ")
print(" ")

print("Задача 2")
print("Есть набор чисел digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)")
print("Поделить каждое число из digits на 9 и вывести на экран.")
print("решение:")
print(" ")

digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for x in digits:
	print(x / 9)

print(" ")
print(" ")

print("Задача 3")
print("fruits = ('banana','stawberry','apple','orange','limon','ananas')")
print("Выведите первый и последний элемент списка.")
print(" ")

fruits = ('banana','stawberry','apple','orange','limon','ananas')
print(fruits[0], fruits[5])

print(" ")
print(" ")

print("Задача 4")
s1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
s2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
print(s1)
print(s2)
print(" ")
print (s1 == s2)
print(" ")
if s1[0] == s2[0] :
	print("0 индекс списков одинаков")
if s1[1] == s2[1] :
	print("1 индекс списков одинаков")
if s1[2] == s2[2] :
	print("2 индекс списков одинаков")
if s1[3] == s2[3] :
	print("3 индекс списков одинаков")
if s1[4] == s2[4] :
	print("4 индекс списков одинаков")
if s1[5] == s2[5] :
	print("5 индекс списков одинаков")
if s1[6] == s2[6] :
	print("6 индекс списков одинаков")
if s1[7] == s2[7] :
	print("7 индекс списков одинаков")

print(" ")
print(" ")
print("Задача 5")

porg1 = [range(300)]
for f in range(0, 301):
	if f >= 237 :
		break
	if f % 2 == 0 :
		print(f)
		



	

 






