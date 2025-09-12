import time
listaNum=[2,4,6,3,9,2]
# index   0 1 2 3 4 5
#length 6

i=0
varAux=0
FlagTroca=True

while FlagTroca:
    FlagTroca=False
    i=0
    while i< len(listaNum):
        if i<=len(listaNum)-2:
           # print("Valor I atual",listaNum[i],"Valor I seguinte",listaNum[i+1] )
            if listaNum[i]>listaNum[i+1] :
                FlagTroca=True
               # print(i , "<- index maior que ->", i+1)
                varAux=listaNum[i]        # 1 Guarda valor na posição a subescrever
                listaNum[i]=listaNum[i+1] # Copia valor da posição a frente
                listaNum[i+1]=varAux      # Faz o swap final com o valor guardado na 1
        time.sleep(0.2)
        i+=1

print(listaNum)