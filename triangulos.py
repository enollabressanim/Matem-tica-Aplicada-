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
    
    ##########################################################################
    
    import math

def main () : 

    def imprimir_menu():
        print("O que você deseja fazer:")
        print("1 - ")
        print("2 - ")
        print("3 - Descobrir um dos lados")
        print("4 - Descobrir um dos angulos desconhecidos")
        print("5 - ")
        print("6 - descobrir area com hipotenusa e cateto ")
        print("7 - descobrir area apenas com catetos ")
        print("8 - sair")

    def descobrir_angulo(a, b):
        angulo = 180 - (a + b)
        print(angulo)
        return angulo 

    def descobrir_hipotenusa(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) + (lado2 **2))
    #    print(lado3)
        return lado3
        
    def descobrir_cateto(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) - (lado2 **2))
    #    print(lado3)
        return lado3

    def descobrir_area(lado1, lado2, lado3):
        p = (lado1 + lado2 + lado3) / 2
        a = math.sqrt(p*(p - lado1)*(p - lado2)*(p - lado3))
        print(a)
        return a

    imprimir_menu()
    opcao = input("Digite a opção desejada: ")
    while opcao != "8":
        if opcao == "3":
            opcao2 = input("difite H para descobrir a hipotenusa ou C para descobrir um dos catetos: ")
            if opcao2 == "H":
                lado1 = float(input("Digite o valor do primeiro cateto: "))
                lado2 = float(input("Digite o valor do segundo cateto: "))
                print(descobrir_hipotenusa(lado1, lado2))
                break
            elif opcao2 == "C":
                lado1 = float(input("Digite o valor da hipotenusa: "))
                lado2 = float(input("Digite o valor de um dos cateto: "))
                print(descobrir_cateto(lado1, lado2))
                break

        elif opcao == "4":
            a = float(input("Informe o angulo a: "))
            b = float(input("Informe o angulo b: "))
            descobrir_angulo(a, b)

        elif opcao == "6":
            lado1 = float(input("Digite o valor de um cateto: "))
            lado2 = float(input("Digite o valor do outro cateto: "))
            lado3 = descobrir_hipotenusa(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)

        elif opcao == "7":
            lado1 = float(input("Digite o valor da hipotenusa: "))
            lado2 = float(input("Digite o valor de um dos catetos: "))
            lado3 = descobrir_cateto(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)
    imprimir_menu()
    opcao = input("Digite a opção desejada: ")
if __name__ =='__main__':
    main ()
