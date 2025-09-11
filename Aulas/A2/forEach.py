#Funcionamento de for each
menssagem="Ola mundo"
listaCarateres=[]
caraterEmMensagem=""
i=0
somaChave=567

#mostra cada caratere em mensagem ( variavel String, Listas )
for caraterEmMensagem in menssagem:
       #cast de caraterEmMensagem para inteiro (ord()) para somar com chave e cast char(chr()) para retornar como caratere para a lista.
       listaCarateres.append(chr(somaChave+ord(caraterEmMensagem)))

#listar
print (listaCarateres)