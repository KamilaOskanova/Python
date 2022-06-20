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

# list = []
# max = None
# for i in range(5):
#     list.append(int(input(f'list[{i}] = '))) # for filling the list
#     if list [i] > list[i-1]:
#         max = list[i]
# print(f'The max number is {max}')


# Task 3:
# Напишите программу, которая будет на вход принимать число N и выводить
# числа от -N до N

# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('Enter the number N: '))
# for i in range(-N, N+1):
#     print(i)


# Task 4:
# Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.

# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

