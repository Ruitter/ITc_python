"""Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству символов и вывести на экран результат.
Copy
Введенный текст: сон машина стол книга девочка 
Результат: сон стол книга машина девочка"""
"""
print("Введите слова через пробел")
words = input().split()
#list1 = words.split()  Сокращаем код максимально)))
for i in words :
		x = len(i)
		print (x)
words.sort(key=x)	
print(words)
"""
text = input().split()
for i in sorted(text,key=lambda a: len(a)):
	print(text)