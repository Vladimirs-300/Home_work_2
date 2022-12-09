# Задача 3. 
# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их количество.

n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / n)**n, 2) for n in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))



