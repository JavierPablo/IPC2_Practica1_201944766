from typing import Generic, TypeVar


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
        pass