def par(a):
    return a % 2 == 0

numero = int(input("Ingrese un número por favor:\n"))

if par(numero):
    print("El número es par.")
else:
    print("El número es impar.")


def impar(a):
    return not par(a)
numero = int(input("ingresa un numero porfavor:\n"))
if impar(numero):
    print("El numero es impar.")
else:
    print("El numero es par.")

