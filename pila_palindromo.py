
class Pila():
    def __init__(self):
        self.elements = []
        self.elements2 = []

    def comparar(self, valor):
        for x in valor:
            self.elements.append(x)

        for x in range(len(self.elements)):
            self.elements2.append(self.elements[-1])
            self.elements.pop()

        word = "".join(self.elements2)

        if valor == word:
            print(f"\"{valor}\" es palindromo")
        else:
            print(f"\"{valor}\" no es palindromo")


palabra = input("Palabra: ")
p = Pila()
p.comparar(palabra)


