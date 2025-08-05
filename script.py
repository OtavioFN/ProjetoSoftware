restaurantes_cadastrados = {}

def cadastrar_restaurante(nome, categoria):
    restaurantes_cadastrados[nome] = {
        "categoria": categoria,
        "cardapio": []
    }
    print(f"{nome} cadastrado com sucesso!\n")

def ver_restaurantes_cadastrados():
    if not restaurantes_cadastrados:
        print("Nenhum restaurante cadastrado.\n")
        return
    print("Restaurantes cadastrados:")
    for nome, info in restaurantes_cadastrados.items():
        print(f"- {nome} (Categoria: {info['categoria']})")
    print()

def adicionar_item_ao_cardapio(nome_restaurante, item, preco):
    item = {item: preco}
    restaurantes_cadastrados[nome_restaurante]["cardapio"].append(item)
    print(f"Item '{list(item.keys())[0]}' adicionado ao cardápio de {nome_restaurante}.\n")

def consultar_cardapio_restaurante(nome_restaurante):
    if nome_restaurante not in restaurantes_cadastrados:
        print("Restaurante não encontrado.\n")
        return
    cardapio = restaurantes_cadastrados[nome_restaurante]["cardapio"]
    if not cardapio:
        print("Cardápio vazio.\n")
        return
    print(f"Cardápio do restaurante {nome_restaurante}:")
    for item in cardapio:
        for nome_item, preco in item.items():
            print(f"- {nome_item}: R$ {preco:.2f}")
    print()

def remover_restaurante(nome):
    if nome in restaurantes_cadastrados:
        del restaurantes_cadastrados[nome]
        print(f"Restaurante '{nome}' removido com sucesso!\n")
    else:
        print("Restaurante não encontrado.\n")

def remover_item_do_cardapio(nome_restaurante, nome_item):
    cardapio = restaurantes_cadastrados[nome_restaurante]["cardapio"]
    for item in cardapio:
        if nome_item in item:
            cardapio.remove(item)
            print(f"Item '{nome_item}' removido com sucesso!\n")
            return
    print("Item não encontrado no cardápio.\n")

def ver_detalhes_restaurante(nome_restaurante):
    if nome_restaurante not in restaurantes_cadastrados:
        print("Restaurante não encontrado.\n")
        return

    dados = restaurantes_cadastrados[nome_restaurante]
    print(f"\nNome: {nome_restaurante}")
    print(f"Categoria: {dados['categoria']}")
    print("Cardápio:")
    if not dados["cardapio"]:
        print("  Nenhum item cadastrado.")
    else:
        for item in dados["cardapio"]:
            for nome_item, preco in item.items():
                print(f"  - {nome_item}: R$ {preco:.2f}")
    print()

def simular_entrega(nome_restaurante):
    if nome_restaurante not in restaurantes_cadastrados:
        print("Restaurante não encontrado.\n")
        return
    print(f"Pedido do restaurante '{nome_restaurante}' saiu para entrega.")
    print("Pedido entregue com sucesso!\n")

def realizar_pedido():
    if not restaurantes_cadastrados:
        print("Nenhum restaurante disponível para pedido.\n")
        return

    print("Restaurantes disponíveis:")
    for nome in restaurantes_cadastrados:
        print(f"- {nome}")
    nome_restaurante = input("Digite o nome do restaurante para fazer o pedido: ").strip()

    if nome_restaurante not in restaurantes_cadastrados:
        print("Restaurante não encontrado.\n")
        return

    cardapio = restaurantes_cadastrados[nome_restaurante]["cardapio"]
    if not cardapio:
        print("Este restaurante ainda não possui itens no cardápio.\n")
        return

    carrinho = []
    while True:
        print("\nCardápio:")
        for idx, item in enumerate(cardapio, start=1):
            for nome_item, preco in item.items():
                print(f"{idx}. {nome_item} - R$ {preco:.2f}")

        escolha = input("Digite o número do item para adicionar ao carrinho (ou 'fim' para finalizar): ").strip()
        if escolha.lower() == 'fim':
            break

        if not escolha.isdigit() or not (1 <= int(escolha) <= len(cardapio)):
            print("Opção inválida.\n")
            continue

        item_escolhido = cardapio[int(escolha) - 1]
        carrinho.append(item_escolhido)
        print("Item adicionado ao carrinho.")

    if not carrinho:
        print("Pedido cancelado (nenhum item no carrinho).\n")
        return

    print("\nResumo do pedido:")
    total = 0
    for item in carrinho:
        for nome_item, preco in item.items():
            print(f"- {nome_item} - R$ {preco:.2f}")
            total += preco
    print(f"Total a pagar: R$ {total:.2f}\n")
    print("Pedido finalizado com sucesso!\n")

