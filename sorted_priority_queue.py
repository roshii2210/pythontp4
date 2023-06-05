from abc import ABC, abstractmethod
from typing import Any, Tuple
from sorted_priority_queue_abstract import SortedPriorityQueueAbstract

class SortedPriorityQueue(SortedPriorityQueueAbstract):
    def __init__(self):
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def add(self, k: Any, v: Any) -> None:
        item = (k, v)
        i = len(self._data) - 1
        while i >= 0 and k < self._data[i][0]:
            i -= 1
        self._data.insert(i + 1, item)

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La estructura está vacía")
        return self._data[-1]

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La estructura está vacía")
        return self._data.pop()

    def __str__(self) -> str:
        return ', '.join(str(item) for item in self._data)