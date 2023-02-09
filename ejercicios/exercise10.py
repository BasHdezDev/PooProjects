#10. Escribir una función que calcule el factorial de un número dado.

n=int(input("Type a number: "))

def fact(n):

  f = 1

  for i in range(1,n+1):
    f *= i
  return print(f"The factorial of {n} is {f}")

fact(n)