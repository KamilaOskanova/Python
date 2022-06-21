# Task 1:
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# weekday = int(input("Enter the number of the day of the week: "))

# if weekday == 6 or weekday == 7:
#     print("Hooray, this is a weekend.")
# elif 0 < weekday < 6:
#     print("Ohh, this is not a weekend.")
# else:
#     print("Invalid number. Enter the number from 1 to 7. ")


# Task 2:
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой
# оси она находится).

# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input("Enter the x coordinate: "))
# y = int(input("Enter the y coordinate: "))

# if x > 0 and y > 0:
#     print(f'x coordinate = {x} and y coordinate = {y} are in the first quarter.')
# elif x < 0 and y > 0:
#     print(f'x coordinate = {x} and y coordinate = {y} are in the second quarter.')
# elif x < 0 and y < 0:
#     print(f'x coordinate = {x} and y coordinate = {y} are in the third quarter.')
# elif x > 0 and y < 0:
#     print(f'x coordinate = {x} and y coordinate = {y} are in the fourth quarter.')
# else:
#     print("Invalid number. Your coordinates cannot be equal to zero. Try again.")


# Task 4
# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# from math import sqrt

# x_A = int(input("Enter the X coordinate of point A: "))
# y_A = int(input("Enter the Y coordinate of point A: "))
# x_B = int(input("Enter the X coordinate of point B: "))
# y_B = int(input("Enter the Y coordinate of point B: "))

# distance = sqrt((x_B - x_A)**2 + (y_B - y_A)**2)
# print(f"The distance between point A({x_A};{y_A}) and point B({x_B};{y_B}) is {round(distance,2)}.")
