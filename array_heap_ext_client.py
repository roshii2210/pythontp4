from array_heap_ext import ArrayHeapExt



heap = ArrayHeapExt()


heap.add(2, 'B')
heap.add(5, 'A')
heap.add(4, 'C')
heap.add(15, 'K')
heap.add(9, 'F')
heap.add(7, 'Q')
heap.add(6, 'Z')
heap.add(16, 'X')
heap.add(25, 'J')
heap.add(14, 'E')
heap.add(12, 'H')
heap.add(11, 'S')
heap.add(8, 'W')
heap.add(20, 'B')
heap.add(10, 'L')


print(heap)


print(len(heap))


print(heap.is_empty())


print(heap.min()) 


print(heap.remove_min())
print(heap) 


k_menores = heap.k_menores(7)
print(k_menores)  


heap.eliminar(6)
print(heap)  


other_heap = ArrayHeapExt()
other_heap.add(5, 'A')
other_heap.add(9, 'F')
other_heap.add(11, 'S')
other_heap.add(13, 'D')

interseccion = heap.interseccion(other_heap)
print(interseccion)
