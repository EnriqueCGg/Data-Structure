class NOdoAB():
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        

class ArbolB():
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato):
        nodo = NOdoAB(dato)
        if not self.raiz:
            self.raiz = nodo
        else:
            self.insertar_rec(dato, self.raiz)
    
    def insertar_rec(self, dato, nodo_actual):
        if dato < nodo_actual.dato:
            if not nodo_actual.izq:
                nodo_actual.izq = NOdoAB(dato)
            else:
                self.insertar_rec(dato, nodo_actual.izq)
        else:
            if not nodo_actual.der:
                nodo_actual.der = NOdoAB(dato)
            else:
                self.insertar_rec(dato, nodo_actual.der)
                
    def preorder(self):
        self.preorder_rec(self.raiz)
            
    def preorder_rec(self, nodo):
        if nodo:
            print(nodo.dato)
            self.preorder_rec(nodo.izq)
            self.preorder_rec(nodo.der)

            
                
arbol = ArbolB()
arbol.insertar(15)
arbol.insertar(7)
arbol.insertar(19)
arbol.insertar(3)
arbol.insertar(11)
arbol.preorder()