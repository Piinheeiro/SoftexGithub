inventario = {}

while True :
    print("O QUE VOCE DESEJA FAZER? ")
    print("[1] ADICIONAR ITEM \n[2] REMOVER ITEM \n[3] LISTAR INVENTÁRIO \n[4] SAIR ")
    opcao = input ("Digite aqui: ")

    if opcao == "1":
        nome = input ("Nome do item: ")
        quantidade = float (input ("Quantidade: "))
        inventario[nome] = quantidade
        print ("Item adicionado!")
    elif opcao == "2":
        nome = input ("Nome do item para remover: ")
        if nome in inventario:
            del inventario[nome]
            print ("Item removido do estoque!")
        else:
            print ("Item não encontrado.")
    elif opcao == "3":
        print ("seu inventário possui os seguintes itens: ", inventario)
    elif opcao == "4":
        print ("Saindo.")
        
    else:
        print ("Opção inválida. Tente novamente.")