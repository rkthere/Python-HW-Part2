#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число для показа суммы его цифр -> ')


def sumNums(nums):
    sum = 0 
    for i in str(nums):
        if i != ",":
            sum += int(i)
    return sum

sumNums(num)
print(sumNums(num))
