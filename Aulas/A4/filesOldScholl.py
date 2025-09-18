# Files txt, json, csv criar persistencia
# 1 passo carregar o conteudo do ficheiro // Open  - r
# 2 - Acoes no ficheiro "Modo" / r (read), w  (write , subesescreve), a (append), b (binario),  x .
# 3 - Fechar o ficheiro  // Close

filename="C:/DEV/Ciseg_0925/Aulas/A4/Dados/fname.txt" 
frase=""

manipfile=open(filename,'r',encoding='utf-8')
frase=manipfile.read()
manipfile.close()

print("read from file : ",frase)

frase=input("insert a frase")

print("input no programa : ",frase)

manipfile=open(filename,'a',encoding='utf-8')
manipfile.write(f"primeiro  \n  segundo \n {frase}")
manipfile.close()