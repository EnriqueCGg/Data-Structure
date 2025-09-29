#Linked list and arrays are similar since they both store collections of data
#The Arrays features all follow from its  strategy of allocating the memory for all its elements in one block of memory
#Linked list use an entirely different strategy: linked lists allocate memory for each element separately and only when necessary

#[dato1|->] [dato2|->] [dato3|->etc]

#Las listas por otro lado son [dato1|dato2|dato3|etc]

#Las listLinks son una lista vacia conforme se agregan elementos y lo mismo cuando se remueven osea

#Listas normales list[4] esta lista tenga dos o menos tiene 4 espacios, mientras que las linked list si tiene 1 solo tiene 1 y si tiene menos cambia su tamaño en la memoria
#Por lo que son mejores y más versatiles que los arrays que tienes que definir un valor

#
class Nodo:
    def __init__(self,data):
        self.data = data 
        self.next= None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head=None 

    def insertar(self,dato): #Inserta dato
        nuevo = Nodo(dato)
        nuevo.next  = self.head
        if self.head:
            self.head.prev = nuevo
        self.head = nuevo

    def mostrar(self): #Muestra la lista
        actual  = self.head
        while actual:
            print(actual.data, end=", ")
            actual = actual.next
        print()

    def buscar(self, valor): #Muestra el valor a buscar
        actual = self.head
        while actual:
            if actual.data == valor:
                print("Encontrado")
                return 
            actual = actual.next
        print("No se encontro el valor") 

    def borrar(self,valor):
        actual = self.head
        if actual.data == valor:
            self.head = actual.next
            return
        anterior = None
        while actual and actual.data != valor:
            actual = actual.next
        if actual.prev: actual.prev.next = actual.next
        if actual.next: actual.next.prev = actual.prev

    def insertarFinal(self,valor):
        actual  = self.head
        while actual.next:
            actual = actual.next
        actual.next = Nodo(valor)


        

l = LinkedList()
l.insertar(12)
l.insertar(14)
l.insertar(10)
l.mostrar()
l.buscar(int(input("Buscar: ")))
l.borrar(int(input("Borrar: ")))
l.mostrar()
l.insertarFinal(5)
l.mostrar()