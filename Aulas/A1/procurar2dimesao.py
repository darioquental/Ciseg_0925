import time
listanome=["Gui","Pedro","Andorinha"]
i=0
it=0
contador=0
nomeproc=""

nomeproc=input("nome para procura")

while i<len(listanome):
    it=0
    contador=0
    while it<len(listanome[i]):
      print("it",it)
      if it==len(nomeproc):
         break
      if listanome[i][it]==nomeproc[it]:
         time.sleep(0.1)
         print(listanome[i][it],"--",nomeproc[it])
         contador+=1
      it+=1
      if contador==len(listanome[i]):
         print("found")
    i+=1

print("contador",contador)