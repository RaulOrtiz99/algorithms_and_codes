from structures.trees.binarytree.nodo import Nodo


class ArbolBinario: 

    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None 

    def inorden(self):
        elementos = []
        self.inorden_recursivo(self.raiz, elementos)
        return elementos

    def inorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual is None:
            return 
        self.inorden_recursivo(nodo_actual.izquierdo,elementos)
        elementos.append(nodo_actual.dato)
        self.inorden_recursivo(nodo_actual.derecho,elementos)

    def preorden(self):
        elementos = []
        self.preorden_recursivo(self.raiz, elementos)
        return elementos

    def preorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual is None:
            return 
        elementos.append(nodo_actual.dato)
        self.preorden_recursivo(nodo_actual.izquierdo,elementos)
        self.preorden_recursivo(nodo_actual.derecho,elementos)

    def postorden(self):
        elementos = []
        self.postorden_recursivo(self.raiz, elementos) 
        return elementos


    def postorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual is None: 
            return 
        self.postorden_recursivo(nodo_actual.izquierdo,elementos)
        self.postorden_recursivo(nodo_actual.derecho,elementos)
        elementos.append(nodo_actual.dato)

    #metodo para insertar un nodo en un arbol vacio 

    def insertar(self,dato):
        if self.esta_vacio():
            self.raiz = Nodo(dato)
        else:
            self.insertar_recursivo(self.raiz, dato)

    def insertar_recursivo(self, nodo_actual, dato):
        if dato < nodo_actual.dato: 
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(dato)
            else: 
                self.insertar_recursivo(nodo_actual.izquierdo,dato)
        else:
            if nodo_actual.derecho is None: 
                nodo_actual.derecho = Nodo(dato)
            else: 
                self.insertar_recursivo(nodo_actual.derecho,dato)