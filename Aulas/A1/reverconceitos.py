#variaveis
var1=0
#listas de varios tipos ex: int , str , bool, float
listanome=["Gui","Pedro","Andorinha"]
varletras="ola mundo"
i=0

#casting int(input("add a number")) cast de str to int
var1=int(input("add a number"))

#condiçao logica IF 
if var1==2:
    print("happy new year")

#ciclos de repetiçao for para listar
for nome in listanome:
    print(nome)

#ciclos de repetiçao while para listar
while i<len(listanome):
    print(listanome[i])
    i+=1

#add to list

listanome.append(input("add a name"))

#remove from list

print(listanome)

listanome.remove(input("add a existed name to remove from the list"))
listanome.pop(input("add a index to remove"))