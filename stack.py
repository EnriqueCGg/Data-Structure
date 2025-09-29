pila = [1,2,3,4]

class Pila():
    def __init__(self):
        self.elements = []

    def isempty(self):
        if len(self.elements) == 0:
            print("Pila vacia")
            return True

    def apilar(self, valor):
        self.elements.append(valor)

    def desapilar(self):
        if not self.isempty():
            return self.elements.pop()
        return None
    
    def mirar(self):
        if not self.isempty():
            print(f"Mirar: {self.elements[-1]}")

    def size(self):
        print(f"Size: {len(self.elements)}")
        return len(self.elements)
    
p = Pila()
p.apilar(2)
p.apilar(3)
p.apilar(4)

p.size()
p.mirar()

p.desapilar()
p.mirar()
p.size()
p.isempty()