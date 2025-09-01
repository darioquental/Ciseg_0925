#aceder lista por 2 dimensões

#   i        0      1         2 
listanome=["Gui","Pedro","Andorinha"]
#   it      012   01234   012345678  
i=0
it=0

#Loop do i 1 dimenção ou seja nome completo na posição da lista
while i<len(listanome):
    #reset da 2 dimensão para iniciar do 0
    it=0
    #Loop do it 2 dimenção ou seja letra a letra em cada nome
    while it<len(listanome[i]):
      print(listanome[i][it])
      #print(i , it ,len(listanome),len(listanome[i]) para debug dos ciclos
      it+=1
    i+=1