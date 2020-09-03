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
    
    ######################################################################################
    
    import math

def main () : 

    def imprimir_menu():
        print("O que você deseja fazer:")
        print("1 - descobrir angulo interno")
        print("2 - descobrir outros dois angulos")
        print("3 - Descobrir um dos lados")
        print("4 - Descobrir um dos angulos desconhecidos")
        print("5 - ")
        print("6 - descobrir area com hipotenusa e cateto ")
        print("7 - descobrir area apenas com catetos ")
        print("8 - sair")
    
    def descobrir_angulo_interno(a, b, c):
        alpha = math.acos((pow(b, 2)+pow(c, 2)-pow(a, 2))/(2*b*c))
        angulo1 = math.degrees(alpha)
        beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
        angulo2 = math.degrees(beta)
        gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
        angulo3 = math.degrees(gamma)
        print("angulo 1: ", angulo1, "angulo 2: ", angulo2, "angulo 3: ", angulo3)
        return angulo1, angulo2, angulo3

    def descobrir_angulo_com_lados(b, c, alpha):
        a = math.sqrt((b ** 2) + (c **2))
        beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
        angulo2 = math.degrees(beta)
        gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
        angulo3 = math.degrees(gamma)
        print("angulo 1: ", alpha, "angulo 2: ", angulo2, "angulo 3:", angulo3)
        return angulo2, angulo3

    def descobrir_angulo(a, b):
        angulo = 180 - (a + b)
        print(angulo)
        return angulo 

    def descobrir_hipotenusa(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) + (lado2 **2))
        return lado3
        
    def descobrir_cateto(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) - (lado2 **2))
        return lado3

    def descobrir_area(lado1, lado2, lado3):
        p = (lado1 + lado2 + lado3) / 2
        a = math.sqrt(p*(p - lado1)*(p - lado2)*(p - lado3))
        print(a)
        return a

    imprimir_menu()
    opcao = input("Digite a opção desejada: ")
    while opcao != "8":
        if opcao == "1":
            a = float(input("Digite o valor do lado a: "))
            b = float(input("Digite o valor do lado b: "))
            c = float(input("Digite o valor do lado c: "))
            descobrir_angulo_interno(a, b, c)
            break
        
        elif opcao == "2":
            b = float(input("Digite o valor do lado b: "))
            c = float(input("Digite o valor do lado c: "))
            alpha =  float(input("Informe o angulo ^A: "))
            descobrir_angulo_com_lados(b, c, alpha)

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
            break

        elif opcao == "6":
            lado1 = float(input("Digite o valor de um cateto: "))
            lado2 = float(input("Digite o valor do outro cateto: "))
            lado3 = descobrir_hipotenusa(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)
            break

        elif opcao == "7":
            lado1 = float(input("Digite o valor da hipotenusa: "))
            lado2 = float(input("Digite o valor de um dos catetos: "))
            lado3 = descobrir_cateto(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)
            break
    imprimir_menu()
    opcao = input("Digite a opção desejada: ")
if __name__ =='__main__':
    main ()

############################################################################################

import math

