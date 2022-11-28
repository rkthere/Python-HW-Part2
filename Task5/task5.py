#5 Реализуйте алгоритм перемешивания списка.
#Из библиотеки random использовать можно только randint
import random

def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list

N = int(input('Введите N  '))
a = list(range(1, N+1))
mixed_list = mix_list(a)
print("Исходный список: ")
print(a)
print("Перемешанный список: ")
print(mixed_list)