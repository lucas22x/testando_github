# aula extra dicionarios e metodos



valores = list(range(10))
#opçao 1    
maiores_que_5_1opçao = []  #resultado
for valor in valores: #para cada elemento em valores
     if valor > 5: #se condiçao
         maiores_que_5_1opçao.append(valor + 10) #adiciona o valor a lista
     


#opçao 2
maiores_que_5_2opçao = [valor +10   #resultado
                 for valor in valores  #para cada elemento em valores
                   if valor > 5] #se condiçao

print(valores)
print(maiores_que_5_1opçao)
print(maiores_que_5_2opçao)


