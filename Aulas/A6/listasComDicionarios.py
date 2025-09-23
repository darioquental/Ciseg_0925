# Criar um dicionario
dicion={
            "nome": "Ana Costa",
            "email": "ana.costa@gmail.com",
            "nif": "123456789",
            "telemovel": "912345678",
            "site": "https://www.anacosta.pt"
        }

print(dicion.items())
dicion.update({"nome": "Luis Andre"})
print(dicion.items())
input()

# criar lista de dicionarios
listaDiciona=[dicion] #cria lista

listaDiciona.append({                           #adiciona dicionario a lista
            "nome": "Joao Antonio",
            "email": "joao.a@gmail.com",
            "nif": "123456589",
            "telemovel": "962345678",
            "site": "https://www.joaoa.pt"
        })

print(listaDiciona[0]) # acesso a lista
print(listaDiciona[1]) # acesso a lista

for Dicio in listaDiciona:
    print("\n\n")
    for keyDicio, valueDicio in Dicio.items():
        print(keyDicio, " : " ,valueDicio )