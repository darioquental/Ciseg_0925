Morada={ "RUA":"Rua do Safiro" , "Portas": [ 1,2,3,4,5,6,7,8,9 ]}

Morada["RUA"]="Rua do dicionario" # Atribuiçao de valor a key RUA
Morada["Portas"].pop(-1)          # Uso de methodos de lista para retirar ultimo valor que esta na key Portas
print(Morada.items())             # Mostra dicionario inteiro
Morada.update({"RUA":"Rua do Porto"}) # Atribuiçao de valor a key RUA, mas se nao existir adiciona a estrutura do dicionario
print(Morada.items()) 

for chave, value in Morada.items(): 
    if isinstance(value,list):
        for val in value:
            print(chave," : ",val)
    else:
        print(chave," : ",value)
