import os
from Menu import Menu
from ManejadorSabores import manejadorSabores
from ManejadorHelados import manejadorHelados

if __name__ == '__main__':
    mH = manejadorHelados()
    mS = manejadorSabores()
    mS.carga()
    bandera = False
    os.system('cls')
    menu = Menu()
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, mS, mH)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')