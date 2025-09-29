class Nodo:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
        
class ListaCircularDoble:
    def __init__(self):
        self.head = None

    def insertar_frente(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            nuevo.prev = self.head
        else:
            ultimo = self.head.prev 
            nuevo.next = self.head  
            nuevo.prev = ultimo     
            self.head.prev = nuevo  
            ultimo.next = nuevo     
            self.head = nuevo       
            
    def insertar_final(self, dato):
        if not self.head:
            self.insertar_frente(dato)
            return
        nuevo = Nodo(dato)
        ultimo = self.head.prev
        nuevo.next = self.head
        nuevo.prev = ultimo
        ultimo.next = nuevo
        self.head.prev = nuevo

    def mostrar(self):
        if not self.head:
            print("La lista está vacía.")
            return
        
        actual = self.head
        print("Lista: ", end="")
        while True:
            print(actual.data, end=" <-> ")
            actual = actual.next
            if actual == self.head: 
                break
        print("(vuelve al inicio)")

    def buscar(self, valor):
        if not self.head:
            print(f"Valor '{valor}' no encontrado.")
            return False

        actual = self.head
        while True:
            if actual.data == valor:
                print(f"Valor '{valor}' ha sido encontrado.")
                return True
            actual = actual.next
            if actual == self.head:
                break
        
        print(f"Valor '{valor}' no se encontró en la lista.")
        return False

    def borrar(self, valor):
        if not self.head:
            print("No se puede borrar, la lista está vacía.")
            return
        actual = self.head
        encontrado = False
        
        # Busca el nodo a borrar
        while True:
            if actual.data == valor:
                encontrado = True
                break
            actual = actual.next
            if actual == self.head:
                break

        if not encontrado:
            print(f"No se puede borrar, el valor '{valor}' no existe.")
            return

        if self.head.next == self.head and self.head.data == valor:
            self.head = None
            print(f"Se borró el valor '{valor}', la lista ahora está vacía.")
            return
        
        if actual == self.head:
            self.head = self.head.next
        
        actual.prev.next = actual.next
        actual.next.prev = actual.prev
        print(f"Se borró el valor '{valor}' de la lista.")

# --- BLOQUE PRINCIPAL CORREGIDO ---
if __name__ == "__main__":
    
    l = ListaCircularDoble()
    # CORRECCIÓN: Se usa el nombre de método correcto "insertar_frente"
    l.insertar_frente(12)
    l.insertar_frente(14)
    l.insertar_frente(10) 

    print("--- Ejemplo Interactivo de Lista Circular ---")
    print("Se ha creado una lista inicial:")
    l.mostrar()

    try:
        valor_buscar = int(input("\nIntroduce un número para BUSCAR: "))
        l.buscar(valor_buscar)
    except ValueError:
        print("Error: Debes introducir un número entero.")

    try:
        valor_borrar = int(input("\nIntroduce un número para BORRAR: "))
        l.borrar(valor_borrar)
        l.mostrar()
    except ValueError:
        print("Error: Debes introducir un número entero.")

    try:
        valor_final = int(input("\nIntroduce un número para INSERTAR AL FINAL: "))
        # CORRECCIÓN: Se usa el nombre de método correcto "insertar_final"
        l.insertar_final(valor_final)
        l.mostrar()
    except ValueError:
        print("Error: Debes introducir un número entero.")
        
    print("\n--- Fin del programa ---")