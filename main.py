"""Punto de entrada para probar estructuras y ejercicios rápidamente."""

from structures.trees.binary_tree import Node


def demo() -> None:
    print("=== Demo: structures.trees.binary_tree ===")
    left = Node(5)
    right = Node(15)
    root = Node(10, left=left, right=right)

    print(f"Nodo raíz : {root!r} (valor={root.value})")
    print(f"Hijo izq  : {root.left!r} (es hoja: {root.left.is_leaf})")
    print(f"Hijo der  : {root.right!r} (es hoja: {root.right.is_leaf})")
    print(f"¿Raíz es hoja? -> {root.is_leaf}")


def main() -> None:
    print("=" * 55)
    print("  algorithms_and_codes - Estructuras de Datos 2")
    print("=" * 55)
    print()
    demo()
    print()
    print("Comandos útiles:")
    print("  uv run pytest          -> Correr todas las pruebas")
    print("  uv run python main.py  -> Correr esta demo")
    print("  uv run python exercises/numeros_enteros.py -> Correr ejercicio")
    print("=" * 55)


if __name__ == "__main__":
    main()
