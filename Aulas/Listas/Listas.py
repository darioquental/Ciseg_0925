# Uma variavel que contem varios valores e podem ter varios tipos de dados 
INDEXX=0
numeros=[1,2,3,4,5,6,7]
listas=[1,2]
#  index 0,1,2,3,4,5,6
#  length 7      
print (len(numeros))
print (numeros)


#  length 8
#numeros=[1,2,3,4,5,6,7,8]
numeros.append(8)
print (len(numeros))
print (numeros)

#  length 9
#numeros=[10,1,2,3,4,5,6,7,8]
numeros.insert(0,10)
print (len(numeros))
print (numeros)
num1=6
#  length 8
#numeros=[10,1,2,3,4,6,7,8]
numeros.remove(9)
print (len(numeros))
print (numeros)

#  length 7
#numeros=[1,2,3,4,6,7,8]
numeros.pop(INDEXX)
print (len(numeros))
print ("remover por index usando pop",numeros)







numeros=[1,2,3,4,5,6,7]
#print no index
print (numeros[0]) # 1
#print das primeiras posiçoes por index
print (numeros[:3])
#print das ultimas posiçoes por index
print (numeros[5:])
#print de uma posiçao a outra do index
print (numeros[2:6])


