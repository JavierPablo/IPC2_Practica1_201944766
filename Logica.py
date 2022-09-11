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
        self.tiempoPropio = 0
        self.__calcularTiempoPropio()
        
    def __incrementarTiempoPropio(self,num:int):
        self.tiempoPropio+=num
    def __calcularTiempoPropio(self):
        self.ingredientes.realizarConCadaElemento(lambda a:self.__incrementarTiempoPropio(OrdenDeHotDog.INGREDIENTES[a].tiempoDeCoccion))
        self.tiempoPropio *=self.cantidadDeHotDogs
    def tiempoTotal(self)-> int:
        return self.tiempoExtra + self.tiempoPropio
    def __str__(self) -> str:
        return f"{self.cliente.nombre}, cantidad = {self.cantidadDeHotDogs}, tiempoTotal = {self.tiempoTotal()} || TE = {self.tiempoExtra} TP = {self.tiempoPropio}"

    def inicializarINGREDIENTES():
        OrdenDeHotDog.INGREDIENTES = Cola()
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Chorizo",3))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Salami",1.5))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Salchicha",2))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Longaniza",4))
        OrdenDeHotDog.INGREDIENTES.insertar(Ingrediente("Costilla",6))
if OrdenDeHotDog.INGREDIENTES is None: 
    OrdenDeHotDog.inicializarINGREDIENTES()



class AdministradorDeOrden:
    def __init__(self) -> None:
        self.cola = Cola[OrdenDeHotDog]()

    def agregarOrden(self,cliente:Cliente, ingredientes:Cola[int], cantidadDeHotdogs:int)-> None:
        tiempoExtra:int = 0
        def consumidor(orden:OrdenDeHotDog):
            nonlocal tiempoExtra
            tiempoExtra+=orden.tiempoPropio
        self.cola.realizarConCadaElemento(consumidor)
        nuevaOrden = OrdenDeHotDog(cliente,cantidadDeHotdogs,ingredientes,tiempoExtra)
        self.cola.insertar(nuevaOrden)

    def quitarOrden(self)-> None:
        self.cola.desencolar()
    def getGraphvizRepresentacion(self):
        print(self.cola)


class InterfazDePrograma():
    def __init__(self) -> None:
        self.administradorDeOrden = AdministradorDeOrden()
        self.direccionCarpetaDestino = "Graficas"
        self.graficasCounter = 0

    def realizarOrden(self,cliente:Cliente, ingredientes:Cola[int], cantidadDeHotdogs:int)-> None:
        self.administradorDeOrden.agregarOrden(cliente,ingredientes,cantidadDeHotdogs)
        self.__generarImagenDeGraphviz()

    def entregarOrden(self)-> None:
        self.administradorDeOrden.quitarOrden()
        self.__generarImagenDeGraphviz()
    
    def __generarImagenDeGraphviz(self):
        self.administradorDeOrden.getGraphvizRepresentacion()
        pass
    def getIngredientesDeHotDog(self) -> Cola[Ingrediente]:
        return OrdenDeHotDog.INGREDIENTES
