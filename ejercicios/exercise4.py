#4. Escribir un programa que determine si un número dado es par o impar.

num = int(input("Type a number: "))

def pair_or_odd(num):
    if num % 2 == 0:
        return print(f"{num} is pair")
    else:
        return print(f"{num} is odd")


pair_or_odd(num)

