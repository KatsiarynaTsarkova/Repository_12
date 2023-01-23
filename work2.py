#Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того 
# товара, который закончился. Ответ. Закончилось: «Бурёнка»
data = open('prim.txt', mode="r", encoding='utf-8')
ass = data.readlines()
data.close()
print(ass)
assort = set(ass[1].split(', '))
warehouse =set(ass[2].split(', '))
print(assort.difference(warehouse))

