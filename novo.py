import random

lista = [1, 2, "hello", [1, 2, 3]]

a = lista[2].upper()

print(a)  

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

lista4 = [lista1, lista2, lista3]
lista5 = [lista1 + lista2 + lista3]

print(lista4)
print(lista5)

minha_lista = [1, 2, "Maria", "João", 3, [1, 2, 3]]
minha_lista.append(10)
print(minha_lista)
minha_lista.pop()

print(minha_lista)
#crie outra lista com 5 elementos e faça a inserção de um novo elemento
#remova o último elemento da lista
#remova um elemento pelo índice

lista6 = [1, 2, 3, 4, 5]
lista6.append(6)
print(lista6)
lista6.pop()
print(lista6)

lista6.pop(2)
print(lista6)
lista7 = random.sample(range(20), 5)
print(lista7)