# Menu principal
while True:
    print("======= Menu =======")
    print("1 - Cadastrar restaurante")
    print("2 - Ver restaurantes cadastrados")
    print("3 - Adicionar item ao cardápio")
    print("4 - Consultar cardápio do restaurante")
    print("5 - Remover restaurante")
    print("6 - Remover item do cardápio")
    print("7 - Ver detalhes do restaurante")
    print("8 - Filtrar restaurantes por categoria")
    print("9 - Simular entrega de pedido")
    print("10 - Fazer pedido (adicionar itens ao carrinho)")
    print("11 - Sair")
    
    try:
        opcao = int(input("Informe a opção desejada: "))
    except ValueError:
        print("Por favor, informe um número válido.\n")
        continue

    if opcao == 1:
        nome = input("Informe o nome do restaurante: ").strip()
        if nome in restaurantes_cadastrados:
            print("Já existe um restaurante com esse nome!\n")
            continue
        categoria = input("Informe a categoria do restaurante: ").strip()
        if nome and categoria:
            cadastrar_restaurante(nome, categoria)
        else:
            print("Escreva um nome e uma categoria válidos.\n")
        continue

    elif opcao == 2:
        ver_restaurantes_cadastrados()
        continue

    elif opcao == 3:
        nome_restaurante = input("Informe o nome do restaurante: ").strip()
        if nome_restaurante not in restaurantes_cadastrados:
            print("Esse restaurante não existe!\n")
            continue
        nome_item = input("Informe o nome do item: ").strip()
        try:
            preco_item = float(input("Informe o preço do item: "))
        except ValueError:
            print("Preço inválido. Use apenas números.\n")
            continue
        adicionar_item_ao_cardapio(nome_restaurante, nome_item, preco_item)
        continue

    elif opcao == 4:
        restaurante_consultado = input("Informe o nome do restaurante a ser consultado: ").strip()
        consultar_cardapio_restaurante(restaurante_consultado)
        continue

    elif opcao == 5:
        nome = input("Informe o nome do restaurante a remover: ").strip()
        remover_restaurante(nome)
        continue

    elif opcao == 6:
        nome_restaurante = input("Informe o nome do restaurante: ").strip()
        if nome_restaurante not in restaurantes_cadastrados:
            print("Restaurante não encontrado.\n")
            continue
        nome_item = input("Informe o nome do item a remover: ").strip()
        remover_item_do_cardapio(nome_restaurante, nome_item)
        continue

    elif opcao == 7:
        nome = input("Informe o nome do restaurante que deseja ver os detalhes: ").strip()
        ver_detalhes_restaurante(nome)
        continue

    elif opcao == 8:
        categoria = input("Informe a categoria para filtrar os restaurantes: ").strip()
        encontrados = False
        for nome, dados in restaurantes_cadastrados.items():
            if dados["categoria"].lower() == categoria.lower():
                print(f"- {nome}")
                encontrados = True
        if not encontrados:
            print("Nenhum restaurante encontrado para essa categoria.\n")
        print()
        continue

    elif opcao == 9:
        nome_restaurante = input("Informe o nome do restaurante para simular a entrega: ").strip()
        simular_entrega(nome_restaurante)
        continue

    elif opcao == 10:
        realizar_pedido()
        continue

    elif opcao == 11:
        print("Programa finalizado com sucesso!")
        break

    else:
        print("Informe uma opção válida entre 1 e 11.\n")
