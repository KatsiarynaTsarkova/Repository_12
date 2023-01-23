#Задача 1. Задайте натуральное число N. Напишите программу, которая составит
#список простых множителей числа N.
#60 -> 2, 2, 3, 5
number = int(input('Введите число: '))
print(number) 
for i in range(number, 1, -1):
    n = 0
    if (number % i == 0):
        for j in range(i, 1, -1):
            if (i % j == 0):
                n +=1
print(i, end = ',')  