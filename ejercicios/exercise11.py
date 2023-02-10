#11. Crear un programa que genere una lista de números pares entre 1 y 100.

def generate_even_numbers():

  even_numbers = []

  for i in range(2, 101, 2):

    even_numbers.append(i)

  return even_numbers

even_numbers = generate_even_numbers()

print(even_numbers)
