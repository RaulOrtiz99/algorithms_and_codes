class Nodo: 

    def __init__(self,dato, izquierdo = None, derecho = None):
        self.dato = dato
        self.izquierdo = izquierdo
        self.derecho = derecho

    def es_hoja(self):
        return self.izquierdo is None and self.derecho is None
    