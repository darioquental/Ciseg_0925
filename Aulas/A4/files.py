#  Persistência de dados com ficheiros (txt, json, csv)

#  Passo 1: Abrir o ficheiro para leitura
# - Utiliza-se a função open() com o modo 'r' (read/leitura)
# - Exemplo: open("ficheiro.txt", "r")

#  Passo 2: Realizar ações no ficheiro
# - Modos de abertura:
#   'r' → leitura (read)
#   'w' → escrita (write) - sobrescreve o conteúdo existente
#   'a' → acrescentar (append) - adiciona ao final do ficheiro
#   'b' → modo binário (pode ser combinado com outros, ex: 'rb')
#   'x' → criar novo ficheiro - erro se já existir

#  Passo 3: Fechar o ficheiro
# - Sempre fechar o ficheiro após o uso com close()
# - Exemplo: ficheiro.close()



filename="C:/DEV/Ciseg_0925/Aulas/A4/Dados/fname.txt" 
frase=""

# Exemplo com 'with' para abrir e ler um ficheiro
with open(filename,'r',encoding='utf-8') as manipfile:
    frase=manipfile.read()
# Não é necessário chamar ficheiro.close() — é feito automaticamente

print("read from file : ",frase)

frase=input("insert a frase")

print("input no programa : ",frase)

with open(filename,'w',encoding='utf-8') as manipfile:
    manipfile.write(f"primeiro  \n  segundo \n {frase}")