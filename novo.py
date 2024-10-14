
import random

lista = [1, 2, "hello", [1, 2, 3]]

a = lista[2].upper()

print(a)  

lista1 = [1, 2, 3]
lista2 = [4, 5, 8]
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

lista6 = [1, 2, 3, 4, 5, 6, 7]
lista6.append(6)
print(lista6)
lista6.pop()
print(lista6)

lista6.pop(2)
print(lista6)
#crie a lista antes de ser chamada  
#crie uma lista com 5 elementos e faça a inserção de um novo elemento   
#remova o último elemento da lista
print (f'-----------------1')
novalista = [1, 2, 3, 4, 5]     
novalista.append(7) 
print(novalista)
print(novalista.pop())
print (f'-----------------2')
#crie uma lista com 5 elementos e faça a inserção de um novo elemento
#remova o último elemento da lista
#remova um elemento pelo índice
lista7 = [1, 2, 3, 4, 5]
lista7.append(6)
print(lista7)
print(lista7.pop())
#remova o segundo elemento da lista
lista7.pop(1)
print(lista7)
print (f'-----------------3')
#crie uma lista com 5 elementos e faça a inserção de um novo elemento
#remova o último elemento da lista
#remova um elemento pelo índice
lista8 = [1, 2, 3, 4, 5]
lista8.append(6)
print(lista8)
print(lista8.pop())
lista8.pop(1)

print(lista8) 

print (f'-----------------5')
lista9 = [1, 2, 3, 4, 5]
#divida a lista em duas
lista10 = lista9[:3]
lista11 = lista9[3:]
print(lista10)
print(lista11)

#divida a lista em duas
#coloque o numero 3 da lista 10 na lista 11
lista12 = [1, 2, 3, 4, 5]
lista13 = lista12[:3]
lista14 = lista12[3:]
lista14.append(lista13.pop(2))
print(lista13)
print(lista14)
print (f'-----------------6')


