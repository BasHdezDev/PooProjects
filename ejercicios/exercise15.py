#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.


msg = input("Type a string: ")

def pali(msg):

  aux = ""
  for i in range(len(msg)-1,-1,-1):
    aux += msg[i]

  if msg == aux:
    x = print(f"{msg} and {aux} are palíndromes")
  else:
    x = print(f"{msg} and {aux} are not palíndromes")
  return x



pali(msg)