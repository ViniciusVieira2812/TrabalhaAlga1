while True:
    print("Digite 1 para fazer o pedido")
    print("Digite 2 para fazer a avaliação do atendimento")

    while True:
        try:
            operacao = int(input("Qual operação deseja realizar? "))
            if 1 <= operacao <= 2:
                break
            else:
                print("Número fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    itens_pedido = []
    valortotal = 0
    while operacao == 1:
        print("1 - Casquinha: 6,00 R$")
        print("2 - Cascão: 12,00 R$")
        print("3 - Milk shake pequeno (330ml): 15,00 R$")
        print("4 - Milk shake médio (440ml): 20,00 R$")
        print("5 - Milk shake grande (550ml): 25,00 R$")
        print("6 - Finalizar o pedido")
        pedido = int(input("Qual o seu pedido?: "))
        if pedido == 1:
            print("1 - Leite Condensado")
            print("2 - Chocolate")
            print("3 - Mista")
            saborC = int(input("Qual sabor desejado?"))
            if saborC == 1:
                itens_pedido.append("1 Casquinha de Leite Condensado")
                valortotal = valortotal + 6
            elif saborC == 2:
                itens_pedido.append("1 Casquinha de Chocolate")
                valortotal = valortotal + 6
            elif saborC == 3:
                itens_pedido.append("1 Casquinha Mista")
                valortotal = valortotal + 6
            else:
                print("Sabor inválido")
        elif pedido == 2:
            print("1 - Leite Condensado")
            print("2 - Chocolate")
            print("3 - Mista")
            saborCC = int(input("Qual sabor desejado?"))
            if saborCC == 1:
              itens_pedido.append("1 Cascão de Leite Condensado")
              valortotal = valortotal + 12
            elif saborCC == 2:
              itens_pedido.append("1 Cascão de Chocolate")
              valortotal = valortotal + 12
            elif saborCC == 3:
              itens_pedido.append("1 Cascão Misto")
              valortotal = valortotal + 12
            else:
              print("Sabor invalido")
        elif pedido == 3:
            print("1 - Leite Condensado")
            print("2 - Chocolate")
            print("3 - Morango")
            print("4 - Abacaxi")
            print("5 - Maracuja")
            print("6 - Ovomaltine")
            saborMP = int(input("Qual sabor desejado?"))
            if saborMP == 1:
              itens_pedido.append("1 Milk Shake pequeno de Leite Condensado")
              valortotal = valortotal + 15
            elif saborMP == 2:
              itens_pedido.append("1 Milk Shake pequeno de Chocolate")
              valortotal = valortotal + 15
            elif saborMP == 3:
              itens_pedido.append("1 Milk Shake pequeno de Morango")
              valortotal = valortotal + 15
            elif saborMP == 4:
              itens_pedido.append("1 Milk Shake pequeno de Abacaxi")
              valortotal = valortotal + 15
            elif saborMP == 5:
              itens_pedido.append("1 Milk Shake pequeno de Maracuja")
              valortotal = valortotal + 15
            elif saborMP == 6:
              itens_pedido.append("1 Milk Shake pequeno Ovomaltine")
              valortotal = valortotal + 15
            else:
              print("Sabor invalido")
        elif pedido == 4:
            print("1 - Leite Condensado")
            print("2 - Chocolate")
            print("3 - Morango")
            print("4 - Abacaxi")
            print("5 - Maracuja")
            print("6 - Ovomaltine")
            saborMP = int(input("Qual sabor desejado?"))
            if saborMP == 1:
              itens_pedido.append("1 Milk Shake medio de Leite Condensado")
              valortotal = valortotal + 20
            elif saborMP == 2:
              itens_pedido.append("1 Milk Shake medio de Chocolate")
              valortotal = valortotal + 20
            elif saborMP == 3:
              itens_pedido.append("1 Milk Shake medio de Morango")
              valortotal = valortotal + 20
            elif saborMP == 4:
              itens_pedido.append("1 Milk Shake medio de Abacaxi")
              alortotal = valortotal + 20
            elif saborMP == 5:
              itens_pedido.append("1 Milk Shake medio de Maracuja")
              valortotal = valortotal + 20
            elif saborMP == 6:
              itens_pedido.append("1 Milk Shake medio Ovomaltine")
              valortotal = valortotal + 20
            else:
              print("Sabor invalido")
        elif pedido == 5:
            print("1 - Leite Condensado")
            print("2 - Chocolate")
            print("3 - Morango")
            print("4 - Abacaxi")
            print("5 - Maracuja")
            print("6 - Ovomaltine")
            saborMP = int(input("Qual sabor desejado?"))
            if saborMP == 1:
              itens_pedido.append("1 Milk Shake grande de Leite Condensado")
              valortotal = valortotal + 25
            elif saborMP == 2:
              itens_pedido.append("1 Milk Shake grande de Chocolate")
              valortotal = valortotal + 25
            elif saborMP == 3:
              itens_pedido.append("1 Milk Shake grande de Morango")
              valortotal = valortotal + 25
            elif saborMP == 4:
              itens_pedido.append("1 Milk Shake grande de Abacaxi")
              valortotal = valortotal + 25
            elif saborMP == 5:
              itens_pedido.append("1 Milk Shake grande de Maracuja")
              valortotal = valortotal + 25
            elif saborMP == 6:
              itens_pedido.append("1 Milk Shake grande Ovomaltine")
              valortotal = valortotal + 25
            else:
              print("Sabor invalido")
        elif pedido == 6:
            print("Seu pedido é:")
            for item in itens_pedido:
                print(item)
            print(f"O valor total do pedido é {valortotal} R$")
            break
        else:
            print("Valor inválido")
    if operacao == 2:
      notaF = int(input("Qual a sua nota para o atendimento dos funcionarios de 1 a 5? "))
      notaT = int(input("Qual a sua nota para o tempo de espera do pedido de 1 a 5? "))
      notaP = int(input("Qual a sua nota para o produto de 1 a 5? "))
      print("Agradeçemos a avaliação")
    
    continua = input("Deseja fazer outra operação? (S/N): ")
    if continua.upper() != "S":
        break