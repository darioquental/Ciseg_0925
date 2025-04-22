numeros=[1,4,5,6,7]
termina=True
opc=0
num=0
nome=""

def listar(nummeros):
    try:
        for i in range(len(nummeros)+2):
            print(nummeros[i])
    except Exception as error:
        print ("Erro no Programa  ",type(error).__name__ ,"   ", error)

def adicionar(nummeros,inputdinamico):
    nummeros.append(inputdinamico)
    return nummeros

while termina:
    print ("1 para Listar")
    print ("2 para Introduzir numero")
    print ("3 para Introduzir Nome")
    print ("4 Sair do Programa")

    opc=int(input("Introd Opcão"))
    match opc:
        case 1:
            listar(numeros)
        case 2:
            num=int(input("Introd novo numero"))
            numeros=adicionar(numeros,num)
        case 3:
            nome=input("Introd novo nome")
            numeros=adicionar(numeros,nome)
        case 4:
            termina=False
        case _:
            print ("Opcao Invalida")