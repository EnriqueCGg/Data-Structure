
class Cliente():
    def __init__(self, numero, prioridad):
        self.numero = numero
        self.prioridad = prioridad
        
class Isempty():
    def __init__(self, lista):
        self.lista_prioridad = lista
    
    def isempty(self):
        if len(self.lista_prioridad) == 0:
            print("No clients")
            return True

class CallCenter():
    def __init__(self):
        self.alta = []
        self.media = []
        self.baja = []
        
    def isempty(self, lista_prioridad):
        if len(lista_prioridad) == 0:
            return True


    def insertar(self, numero, prioridad):
        cliente = Cliente(numero, prioridad)
        if cliente.prioridad.lower() == 'alta':
            self.alta.append(cliente.numero)
            return
        if cliente.prioridad.lower() == 'media':
            self.media.append(cliente.numero)
            return
        self.baja.append(cliente.numero)
        
    def buscar(self, numero):
        cliente = Cliente(numero,'')
        if cliente.numero in self.alta:
            print('Cliente en lista de espera en prioridad ALTA')
        elif cliente.numero in self.media:
            print('Cliente en lista de espera en prioridad MEDIA')
        elif cliente.numero in self.baja:
            print('Cliente en lista de espera en prioridad BAJA')
        else:
            print('No se encontro cliente\n')
            
    def atender(self):
        #prioridad_alta = Isempty(self.alta)
        if not self.isempty(self.alta):
            print(f"Atendiendo a: {self.alta[0]}")
            self.alta.pop(0)
            return
        elif not self.isempty(self.media):
            print(f"Atendiendo a: {self.media[0]}")
            self.media.pop(0)
            return
        elif not self.isempty(self.baja):
            print(f"Atendiendo a: {self.baja[0]}")
            self.baja.pop(0)
            return
        else:
            print(f"No hay clientes por atender")
            
    def mostrar(self):
        print('\nListas de llamadas pendientes:')
        if not self.isempty(self.alta):
            print('Prioridad ALTA: ')
            for x in range(len(self.alta)):
                print(self.alta[x], end=' - ')
            #print('\n')

        if not self.isempty(self.media):
            print('\nPrioridad MEDIA: ')
            for x in range(len(self.media)):
                print(self.media[x], end=' - ')
            #print('\n')
            
        if not self.isempty(self.baja):
            print('\nPrioridad BAJA: ')
            for x in range(len(self.baja)):
                print(self.baja[x], end=' - ')
            #print('\n')
                

call = CallCenter()
call.insertar('9991112233', 'ALTA')
call.insertar('9991104455', 'Media')
call.insertar('9991907722', 'bajA')
call.insertar('9881112233', 'alta')
call.insertar('9881104455', 'media')
call.insertar('9881907722', 'baja')

call.mostrar()


print('\n')

call.buscar('9991112233')
call.buscar('9881104455')
call.buscar('9991907722')
call.buscar('9771907722')


call.atender()
call.atender()
call.atender()

call.mostrar()
