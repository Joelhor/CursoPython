def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))  # Converte a lista para um conjunto para remover duplicatas
    lista_sem_repeticao.sort()  # Ordena a lista resultante
    return lista_sem_repeticao

# Exemplos de uso:
lista1 = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista1))  # Saída: [1, 2, 3, 4]

lista2 = [1, 2, 3, 3, 3, 4]
print(remove_repetidos(lista2))  # Saída: [1, 2, 3, 4]

