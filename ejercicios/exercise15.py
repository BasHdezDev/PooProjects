#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.


msg = input("Ingrese su mensaje: ")

def pali(msg):

  aux = ""
  for i in range(len(msg)-1,-1,-1):
    aux += msg[i]

  if msg == aux:
    x = print(f"{msg} y {aux} son palíndromos")
  else:
    x = print(f"{msg} y {aux} no son palíndromos")
  return x



pali(msg)