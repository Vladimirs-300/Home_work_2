# Задача 1.
# Напишите программу, которая принимает на вход
# большое число и показывает его цифру.
# Без работы с последовательностями строк.
# вход -> выход
# - 6782 -> 23
# - 0,67 -> 13
# - 198,45 -> 27

number = input('Введите число: ')

sum = 0
for i in number:
    if i != '.':
        sum += int(i)
print(sum)