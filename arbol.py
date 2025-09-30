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
            print(nodo.dato, end=', ')
            self.preorder_rec(nodo.izq)
            self.preorder_rec(nodo.der)

    def inorder(self):
        self.inorder_rec(self.raiz)

    def inorder_rec(self, nodo):
        if nodo:
            self.inorder_rec(nodo.izq)
            print(nodo.dato, end=', ')
            self.inorder_rec(nodo.der)

    def postorder(self):
        self.postorder_rec(self.raiz)

    def postorder_rec(self, nodo):
        if nodo:
            self.postorder_rec(nodo.izq)
            self.postorder_rec(nodo.der)
            print(nodo.dato, end=', ')

    def buscar(self, dato):
        return self.buscar_rec(dato, self.raiz)

    def buscar_rec(self, dato, nodo):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        elif dato < nodo.dato:
            return self.buscar_rec(dato, nodo.izq)
        else:
            return self.buscar_rec(dato, nodo.der)
#test
arbol = ArbolB()
arbol.insertar(20)
arbol.insertar(15)
arbol.insertar(33)
arbol.insertar(10)
arbol.insertar(18)
arbol.insertar(5)
arbol.insertar(12)
arbol.insertar(17)
arbol.insertar(19)
arbol.insertar(25)
arbol.insertar(50)
arbol.insertar(21)
arbol.insertar(27)
arbol.insertar(40)
arbol.insertar(70)

print('Preorder: ')
arbol.preorder()
print('\nInorder: ')
arbol.inorder()
print('\nPostorder: ')
arbol.postorder()

print("\nBuscar 25:", arbol.buscar(25))  
print("Buscar 99:", arbol.buscar(99))    