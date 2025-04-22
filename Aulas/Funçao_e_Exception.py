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
        print ("erro no programa  ",type(error).__name__ ,"   ", error)

def adicionar(nummeros,inputdinamico):
    nummeros.append(inputdinamico)
    return nummeros

while termina:
    print ("1 para listar")
    print ("2 para introduzir numero")
    print ("3 para introduzir Nome")
    print ("4 Sair do Programa")

    opc=int(input("Introd Opcão"))
    match opc:
        case 1:
            listar(numeros)
        case 2:
            num=int(input("introd novo numero"))
            numeros=adicionar(numeros,num)
        case 3:
            nome=input("introd novo nome")
            numeros=adicionar(numeros,nome)
        case 4:
            termina=False
        case _:
            print ("opcao invalida")