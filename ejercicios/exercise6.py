#6. Crear un programa que calcule la suma de los números en una lista dada.

list = [1,23,4,14,21]

index = len(list)

sum = 0

for i in range(0,index,+1):
    sum = list[i] + sum


print(f"The sum of the numbers of the list is {sum}")