# `algorithms_and_codes`

Laboratorio personal y académico para la materia de **Estructuras de Datos 2**, con arquitectura limpia para integrar a futuro una aplicación web interactiva (**Data Structures Visualizer**).

---

## 📁 Estructura del Proyecto

Una estructura plana, intuitiva y organizada por unidades temáticas de la materia:

```text
algorithms_and_codes/
│
├── structures/                 # Código principal de estructuras (Python puro)
│   ├── trees/                  # Unidad: Árboles (Binario, BST, AVL, Heaps)
│   │   └── binary_tree.py      # Nodo y árbol binario base
│   ├── linear/                 # Unidad: Listas enlazadas, Pilas, Colas
│   └── graphs/                 # Unidad: Grafos y algoritmos de red
│
├── exercises/                  # Tus prácticas, retos y ejercicios de clase
│   └── numeros_enteros.py      # Ejercicios resueltos
│
├── tests/                      # Tests rápidos con pytest
│   ├── test_trees.py           # Tests de árboles
│   └── test_exercises.py       # Tests de ejercicios
│
├── apps/                       # Aplicaciones futuras (Visualizer)
│   ├── backend/                # Futuro: Django + Django Ninja (consumirá structures/)
│   └── frontend/               # Futuro: React + React Flow (visualización interactiva)
│
├── main.py                     # Script para probar rápidamente en consola
├── pyproject.toml              # Configuración con uv y pytest
└── .gitignore                  # Higiene del repositorio
```

---

## ⚡ ¿Cómo trabajar en el día a día?

### 1. Crear una nueva estructura (Ejemplo: Árbol AVL)
Cuando tu docente avance a un nuevo tema, no tienes que crear carpetas complejas:
1. Creas el archivo directamente en su unidad: `structures/trees/avl.py`.
2. Creas su test en: `tests/test_avl.py`.
3. Ejecutas las pruebas con:
   ```bash
   uv run pytest
   ```

### 2. Resolver ejercicios de clase
Colocas tus ejercicios directamente en `exercises/` (por ejemplo `exercises/taller_arboles.py`) e importas tus estructuras con total normalidad:
```python
from structures.trees.binary_tree import Node
```

### 3. Futuro Visualizer
Cuando desarrollemos la aplicación web:
- `apps/backend` (Django Ninja) importará directamente `from structures.trees... import ...`.
- `apps/frontend` (React + React Flow) consumirá la API para pintar los nodos y animaciones en pantalla.

---

## 🚀 Comandos Rápidos

```bash
# 1. Instalar dependencias
uv sync

# 2. Ejecutar la demo principal
uv run python main.py

# 3. Correr todas las pruebas unitarias
uv run pytest -v

# 4. Correr un ejercicio específico
uv run python exercises/numeros_enteros.py
```

---

## 🌿 Estrategia de Git (Ramas)

- **`main`**: Representa el código estable y probado.
- Crea ramas cortas para cada avance de la materia:
  - `feature/bst`
  - `feature/avl`
  - `feature/linked-list`
  - `feature/dijkstra`
  - `feature/visualizer-backend`
  - `feature/visualizer-frontend`

---

## 🗺️ Roadmap de la Materia

- [x] **Base limpia y modular**: Organización por unidades, pytest y uv.
- [x] **Nodo base de Árbol Binario (`Node`)** y tests unitarios.
- [ ] **Binary Search Tree (BST)**: Inserción, búsqueda, eliminación y recorridos (Inorder, Preorder, Postorder, BFS).
- [ ] **Árboles AVL**: Balanceo automático y rotaciones (LL, RR, LR, RL).
- [ ] **Estructuras Lineales**: Listas enlazadas simples, dobles y circulares.
- [ ] **Grafos**: Matriz/lista de adyacencia, BFS, DFS, Dijkstra.
- [ ] **Visualizer Backend**: Django + Django Ninja API.
- [ ] **Visualizer Frontend**: React + React Flow interactivo.
