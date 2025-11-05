# Utiliza uma árvore binária ordenada - heap
# max_heap: parent > child
# Tem uma tree aplica o build max heap e encontra uma max_heap
# Troca o max com o ultimo 
# Remove o ultimo por que já está "ordenado"
# Tem uma tree que aplica uma heapify e encontra o max_heap
# Custo da buil_max_heap é de O(n)
# E o curso do heapify é O(lg n) * (n-1) = teta(n lg n)]

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

def heap_sort(array):
    n = len(array)
    build_max_heap(array)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
heap_sort(array)
print(array)