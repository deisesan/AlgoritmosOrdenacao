from functions import swap

# Seleciona o elemento e coloca ele na posição que ele pertença, dando shift nos outros.
# Complexidade O(n^2) - Tempo quadrático
# Porém é O(n) no melhor caso
# Aceitável em pequenos conjuntos de dados
def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		temp = array[i]
		j = i - 1
		while j >= 0 and array[j] > temp:
		 	array[j+1] = array[j]
		 	j -= 1
		array[j+1] = temp

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
insertion_sort_1(array)
print(array)