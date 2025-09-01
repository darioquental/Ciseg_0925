listanome=["Gui","Pedro","Andorinha","Gui"]
i=0
#flags 
flagigualdade=0
flagkeepindex=[]

nomeproc=input("name to search")
#ciclos de repetiçao while
while i<len(listanome):
    #compara posiçao a posiçao com nome intrud
    if listanome[i]==nomeproc:
       #flag para contar as igualdades
       flagigualdade+=1
       #flag para guardar os index    
       flagkeepindex.append(i)  
    i+=1
print(flagkeepindex)

#se nome foi encontrado ou não
if flagigualdade>0:
    print("name found")
else:
    print("not found")    