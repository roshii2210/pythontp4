from data_structures import ArrayHeap
from abc import ABC, abstractmethod
from typing import Any, List


class ArrayHeapExtAbstract(ABC):

    """Conjunto de métodos adicionales a ArrayHeapExtAbtract"""
    @abstractmethod
    def k_menores(self, k: Any) -> List[Any]:
        """Devuelve una lista formada por los elementos del heap
        cuyo valor de clave es inferior a k.
        Para los datos de entrada del ejercicio 6, si k = 7 entonces este
        método debería retornar entradas con clave: 2, 4, 5, 6, y 7
        (no necesariamente en ese orden).

        Args:
            k (Any): valor de clave hasta donde se quieren encontrar entradas menores (inclusive).

        Returns:
            List[Any]: lista de entradas del heap cuyo valor de clave es menor que k.
            Debe ser una lista vacía en caso que no haya entradas que cumplan la condición
        """
        pass

    @abstractmethod
    def eliminar(self, k: Any) -> None:
        """Elimina el elemento del heap cuyo valor de clave coincida con k.
        Reorganiza todo el heap de manera de mantener la condición.

        Args:
            k (Any): clave de la entrada que se quiere eliminar.
        """
        pass

    @abstractmethod
    def interseccion(self, other: ArrayHeap) -> List[Any]:
        """Devuelve las entradas que están tanto en el Heap que recibe la llamada como en other.

        Args:
            other (ArrayHeap): se trata de otro heap. Considerar que puede estar vacío.

        Returns:
            List[Any]: es lista python formada por los elementos en común entre este heap y el pasado por parámetro.
        """
        pass
