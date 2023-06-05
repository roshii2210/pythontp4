from sorted_priority_queue import SortedPriorityQueue


queue = SortedPriorityQueue()


print("¿La cola está vacía?", queue.is_empty())


queue.add(3, "Tres")
queue.add(1, "Uno")
queue.add(4, "Cuatro")
queue.add(2, "Dos")
queue.add(5, "Cinco")


print("Cola:", queue)


print("Tamaño de la cola:", len(queue))


print("Elemento con la menor prioridad:", queue.min())


removed_item = queue.remove_min()
print("Elemento eliminado:", removed_item)


print("Cola después de eliminar el elemento:", queue)


print("Tamaño de la cola después de eliminar:", len(queue))


queue.add(0, "Cero")
queue.add(6, "Seis")


print("Cola final:", queue)
