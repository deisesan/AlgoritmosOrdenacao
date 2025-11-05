from functions import swap

# Pesquisa e mantém o valor do mínimo em cada interação, no final é feito a troca das variáveis.
# Complexidade O(n^2) - Tempo quadrático
# Aceitável em pequenos conjuntos de dados
def selection_sort(array):
	n = len(array)
	for i in range(n - 1):
		min = i
		for j in range(i+1, n):
			if(array[min] > array[j]):
				min = j
		swap(array, min, i)

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
selection_sort(array)
print(array)