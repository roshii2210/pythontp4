from data_structures import ArrayHeap
from abc import ABC, abstractmethod
from typing import Any, List
from array_heap_ext_abstract import ArrayHeapExtAbstract

class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):
    """Implementa una cola de prioridad mínima con un heap binario
    que extiende la clase ArrayHeap y cumple con los métodos adicionales de ArrayHeapExtAbstract.
    """

    def k_menores(self, k: Any) -> List[Any]:
        """Devuelve una lista formada por los elementos del heap
        cuyo valor de clave es inferior a k.

        Args:
            k (Any): valor de clave hasta donde se quieren encontrar entradas menores (inclusive).

        Returns:
            List[Any]: lista de entradas del heap cuyo valor de clave es menor que k.
            Debe ser una lista vacía en caso que no haya entradas que cumplan la condición.
        """
        return [item for item in self._data if item._key <= k]

    def eliminar(self, k: Any) -> None:
        """Elimina el elemento del heap cuyo valor de clave coincida con k.
        Reorganiza todo el heap de manera de mantener la condición.

        Args:
            k (Any): clave de la entrada que se quiere eliminar.
        """
        index = None
        for i, item in enumerate(self._data):
            if item._key == k:
                index = i
                break

        if index is not None:
            self._swap(index, len(self._data) - 1)
            self._data.pop()
            self._downheap(index)

    def interseccion(self, other: ArrayHeap) -> List[Any]:
        """Devuelve las entradas que están tanto en el Heap que recibe la llamada como en other.

        Args:
            other (ArrayHeap): otro heap. Considerar que puede estar vacío.

        Returns:
            List[Any]: lista formada por los elementos en común entre este heap y el pasado por parámetro.
        """
        return [item for item in self._data if item in other._data]