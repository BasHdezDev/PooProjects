#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def find_min_max(numbers):

  min_num = numbers[0]

  max_num = numbers[0]

  for num in numbers:

    if num < min_num:

      min_num = num

    elif num > max_num:

      max_num = num

  return (min_num, max_num)

numbers = [3, 5, 2, 8, 1]

print(find_min_max(numbers))


