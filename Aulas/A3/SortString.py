listaNome=["Dario Quental","Dario Almeida","Bruno Carvalho"]
# index         0                1                 2
#length 3
 
i=0 # Variavel que controla a primeira posiçao ( nome )
it=0 # Variavel que controla a segunda posiçao ( letra do nome )
controloTroca=-1 # guarda a posiçao da 1 dimensao(nome inteiro) que existiu uma troca
il=1 # Variavel que controla as rotações a lista inteira
 
while il<len(listaNome):       # Loop controla as voltas a lista
    i=0                # reposiçao do index da lista 1 dimensão ( Nome )
    print("IL - ",il)
    while i< len(listaNome):  # Loop controla a posiçao do nome
        print("\n\n","index 1 pos - ",i,"\n\n")
        if i<=len(listaNome)-2:
            it=0  # reposiçao do index da lista 2 dimensão ( Letras )
            controloTroca=-1 # reposiçao da variavel troca // tambem seria possivel usar um break
            while it<len(listaNome[i]) and it< len(listaNome[i+1]): # Loop controla as letras no nome
                print("index 2 pos - ",it," Valor Controla troca ", controloTroca)
                if ord(listaNome[i][it]) > ord(listaNome[i+1][it]) and  controloTroca != i :
                    print("If da troca posicao do i", i ," posiçao do  it", it )
                    print (listaNome[i][it] , "   -   " , listaNome[i+1][it] )
                    controloTroca=i # controlar index da primeira dimençao ( quando acontece troca de nome ja nao é trocado nenhum nome)
                    listaNome.insert(i,listaNome[i+1]) # insere o nome mais pequeno(ASCII) atras do nome maior (ASCII)
                    print(listaNome)
                    listaNome.pop(i+2) # apaga a posiçao extra na lista que ja foi anteriomente movida no insert
                    print(listaNome)
                it+=1                        
        i+=1
    il+=1

    ''' Exercicio 3.1 Corrigir o problema com a troca Extra.
 
        Exercicio 4 Ordena as Letras de Z-A de em uma lista com uma unica string.
        EX: lista=[" EU GOSTO E DO VERAO"]
 
        Exercicio 4.1 Atualiza o codigo anterior para incluir letras pequenas e com acentos.
        Em que E maior , e menor ou é com acento valem o mesmo, e as restantes letras igual.
        Incluir todas as acentuações portuguesas a valer o mesmo que a letra normal tal como explicado em cima.
        EX: lista=[" Eu Gosto é do verão"] '''