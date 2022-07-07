# Task 33:
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 

# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from pathlib import Path


# def random_coeff (k):
#     eq_list = [randint(0,100)]
#     equation = str(eq_list[0])
#     for i in range(1,k+1):
#         eq_list.append(randint(0,100))
#         if eq_list[-1] == 0 : continue
#         equation = f'{eq_list[-1]}*x^{i} + '+ equation
       
#     equation = equation.replace('x^1 ','x ') 
#     equation = equation.replace(' 1*',' ')
#     equation = equation.replace(' + 0','') 


#     file_path = Path("Seminar5/Task33_Equation.txt")
#     f = open(file_path, 'w')
#     f.write(equation + " = 0")
#     f.close()
#     return eq_list

# coeff = int(input('Enter the power of the polynomial: '))
# print(random_coeff(coeff))

# Task 35: 
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

# path = Path("Seminar5/Task35_Numbers.txt")
# data = open(path, 'r') 
# for line in data:
#     numbers = ''
#     numbers += line 
# data.close()

# numbers = [int (x) for x in numbers.split()]
# print(f'List of numbers = {numbers}')
# sorted_numbers = sorted(numbers)
# print(f'Sorted list of numbers = {sorted_numbers}')

# def lost_number(list):
#     numb = ''
#     for i in range(len(list)):
#         if i > 0: 
#             if not list[i] - 1 == list[i-1]:
#                 numb = list[i]-1 
#     return numb

# lost_number(sorted_numbers)
# print(f'The lost number is {lost_number(sorted_numbers)}') 

# Task 43: 
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

input_list = list(input('Enter the numbers separated by spaces: '))

def unique_list(list):
    uniq_list = [i for i in list if list.count(i) < 2]  
    return uniq_list 
 
input_list.sort()
print(unique_list(input_list))