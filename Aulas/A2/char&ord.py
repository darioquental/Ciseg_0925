import time
# ord() Cast para um caracter se turnar um numero int

# A - Z     ord(Letra)     65 - 90 
# exemplo ord("A") -> 65
# exemplo ord("Z") -> 90

# a - z     ord(Letra)     97 - 122 
# exemplo ord("a") -> 97
# exemplo ord("z") -> 122

# space     ord(" ")        32

# chr() Cast para um int se turnar um caratere
#  65 - 90    chr(Num)     A - Z 
# exemplo chr(65) -> "A"
# exemplo chr(90) -> "Z"

# 97 - 122     chr(Num)   a - z   
# exemplo chr(97) ->  "a"
# exemplo chr(122) -> "z"


# exemplo chr 

i=65

while i<=90:
    print(chr(i))
    if chr(i) == "K":
        print ("Acertou no K")
    i+=1


i=97
while i<=122:
    print(chr(i))
    i+=1


# exemplo de ord()

i=0
nome="Pedro Antunes"
keepSpaceIndex=0
foundSpace=False
#inde 0,1,2,3,4,5,6,7,8,9,10,11,12


while i < len(nome):
    print("Letra: ", nome[i], " numero INT" , ord(nome[i]))

    #Procura letras A-Z
    if ord(nome[i]) >= 65 and ord(nome[i])<=90:
        print("Letra Maiuscula \n")
        time.sleep(0.2)
    #Procura letras a-z
    if ord(nome[i]) >= 97 and ord(nome[i])<=122:
        print("Letra Minuscula \n")
        time.sleep(0.2)
    #Procura o espaço
    if ord(nome[i]) == 32:
        print ("espaço encontrado\n")
        foundSpace=True
        keepSpaceIndex=i
        time.sleep(0.2)
    #usa as flags para revelar a posiçao do espaço
    i+=1
if foundSpace:
    print ("foi encontrado um espaço na posiçao:",keepSpaceIndex)
    time.sleep(0.2)
    