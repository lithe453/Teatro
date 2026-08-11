continuar = "n"

while continuar == "n":
    print("--------------------")
    print("====== TEATRO ======")
    print("---------------------")

    print("1- mostrar teatro")
    print("2- reserva lugar")
    print("3- cancelar reserva")
    print("4- fechar o programa")

    op = int(input("escolha uma opcao: "))

    match op:
        case 1:
            mostrar_teatro()

        case 2:
            mostrar_teatro()

            lugar_escolhida = int(input("escolha um lugar de 0 a 9: "))
            fila_escolhida = int(input("escolha uma fila de 0 a 9: "))

            teatro[fila_escolhida][lugar_escolhida] = 1

        case 3:
            mostrar_teatro()

            lugar_escolhida = int(input("escolha um lugar de 0 a 9: "))
            fila_escolhida = int(input("escolha uma fila de 0 a 9: "))

            teatro[fila_escolhida][lugar_escolhida] = 0

        case 4:
            continuar = input("deseja fechar o progama? s/n: ")
