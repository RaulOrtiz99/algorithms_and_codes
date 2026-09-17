"""Ejercicios básicos de lógica con números enteros (paridad)."""


def par(a: int) -> bool:
    """Retorna True si el número entero 'a' es par, False en caso contrario."""
    return a % 2 == 0


def impar(a: int) -> bool:
    """Retorna True si el número entero 'a' es impar, False en caso contrario."""
    return not par(a)


def main() -> None:
    numero_1 = int(input("Ingrese un número por favor:\n"))
    if par(numero_1):
        print("El número es par.")
    else:
        print("El número es impar.")

    numero_2 = int(input("Ingresa un número por favor:\n"))
    if impar(numero_2):
        print("El número es impar.")
    else:
        print("El número es par.")


if __name__ == "__main__":
    main()
