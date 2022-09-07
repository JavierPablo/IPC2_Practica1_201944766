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
    def insertar(self,element) -> R:
        pass
    def desencolar(self) -> R:
        pass