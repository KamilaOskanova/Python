# Task 1:
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

#Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_of_odd_indexes (list):
#     for i in list:
#         sum_of_elements = sum(list[1::2])
#     print(f'The sum of the elements with odd indexes is {sum_of_elements}')
#     return sum_of_elements

# my_list = [2, 3, 5, 9, 3, 6, 77, 11]
# print(my_list)
# sum_of_odd_indexes(my_list)


# Task 2:
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


# def multiplication (list):
#     list2 = []

#     for i in range((len(list)+1)//2):
#         list2.append(list[i]*list[len(list)-1-i])
#     print (list2)
#     return list2


# numbers = [2, 3, 4, 5, 6, 7, 8]
# print (numbers, end = ' => ')
# multiplication(numbers)  # result: [2, 3, 4, 5, 6, 7, 8] => [16, 21, 24, 25]

# Task 3:
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def difference (list):
    list2 = []
    for i in range(len(list)):
        list2.append(round(list[i]-int(list[i]), 4))
    print(list2)
    max = list2[0]
    min = list2[0]

    for j in range(len(list2)):
        if list2[j] > max and list2[j] != 0:
            max = list2[j]
        if list2[j] < min and list2[j] != 0:
            min = list2[j]

    print(f'The maximum float part is {max}, the minimum float part is {min}')
    diff_result = round((max-min), 4)
    print(f'The difference between max and min is {diff_result}')
    return list2

float_list = [1.1, 1.2, 3.1, 5, 10.01]
print(float_list, end= ' => ')
difference(float_list)