# Declaraçao   ().
# Nao podem mudar nem adicionar depois de criados.
# Podem ser criados enquanto o programa corre.
# utilizar em dicionarios dado que eles sao indexados tal como as lista
# aplicações String que nunca muda, extenções, parametros de db  keys de dicionario

# criar tuple
my_tuple_extentions=(".exe",".mp3",".docs")
num1=0
num2=0

print(my_tuple_extentions[1])

for ext in my_tuple_extentions:
    print(ext)

num1=int(input("insert a number"))
num2=int(input("insert a number"))

# criar tuple in runtime
my_tuple_create=(num1,num2)

for extcreat in my_tuple_create:
    print(extcreat)

numero1 , numero2= my_tuple_create

print(numero1)
print(numero2)