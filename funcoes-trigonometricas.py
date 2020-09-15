import math

def main () :
    def menu():
        print("O que você deseja fazer:")
        print("1 - Função de seno")
        print("2 - Função de cosseno")
        print("3 - Função da tangente")
    
    def periodo_seno(c):
        if c < 0:
            c = c * -1 
            periodo_s = (2 * math.pi) / c
            print("período: ", periodo_s)
        else:
            periodo_s = (2 * math.pi) / c
            print("período: ", periodo_s)
    
    def imagem_seno(a,b):
        im1 = a - b
        im2 = a + b
        if im1 > im2:
            print("imagem: [", im2, ",", im1, "]")
        else:
            print("imagem: [", im1, ",", im2, "]")
        
    def amplitude_seno(b):
        if b < 0:
            b = b * -1
            print("amplitude: ", b)
        else:
            print("amplitude: ", b)

    def periodo_cosseno(c):
        if c < 0:
            c = c * -1 
            periodo_s = (2 * math.pi) / c
            print("período: ", periodo_s)
        else:
            periodo_s = (2 * math.pi) / c
            print("período: ", periodo_s)
    
    def imagem_cosseno(a,b):
        im1 = a - b
        im2 = a + b
        if im1 > im2:
            print("imagem: [", im2, ",", im1, "]")
        else:
            print("imagem: [", im1, ",", im2, "]")
        
    def amplitude_cosseno(b):
        if b < 0:
            b = b * -1
            print("amplitude: ", b)
        else:
            print("amplitude: ", b)
    
    def periodo_tan(c):
        if c < 0:
            c = c * -1
            periodo = math.pi/c
            print("período: ", periodo)
        else:
            periodo = math.pi/c
            print("período: ", periodo)    


    menu()
    opcao = input("digite a opcao desejada: ")
    if opcao == "1":
        print("Insira as variáveis da função:")
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        periodo_seno(c)
        imagem_seno(a,b)
        amplitude_seno(b)

    elif opcao == "2":
        print("Insira as variáveis da função:")
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        periodo_cosseno(c)
        imagem_cosseno(a,b)
        amplitude_cosseno(b)

    elif opcao == "3":
        print("Insira as variáveis da função:")
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        periodo_tan(c)



if __name__ =='__main__':
    main ()
