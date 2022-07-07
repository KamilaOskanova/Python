# Task 1:
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# import math

# def decimal_to_binary(decimal):
#     binary = ''

#     while(decimal>=1):
#         binary = str(math.floor(decimal%2)) + binary
#         decimal = decimal/2
#     return binary

# number = int(input('Enter the number: '))
# print (decimal_to_binary(number))


# Task 2:
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def Fibonacci(n):
#     if n == 0:
#         print('F(0) = 0')
#         return 0
        
#     if n > 0: 
#         list1 = []
#         fib1 = 0
#         fib2 = 1
#         list1.append(fib1)
#         list1.append(fib2)

#         for i in range(2, n+1):
#             fib1, fib2 = fib2, fib1 + fib2 
#             list1.append(fib2)

#         list2 = []
#         fib3 = 0
#         fib4 = 1
#         list2.insert(0, fib4)

#         for i in range(2, n+1):
#             elem = fib3 - fib4
#             fib3, fib4 = fib4, elem 
#             list2.insert(0, elem)
 
#         list2.extend(list1) 
#         print (str(list2))
#         return list2

# number = int(input('Enter your number: '))
# Fibonacci(number)

# Task 3:
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее 
# число. В качестве символа-разделителя используйте пробел.

# def max_and_min (str):
#     str = str.split(" ")
#     print(f'The maximum number is {max(str)}.')
#     print(f'The minimum number is {min(str)}.')

# string = '1 2 3 4 5 6'
# print(string)
# max_and_min(string)

# Task 4: 
# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import math

def least_common_multiple(a, b):
    print(math.lcm(a,b))

number_a = int(input("Enter the first number: "))
number_b = int(input("Enter the second number: "))
least_common_multiple(number_a, number_b)