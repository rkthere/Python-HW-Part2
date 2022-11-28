#3.Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

n = int(input("Введите число: "))
def ListFill(n):
        if n > 0:
                return (1+1/i)**i
        else:
                return 1

list = []
for i in range(1, n + 1):
        list.append(ListFill(i))

print(f'Сумма чисел -> {sum(list)} \nПоследовательноcть -> {list}')