def main () : 

    def imprimir_menu():
        print("\nO que você deseja fazer:")
        print("1 - descobrir angulo interno")
        print("2 - descobrir outros dois angulos")
        print("3 - Descobrir um dos lados")
        print("4 - Descobrir um dos angulos desconhecidos")
        print("5 - Descobrir dois lados")
        print("6 - descobrir area com hipotenusa e cateto ")
        print("7 - descobrir area apenas com catetos ")
        print("8 - sair")
    
    def descobrir_angulo_interno(a, b, c):
        alpha = math.acos((pow(b, 2)+pow(c, 2)-pow(a, 2))/(2*b*c))
        angulo1 = math.degrees(alpha)
        beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
        angulo2 = math.degrees(beta)
        gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
        angulo3 = math.degrees(gamma)
        print("angulo 1: ", "%.6f" % angulo1, "\nangulo 2: ", "%.6f" % angulo2, "\nangulo 3: ", "%.6f" % angulo3)
        return angulo1, angulo2, angulo3

    def descobrir_angulo_com_lados(b, c, alpha):
        a = math.sqrt((b ** 2) + (c **2))
        beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
        angulo2 = math.degrees(beta)
        gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
        angulo3 = math.degrees(gamma)
        print("angulo 1: ", "%.6f" % alpha, "\nangulo 2: ", "%.6f" % angulo2, "\nangulo 3:", "%.6f" % angulo3)
        return angulo2, angulo3

    def descobrir_angulo(a, b):
        angulo = 180 - (a + b)
        print("%.6f" % angulo)
        return angulo 

    def descobrir_hipotenusa(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) + (lado2 **2))
        return lado3
        
    def descobrir_cateto(lado1, lado2):
        lado3 = math.sqrt((lado1 ** 2) - (lado2 **2))
        return lado3
    
    def descobrir_lados(B, C, a):
        anguloA = 180 - (B + C)
        ladoB = a * math.sin(math.radians(B)) / math.sin(math.radians(anguloA))
        ladoC =  a * math.sin(math.radians(C)) / math.sin(math.radians(anguloA))
        print("Lado A:", "%.6f" % a,"\nLado B: ", "%.6f" % ladoB, "\nLado C:", "%.6f" % ladoC)
        return ladoB, ladoC

    def descobrir_area(lado1, lado2, lado3):
        p = (lado1 + lado2 + lado3) / 2
        a = math.sqrt(p*(p - lado1)*(p - lado2)*(p - lado3))
        print("Área: ", "%.6f" % a)
        return a

    imprimir_menu()
    opcao = input("Insira a função que deseja realizar: ")
    while opcao != "8":
        if opcao == "1":
            a = float(input("Digite o valor do lado a: "))
            b = float(input("Digite o valor do lado b: "))
            c = float(input("Digite o valor do lado c: "))
            descobrir_angulo_interno(a, b, c)
            break
        
        elif opcao == "2":
            b = float(input("Digite o valor do lado b: "))
            c = float(input("Digite o valor do lado c: "))
            alpha =  float(input("Informe o angulo ^A: "))
            descobrir_angulo_com_lados(b, c, alpha)
            break

        elif opcao == "3":
            opcao2 = input("difite H para descobrir a hipotenusa ou C para descobrir um dos catetos: ")
            if opcao2 == "H":
                lado1 = float(input("Digite o valor do primeiro cateto: "))
                lado2 = float(input("Digite o valor do segundo cateto: "))
                angulo = input("Insira o angulo: ")
                print("%.6f" % descobrir_hipotenusa(lado1, lado2))
                break

            elif opcao2 == "C":
                lado1 = float(input("Digite o valor da hipotenusa: "))
                lado2 = float(input("Digite o valor de um dos cateto: "))
                angulo = input("Insira o angulo: ")
                print("%.6f" % descobrir_cateto(lado1, lado2))
                break

        elif opcao == "4":
            a = float(input("Informe o angulo a: "))
            b = float(input("Informe o angulo b: "))
            lado = input("Insira o lado: ")
            descobrir_angulo(a, b)
            break

        elif opcao == "5":
            B = int(input("Digite o angulo B: "))
            C = int(input("Digite o angulo C: "))
            a = int(input("Digite o lado A: "))
            descobrir_lados(B, C, a)
            break

        elif opcao == "6":
            lado1 = float(input("Digite o valor de um cateto: "))
            lado2 = float(input("Digite o valor do outro cateto: "))
            angulo = input("Insira o angulo: ")
            lado3 = descobrir_hipotenusa(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)
            break

        elif opcao == "7":
            lado1 = float(input("Digite o valor da hipotenusa: "))
            lado2 = float(input("Digite o valor de um dos catetos: "))
            angulo = input("Insira o angulo: ")
            lado3 = descobrir_cateto(lado1, lado2)
            descobrir_area(lado1, lado2, lado3)
            break
if __name__ =='__main__':
    main ()
