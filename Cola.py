from typing import Generic, TypeVar


T = TypeVar("T")
class Nodo(Generic[T]):
    def __init__(self) -> None:
        super().__init__()