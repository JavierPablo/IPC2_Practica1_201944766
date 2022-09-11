
import itertools
from msilib.schema import AppId
from Cola import Cola
from Logica import Cliente, InterfazDePrograma


MENU = """
=============================================
|                                           |
| 1. realizar nueva orden de hot dogs       |
| 2. despachar orden de hot dogs            |
|                                           |
|                       para salir \"e\"      |
=============================================

"""
API = InterfazDePrograma()
INGREDIENTES_DE_HOTDOG = Cola()
secuencia = itertools.count(start=1)
API.getIngredientesDeHotDog().realizarConCadaElemento(lambda e:INGREDIENTES_DE_HOTDOG.insertar(f"{next(secuencia)} -> {e.nombre}"))
MAXIMA_ELECCION_INGREDIENTE:int = next(secuencia)-1
eleccion = ""
while eleccion != "e":
    print(MENU)
    eleccion = input("Ingrese un numero = ")
    if eleccion == "1":
        nombre = input("Ingrese nombre del cliente = ")
        cantidad = input("Ingrese la cantidad de hot dogs que desea = ")
        while not cantidad.isdigit():
            cantidad = input("Ingrese una cantidad de hot dogs valida = ")
        ingredientes = Cola[int]()
        print("--------------------------------------------------------------")
        print("Seleccione los ingredientes que desea, pulse \"m\" para salir")
        INGREDIENTES_DE_HOTDOG.realizarConCadaElemento(lambda e:print(e))
        ing = ""
        while ing != "m":
            ing = input("Numero de ingrediente = ")
            if ing.isdigit():
                data = int(ing)
                if not data <= 0 and not data > MAXIMA_ELECCION_INGREDIENTE:
                    if ingredientes.obtenerPrimerElemento(lambda a:a == data-1) == None:
                        ingredientes.insertar(data-1)
                        print("insertado ",data)
                    else: print("Ingrediente repetido")
                else: print("Fuera de rango")

        if ingredientes.inicio == None : print("No ingreso ningun alimento, por lo tanto no se ha agregado la orden")
        else: API.realizarOrden(Cliente(nombre),ingredientes,int(cantidad))
    elif eleccion == "2":
        print("Sacando orden")
        API.entregarOrden()
