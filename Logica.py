from dataclasses import dataclass

from Cola import Cola


@dataclass
class Ingrediente:
    nombre:str
    tiempoDeCoccion:int

@dataclass
class Cliente:
    nombre:str

class OrdenDeHotDog:
    INGREDIENTES:Cola[Ingrediente] = None
    def __init__(self,cliente:Cliente,cantidadDeHotDogs:int,ingredientes:Cola[int],tiempoExtra:int) -> None:
        self.cliente=cliente
        self.cantidadDeHotDogs=cantidadDeHotDogs
        self.ingredientes=ingredientes
        self.tiempoExtra=tiempoExtra
        self.tiempoPropio = self.__calcularTiempoPropio()
        OrdenDeHotDog.INGREDIENTES.realizarConCadaElemento(lambda a:print(a))
        
    def __calcularTiempoPropio(self):
        def consumidorContadorDeTiempo(num:int):
            self.tiempoPropio+=OrdenDeHotDog.INGREDIENTES[num].tiempoDeCoccion
        self.ingredientes.realizarConCadaElemento(consumidorContadorDeTiempo)
        
    def inicializarINGREDIENTES():
        OrdenDeHotDog.INGREDIENTES = Cola()
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Chorizo",3))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Salami",1.5))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Salchicha",2))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Longaniza",4))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Costilla",6))
if OrdenDeHotDog.INGREDIENTES is None: 
    OrdenDeHotDog.inicializarINGREDIENTES()



class AdministradorDeOrden(Cola[OrdenDeHotDog]):
    def __init__(self) -> None:
        super().__init__()
    def realizarOrden(self,cliente:Cliente, ingredientes:Cola[int], cantidadDeHotdogs:int)-> None:
        pass
    def entregarOrden(self)-> None:
        pass


