# Task 34:
# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

# path = 'Seminar6/first_polynomial.txt'
# data = open(path, 'r')
# for line in data:
#     first_poly = ''
#     first_poly += line      
# data.close()

# path = 'Seminar6/second_polynomial.txt'
# sp = open(path, 'r')
# for line in sp:
#     second_poly = ''
#     second_poly += line       
# sp.close()

# def concat_and_convert_to_list(first_poly, second_poly):
#     two_poly = ''
#     two_poly = first_poly + '+' + second_poly
#     split_poly = two_poly.split('+')
#     return split_poly
    
# def polynomial_to_dict(polynom):    
#     dict = {}

#     for element in polynom:
#         second_split_poly = element.strip().split('*') 
#         if len(second_split_poly) >= 1:
#             if second_split_poly[1] in dict.keys():     
#                 dict[second_split_poly[1]] = dict[second_split_poly[1]] + int(second_split_poly[0]) 
#             else:
#                 dict[second_split_poly[1]] = int(second_split_poly[0])
#         else:
#             if 0 in dict.keys():
#                 dict[0] = dict[0] + int(second_split_poly[0])
#             else:
#                 dict[0] = int(second_split_poly[0])
    
#     result = ''

#     for i in dict:
#         if result != '':
#             result += '+'
#         result += str(dict[i])
#         if i != 0:
#             result += '*' + i
#     return result

# decision = polynomial_to_dict(concat_and_convert_to_list(first_poly, second_poly))

# dt = open('Seminar6/sum_of_polynomials.txt', 'w')
# dt.write(decision)     
# dt.close()


# Task 42:
# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a. входные и выходные данные хранятся в отдельных текстовых файлах

def coding(string_arg):
    string_result = ''
    list_result = []
    n = 1
    for i in range(len(string_arg)-1):
        if string_arg[i] == string_arg[i + 1]:
            n +=1
        else:
            string_result +=  (str(n)+string_arg[i])+','
            n = 1
    string_result += (str(n)+string_arg[i])
    return string_result


def decoding(string_arg):
    list1 = string_arg.split(',')
    string_result = ''
    for i in range(len(list1)):
        string_result += int(list1[i][:-1])*list1[i][-1]
    return string_result


def file_write(file_name, polinom_str):    
    with open(file_name, 'w') as data:
        data.write(polinom_str)


def file_read(file_name):
    data = open(file_name, 'r')
    for line in data:
        polinom = line
    data.close
    return polinom

file_write('Seminar6/inital_data.txt', '111111111111111111222222222222222222')
file_write('Seminar6/encoded_data.txt', coding(file_read('Seminar6/initial_data.txt')))
file_write('Seminar6/decoded_data.txt', decoding(file_read('Seminar6/encoded_data.txt')))

# Task 39:
# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 