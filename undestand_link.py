class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertar(self, dato):
        new_node = Node(dato)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node 
        self.head = new_node
        

    def insertar_final(self, dato):  # Inserta al final
        new_node = Node(dato)
        if not self.head:   # lista vacía
            self.head = new_node
            return
        actual = self.head
        while actual.next:   # llegar al último
            actual = actual.next
        actual.next = new_node
        new_node.prev = actual

    def mostrar(self): #Muestra la lista
        actual = self.head
        while actual:
            print(actual.data, end=', ')
            actual = actual.next
        print()
    
    def buscar(self, target):
        actual = self.head
        while actual:
            if target == actual.data:
                print('Found!')
                return
            actual = actual.next
        print('Not found')
        
    def borrar(self, target):
        actual = self.head
        while actual and actual.data != target:
            actual = actual.next
        if not actual:  # No encontrado
            return
        # caso medio/final
        if actual.prev:
            actual.prev.next = actual.next
        else:
            # caso: borrar head
            self.head = actual.next
            if self.head:
                self.head.prev = None  
        # caso medio/final
        if actual.next:
            actual.next.prev = actual.prev


dato = LinkedList()

dato.insertar(3)
dato.insertar_final(5)
dato.insertar(7)
dato.insertar_final(9)

dato.mostrar()

dato.buscar(2)
dato.buscar(7)

dato.borrar(3)
dato.mostrar()