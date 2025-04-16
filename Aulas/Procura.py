# Algoritmo para Procura
import time
nomproc=""
contaigualdade=0
#index i     0               1               2               3
nomes=["Dario Quental", "Joao Matos", "Liliana Queiroz","Joao Matos"]
indexproc=[]
#ind it 0123456789101112
#Nomes[i][it]

nomproc="Joao Matos"
#        0123456789  10

for i in range(len(nomes)):
    print("valor e i no for externo roda 1 dimensao da lista", i )
    contaigualdade=0
    print("Nome no index 1º dimenção",nomes[i])
    for it in range(len(nomes[i])):
        time.sleep(1)
        print("valor e it no for interno roda segunda dimençao da lista", it )
        print(nomes[i][it])
        print (nomproc[it])
        if ord(nomes[i][it]) == ord(nomproc[it]):
            contaigualdade+=1
        print("igualdade = ",contaigualdade)
        if contaigualdade==len(nomproc):
            print ("nome em nomes",nomes[i], "posiçao da lista", i )
            print ("nome em nomproc", nomproc)    
        if it == (len(nomproc)-1): 
           print("tamanho do valor nomproc",len(nomproc)) 
           break

