#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def multip(n):
    if n == 1:
        return 1
    else:
        return n * multip(n - 1)


num = int(input("Введите число: "))

list = []
for e in range(1, num + 1):
    list.append(multip(e))

print(f"Произведения чисел от 1 до {num}:  {list}")