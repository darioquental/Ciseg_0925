import time
numeros=[4,3,6,2,1,0]
#Index   0 1 2 3 4 5 6
#Length 6
i=0
numaux=0
troca= True

while troca:
   
    print(f"variavel{i} Lista de numeros {numeros}")
    time.sleep(1)
    troca=False
    i=0
    while i <= 4:
        # print("Valor I atual",listaNum[i],"Valor I seguinte",listaNum[i+1] )
        if ( numeros[i]>numeros[i+1] ):
            troca=True
            # print(i , "<- index maior que ->", i+1)
            numeros[i] , numeros[i+1]  = numeros[i+1] , numeros [i] # Troca directa de valores
        #                              
        #  numaux = numeros[i]        
        #  numeros[i] = numeros[i+1]   
        #  numeros[i+1] = numaux      
        print (i)
        print(f"variavel{i}")
        time.sleep(0.2)
        i+=1

print (numeros)