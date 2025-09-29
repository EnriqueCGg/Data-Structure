inventario = {}
productos_agotados = set()
productos_vendidos = {}

def agregar_inventario(nombre, cantidad):
    inventario[nombre] = cantidad
    productos_vendidos[nombre] = 0

def comprobar_inventario(nombre):
    if nombre in inventario:
        #print("Existe")
        return True

def stock(nombre):
    if comprobar_inventario(nombre):
        if inventario[nombre] > 0:
            print('Suficiente inventario')
            return True
        
def venta(nombre, cantidad):
    if comprobar_inventario(nombre):
        if inventario[nombre] >= cantidad:
            inventario[nombre] -= cantidad
            productos_vendidos[nombre] += cantidad
            print('Venta Exitosa')
            if inventario[nombre] == 0:
                productos_agotados.add(nombre)
        else:
            print('La cantidad de productos supera nuestro inventario')
            
def re_stock(nombre, cantidad):
    inventario[nombre] += cantidad
    if nombre in productos_agotados:
        productos_agotados.discard(nombre)

#Test
agregar_inventario('laptop', 10)
agregar_inventario('mouse', 20)
agregar_inventario('keyboard', 30)
print(f'inventario: {inventario}')
print(f'productos_vendidos: {productos_vendidos}')
comprobar_inventario('keyboard')
stock('laptop')

venta('mouse', 15)
venta('mouse', 5)
venta('laptop', 10)
print(f'inventario: {inventario}')
print(f'productos_vendidos: {productos_vendidos}')
print(f'productos_agotados: {productos_agotados}')

re_stock('laptop', 20)
re_stock('mouse', 35)
print(f'inventario: {inventario}')
print(f'productos_vendidos: {productos_vendidos}')
print(f'productos_agotados: {productos_agotados}')


# Simulación de interfaz
'''
while True:
    selection = int(input('Choose a option: '))
    
    if selection == 1:
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        agregar_inventario(nombre, cantidad)
        print(f'inventario: {inventario}')
    if selection == 2: 
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        venta(nombre, cantidad)
        print(f'productos_vendidos: {productos_vendidos}')
    if selection == 3: 
        print(inventario)
    if selection == 0:
        break
'''