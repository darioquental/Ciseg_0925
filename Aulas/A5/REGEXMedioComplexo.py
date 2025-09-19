import re

# Validações , substituições e procura de qualquer tipo de texto

# Padrões
# "ABC"  ----  > procurar o padrão ABC no texto
# [A-L]  ----  > procurar o padrão de A a L no texto
# *.mp3 ----  > procurar o padrão de tudo que acabe em .mp3 no texto

# funções
# re.search() -- > procura padrao em qualquer parte do texto
# re.match()  -- > procura do inico da string
# re.findall()  -- > devolve todas as ocorrências
# re.split()    -- > divide a string em partes por padrao 

#Validar email
email="ddd@asdas.pt"

padrao=r"^[\w\.]+@[\w]+\.\w+$"

resultado=re.match(padrao,email)

print(resultado.group())
print(resultado.start())
print(resultado.end())
print(resultado.span())

# ^ → início da string
# [\w\.-]+ → letras, números, underscore, ponto ou hífen
#@ → arroba
#\.\w+ → ponto seguido de letras (ex: .com, .pt)
#$ → fim da string