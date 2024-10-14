#desenvolver um algoritmo para uma locadora de carros que
#deve solicitar ao usuário o carros que deseja alugar
#e mostyrar o valor do aluguel por dia.
#O algoritmo deve calcular o valor total do aluguel e exibir o resultado
#para o usuário.
#inicia com 3 opçoes de escoljha : 0-mostrar portifolio de carros, 1-alugar carro, 2-devolver o carro
#se escolher 0, mostra o portifolio de carros disponiveis com 8 opçoes de carros (ex: gol, uno, palio, celta, corsa, ka, hb20, onix) e o valor do aluguel por dia
#se escolher 1, solicita o codigo do carros e por quantos dias quer alugar
#calcula o valor total do aluguel e exibe o resultado para o usuario e pergunta se quer confirmar a locaçao
#se escolher 2, opçao de devolucao do carro
#mostra a lista de carros alugados
#solicita o codigo do carro que esta sendo devolvido
#calcula o valor total do aluguel e exibe o resultado para o usuario
#pergunta se quer confirmar a devolucao
#se escolher 3, sai do programa
#crie um dicionario com os carros e os valores
#crie uma lista para armazenar os carros alugados
#crie uma lista para armazenar os carros disponiveis


carros = {
    "gol": 50,
    "uno": 60,
    "palio": 55,
    "celta": 45,
    "corsa": 50,
    "ka": 55,
    "hb20": 65,
    "onix": 70
}

carros_alugados = []
carros_disponiveis = list(carros.keys())

while True:
    print("Escolha uma opção:")
    print("0 - Mostrar portfólio de carros")
    print("1 - Alugar carro")
    print("2 - Devolver carro")
    print("3 - Mostrar carros disponíveis")  # Nova opção adicionada
    print("4 - Sair do programa")  # Atualizado para 4

    # opcao = int(input("Opção:"))

    while True:
        try:
            opcao = int(input("Opção: "))
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    if opcao == 0:
        print("Portfólio de carros disponíveis:")
        for carro, valor in carros.items():
            print(f"{carro}: R${valor} por dia")

    elif opcao == 1:
        while True:   
            # Exibe o portfólio de carros disponíveis antes do usuário fazer uma escolha
            print("Portfólio de carros disponíveis:")
            for i, carro in enumerate(carros_disponiveis):
                print(f"{i} - {carro}")

            # Solicita ao usuário que insira o código do carro que deseja alugar
            codigo = int(input("Digite o código do carro que deseja alugar: "))
            
            # Verifica se o código inserido é válido. Se não for, dá ao usuário a opção de voltar ao menu inicial ou ver o portfólio de carros novamente
            if codigo < 0 or codigo >= len(carros_disponiveis):
                print("Código inválido. Por favor, tente novamente.")
                print("\n1 - Ver portfólio de carros disponíveis novamente")
                print("2 - Voltar ao menu inicial")
                escolha = int(input("Digite a sua escolha: "))
                
                if escolha == 2:  
                    break  
                elif escolha == 1:
                    continue
                else:
                    print("Opção inválida. Por favor, tente novamente.")
                    continue

            # Se o código inserido for válido, prossegue para a parte que lida com o aluguel do carro
            dias = int(input("Digite a quantidade de dias que deseja alugar: "))

            carro_alugado = carros_disponiveis[codigo]
            valor_total = carros[carro_alugado] * dias

            print(f"Valor total do aluguel: R${valor_total}")

            confirmacao = input("Deseja confirmar a locação? (S/N): ")
            if confirmacao.lower() == "s":
                carros_alugados.append(carro_alugado)
                carros_disponiveis.remove(carro_alugado)
                print("Locação confirmada!")
            else:
                print("Locação cancelada!")
            break

    elif opcao == 2:

        # if not carros_alugados:
        #      print("Nenhum carro alugado no momento.")
        #      break 
            # Variável de controle para sair do loop do menu principal
        sair_menu_principal = False

        # Verifica se há carros alugados. Se não houver, exibe uma mensagem e sai do loop para voltar ao menu inicial
        if not carros_alugados:
            print("Nenhum carro alugado no momento.")
            sair_menu_principal = True  # Atualiza a variável de controle

        if not sair_menu_principal:  # Se a variável de controle for False, executa o loop
        
        
            while True:  
                print("Carros alugados:")
                for i, carro in enumerate(carros_alugados):
                    print(f"{i} - {carro}")

                codigo = int(input("Digite o código do carro que está sendo devolvido: "))
                if codigo < 0 or codigo >= len(carros_alugados):
                 print("Código inválido. Por favor, tente novamente.")
                 continue   

                dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))  # Adicione esta linha
                carro_devolvido = carros_alugados[codigo]
                valor_total = carros[carro_devolvido] * dias

                print(f"Valor total do aluguel: R${valor_total}")

                confirmacao = input("Deseja confirmar a devolução? (S/N): ")
                if confirmacao.lower() == "s":
                    carros_disponiveis.append(carro_devolvido)
                    carros_alugados.remove(carro_devolvido)
                    print("Devolução confirmada!")
                else:
                    print("Devolução cancelada!")
                break 
            # Se a variável de controle for True, sai do loop do menu principal
        if sair_menu_principal:
          continue    


    elif opcao == 3:  
        print("Carros disponíveis:")
        for i, carro in enumerate(carros_disponiveis):
            print(f"{i} - {carro}")

    elif opcao == 4: 
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



