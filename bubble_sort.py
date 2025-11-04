from functions import swap

# Compara pares de elementos adjacentes e troca se não estiverem em ordem.
# Complexidade O(n^2)
# Aceitável em pequenos conjuntos de dados
def bubble_sort(array):
  n = len(array)
  for i in range(n-1):
    for j in range(n-i-1):
      if(array[j] > array[j+1]):
        swap(array, j, j+1)

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]

bubble_sort(array)
print(array)    