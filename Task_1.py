# Задача 1. 
# Напишите программу, которая принимает на вход
# большое число и показывает его цифру.
# Без работы с последовательностями строк.
# вход -> выход
# - 6782 -> 23
# - 0,67 -> 13
# - 198,45 -> 27

num = input("Enter the number: ")
sum = 0
for i in num:
    if i!=".":
        sum = sum + int(i)
print(f"The sum of the {num} is: ", sum)