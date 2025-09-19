# Dicionarios sao não ordenados e não usam index mas sim mapping 
# Acesso a  key : value ,  em vez de index 0 1 2 3
# Type struct
# Mutaveis

meudicionario={ "nome": "Joao", "idade": 20}


print("Contruido : ",meudicionario)
# alterar valor
meudicionario["nome"]="Pedro"

print("Alterado valor de key nome : ",meudicionario)

for chave , valor in meudicionario.items():
    print (f"Key do dicionario = {chave} valor dele =  {valor}")

# funcões uteis
print("items  ", meudicionario.items() )
print("keys  ", meudicionario.keys() )
print("values  ", meudicionario.values() )
print("get   ",meudicionario.get("nome") )
print("acesso value da key   ",meudicionario["nome"] )
print("get   ",meudicionario.get("email") )
#print("acesso value da key   ",meudicionario["email"] )   # usar get para acesso seguro e if

meudicionario.update({ "nome": "Antonio", "idade": 45}) # adiciona item que nao existe se existir muda valor
print("items  ", meudicionario.items() )
meudicionario["nomeproprio"]=meudicionario["nome"]
print("items  ", meudicionario.items() )
del meudicionario["nome"]
print("items  ", meudicionario.items() )

for chave , valor in meudicionario.items():
    print (f"Key do dicionario = {chave} valor dele =  {valor}")

meudicionario.update({ "email": "hhh@tot.pt"}) # adiciona item que nao existe (Chave) se existir muda valor (Valor)
print("items  ", meudicionario.items() ) 
meudicionario.pop("nomeproprio")      # Remove e retorna valor da chave
meudicionario.popitem()         # Remove o último item 

print("items  ", meudicionario.items() )