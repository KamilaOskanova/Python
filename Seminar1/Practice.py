# Task 1:
# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# Примеры:
# 5, 25 -> да
# 25, 5 -> да
# 8,9 -> нет

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))

# if a**2 == b:
#     print(f"Yes, the second number {b} is the squared first number {a}")
# elif b**2 == a:
#     print(f"Yes, the first number {a} is the squared second number {b}")
# else:
#     print("No, these numbers are not squares of each other")


# Task 2:
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# max = int(input('1 number: '))
# for i in range(2, 6):
#     a = int(input(f'{i} number: ')) # for filling the list
#     if a > max:
#         max = a
# print(f'The max number is {max}')


# Task 3:
# Напишите программу, которая будет на вход принимать число N и выводить
# числа от -N до N

# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('Enter the number N: '))
# for i in range(-N, N+1):
#     print(i, end = " ") # for adding spaces between numbers and showing them in a line


# Task 4:
# Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.

# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# from math import trunc

# a = float(input("Enter the float number: "))
# a = trunc (a % 1 * 10)
# print(a) # this doesn't work when after the dot there are number >= 5, it round up

# from fractions import Fraction 
# from math import trunc
# floatnumbers = float(input("Введите число: "))
# if floatnumbers:
#   finalresult = trunc(Fraction(floatnumbers)*10 % 10)
#   print(finalresult)
# else:
#   print('Результат отрицательный')

# Класс Fraction (class fractions.Fraction(float)),  импортируемый из модуля 
# fractions (поддержка рациональных чисел), позволяет также нам производить 
# различные действия с дробями, создавать свои экземпляры классов

# Метод trunc() отбрасывает знаки после запятой, возвращает усеченную 
# целую часть числа. Примечание. Этот метод НЕ округляет число вверх/вниз 
# до ближайшего целого числа, а просто удаляет десятичные дроби.



# Task 5:
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input("Enter the number: "))

# if num % 10 == 0:
#     print("Unvalid number")
# elif num % 15 == 0:

#     if  or num % 10


# Task 6:
# На столе стоит две корзины с яблоками. Корзина a и корзина b. Введите количество яблок с клавиатуры. 
# Затем поменяйте содержимое корзин местами и выведите результат.

# Например, если пользователь ввёл 5 и 7, то до обмена a=5, b=7, а после a=7 и b=5.



# Task 7: 
# Пишем "компьютерный вирус". Запросите у пользователя любой текст. 
# Сохраните вторую с начала и третью с конца буквы в отдельные переменные (например a и b). 
# Замените во всём тексте букву из переменной a, на букву из переменной b и выведите зашифрованный 
# текст на экран. Пример до шифровки: "Однажды, в студеную зимнюю пору, я из лесу вышел; был сильный мороз". 
# Пример после шифровки: "Орнажры, в стуреную зимнюю пору, я из лесу вышел; был сильный мороз".



# Task 8: 
# Напишите программу, которая проверит истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# x = input()
# y = input()

# if not(x or y) == (not(x) and not(y)):
#     print("Выражение истинно")
# else:
#     print("Выражение ложно")