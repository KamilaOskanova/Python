# Task 1:
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр(отсекаем минус, считаем все в плюс).

# Пример:
# 67,82 -> 23
# 0,56 -> 11

# def SumOfDigitsInFloat (num):
#     num = abs(num)
#     num = str(num)

#     sum = 0
#     for digit in num:
#         if digit.isdigit():
#             digit = int(digit)
#             sum += digit
    
#     print(sum)

# user_num = float(input('Enter the decimal number: '))
# SumOfDigitsInFloat(user_num)

# Task 2:
# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)


# def Factorial (number):
#     result = 1

#     for i in range(1,number+1):
#         result*=i
#         print(result, end = ' ')


# fact_num = int(input("Enter the number: "))
# if fact_num <=0:
#     print("Please, enter the number more than 0.")
# else:
#     Factorial(fact_num)

# Task 3:
# Реализуйте случайное перемешивания списка.

# *Пример:*
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] 
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']

import random

list = ['Веселый пианист', 250, 3.14, 'True ']
print(list)

random.shuffle(list)
print(list)