#3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

num = int(input("Type a number: "))

def pair_or_odd(num):
    if num % 2 == 0:
        return print(f"{num} es par")
    else:
        return print(f"{num} es impar")


pair_or_odd(num)