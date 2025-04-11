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
        if ( numeros[i]>numeros[i+1] ):
            troca=True
            numeros[i] , numeros[i+1]  = numeros[i+1] , numeros [i]
        #                              4,3 
        #  numaux = numeros[i]         0=4
        #  numeros[i] = numeros[i+1]   3,3
        #  numeros[i+1] = numaux       3,4
        print (i)
        print(f"variavel{i}")
        time.sleep(1)
        i+=1

print (numeros)