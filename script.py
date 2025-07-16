restaurantes_cadastrados = {}

def cadastrar_restaurante(nome, categoria):
    restaurantes_cadastrados[nome] = {
        "categoria": categoria,
        "cardapio": []
    }
    print(f"{nome} cadastrado com sucesso!")

def ver_restaurantes_cadastrados():
    for i in restaurantes_cadastrados.keys():
        print(i)

def adicionar_item_ao_cardapio(nome_restaurante, item, preco):
    item = {item: preco}
    restaurantes_cadastrados[nome_restaurante]["cardapio"].append(item)

def consultar_cardapio_restaurante(nome_restaurante):
    for i in restaurantes_cadastrados[nome]["cardapio"]:
        print(i.keys()) #continuar

while (True):
    print("1 - Cadastrar restaurante")
    print("2 - Ver restaurantes cadastrados")
    print("3 - Adicionar item ao cardápio")
    print("4 - Consultar cardápio do restaurante")
    print("5 - Função 5")
    print("6 - Função 6")
    print("7 - Função 7")
    print("8 - Função 8")
    print("9 - Função 9")
    print("10 - Função 10")
    print("11 - Sair")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        nome = str(input("Informe o nome do restaurante: "))
        if nome in restaurantes_cadastrados.keys():
            print("Já existe um restaurante com esse nome!")
            print("Não foi possível cadastrar seu restaurante!")
            continue
        categoria = str(input("Informe a categoria do restaurante: "))
        if nome != "" and categoria != "":
            cadastrar_restaurante(nome, categoria)
        else:
            print("Escreva um nome e/ou categoria válida para seu restaurante!")
        continue
    elif opcao == 2:
        ver_restaurantes_cadastrados()
        continue
    elif opcao == 3:
        nome_restaurante = str(input("Informe o nome do restaurante a adicionar o item: "))
        if nome_restaurante not in restaurantes_cadastrados.keys():
            print("Esse restaurante não existe!")
            continue
        else:
            nome_item = str(input("Informe o nome do item o qual você quer adicionar ao seu restaurante: "))
            preco_item = float(input("Informe o valor do item que você quer inserir no seu restaurante: "))
            adicionar_item_ao_cardapio(nome_restaurante, nome_item, preco_item)
        continue
    elif opcao == 4:
        restaurante_consultado = str(input("Informe o nome do restaurante a ser consultado: "))
        consultar_cardapio_restaurante(restaurante_consultado)
        continue
    elif opcao == 5:
        #Opção 5
        continue
    elif opcao == 6:
        #Opção 6
        continue
    elif opcao == 7:
        #Opção 7
        continue
    elif opcao == 8:
        #Opção 8
        continue
    elif opcao == 9:
        #Opção 9
        continue
    elif opcao == 10:
        #Opção 10
        continue
    elif opcao == 11:
        print("Programa finalizado com sucesso!")
        break
    else:
        print("Informe uma opção válida entre 1-11!")

