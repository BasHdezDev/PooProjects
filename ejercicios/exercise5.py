#5. Crear una función que convierta grados Fahrenheit a grados Celsius.

fah = float(input("Type a fahrenheit degree: "))

def fah_to_cel(fah):
  cel=(fah-32)/1.8
  return print(f"{fah} fahrenheit are {cel} celsius")

fah_to_cel(fah)