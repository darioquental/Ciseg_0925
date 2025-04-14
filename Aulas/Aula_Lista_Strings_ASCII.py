import time
# Controlo de listas em 2 dimensoes 
cidades= [ "Lisboa", "Madrid", "São Paulo"]
#index i 1 dim       0    ,   1     ,   2
#             "L i s b o a"                   
#index it 2 dim   0 1 2 3 4 5
i=0
it=0
while i<=2:
    print ("valor na 1ª dimenção",cidades[i])
    #cidades[i][?]
    it=0
    while it< len(cidades[i]):
            print (f"1ª dimençao i= {i}")
            print (f"1ª dimençao it= {it}")
            print ("Letra na 2 dimençao",cidades[i][it])
            time.sleep(1)
            it+=1
    i+=1        




