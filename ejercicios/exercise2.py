#2. Escribir una función que calcule el área de un círculo dado su radio.

radio = float(input("Enter the radio of the circle: "))
def circlearea(radio):
    areais = (radio*radio)*3.14
    return print(f"The area of the circle is {areais}")

circlearea(radio)

