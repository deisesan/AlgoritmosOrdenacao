# Conta o número de ocorrências
# Faz uma acumulado doido - Soma de prefixo
## Quantidade de elementos que aparecem antes
# Dá um shift de 1 casa para a direita

# Definir k que é o maior valor
# Array de contagem vai ser de tamanho k
# Calcular a frequência dos elementos

# for int i = 0, i < A.lenght; i++ 
def counting_sort(array):
    max_val = max(array)
    arrayCount = [0] * (max_val + 1)
    arrayFinal = [0] * len(array)

    for i in range(len(array)):
        arrayCount[array[i]] += 1     
    
    # valores menores ou iguais ao numero de elementos selecionado do array 
    for i in range(1, len(arrayCount)):
        arrayCount[i] += arrayCount[i - 1]

    # Ordenar de trás pra frente em array para manter a estabilidade
    for i in range(len(array) - 1, -1, -1):
        arrayFinal[arrayCount[array[i]] - 1] = array[i]
        arrayCount[array[i]] -= 1

    for i in range(len(array)):
        array[i] = arrayFinal[i]


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
counting_sort(array)
print(array)    