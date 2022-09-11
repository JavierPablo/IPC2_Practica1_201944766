from typing import Callable, Generic, TypeVar


T = TypeVar("T")
class Nodo(Generic[T]):
    def __init__(self,elemento:T) -> None:
        self.siguiente:Nodo[T] = None
        self.elemeento:T = elemento

R = TypeVar("R")
class Cola(Generic[R]):
    def __init__(self) -> None:
        self.inicio:Nodo[R] = None
        self.final:Nodo[R] = None

    def insertar(self,elemento:R) -> None:
        if self.inicio == None:
            self.inicio = Nodo(elemento)
            self.final = self.inicio
            return
        self.final.siguiente = Nodo(elemento)
        self.final = self.final.siguiente
        
    def desencolar(self) -> R:
        temporal = self.inicio
        if temporal is None: return None
        if temporal is self.final: 
            self.inicio = None
            self.final = None
        else:
            self.inicio = temporal.siguiente
        return temporal.elemeento
    
    def __str__(self) -> str:
        strRepr = ""
        temporal = self.inicio
        while temporal is not None: 
            strRepr += str(temporal.elemeento)
            temporal = temporal.siguiente
            if temporal is not None: strRepr +=" -> "
        return strRepr

    def realizarConCadaElemento(self,consumidor:Callable[[R],None]) -> None:
        temporal = self.inicio
        while temporal is not None: 
            consumidor(temporal.elemeento)
            temporal = temporal.siguiente
    
    def obtenerPrimerElemento(self,predicado:Callable[[R],bool]) -> R:
        temporal = self.inicio
        while temporal is not None: 
            if predicado(temporal.elemeento): return temporal.elemeento
            temporal = temporal.siguiente
        return None
    
    def  __getitem__(self,index:int):
        if index < 0 :return None
        actual = self.inicio
        if  actual is None: return None
        for x in range(index):
            actual = actual.siguiente
            if  actual is None: return None
        return actual.elemeento