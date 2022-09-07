from typing import Generic, TypeVar


T = TypeVar("T")
class Nodo(Generic[T]):
    def __init__(self,elemento:T) -> None:
        self.siguiente:Nodo[T] = None
        self.elemeento:T = elemento
    