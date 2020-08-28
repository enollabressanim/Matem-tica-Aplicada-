def imprimir_menu():
    print("O que você deseja fazer:")
    print("1 - Adicionar seriado")
    print("2 - Consultar lista")
    print("3 - Remover")
    print("4 - Descobrir um dos angulos desconhecidos")
    print("5 - Sair")
    print("6 - ")

def descobrir_angulo(a, b):
    angulo = 180 - (a + b)
    print(angulo)
    return angulo 

imprimir_menu()
opcao = input("Digite a opção desejada: ")
if opcao == "4":
    a = float(input("Informe o angulo a: "))
    b = float(input("Informe o angulo b: "))
    descobrir_angulo(a, b)