import os
import json

dicionario={}

MFICHEIRO = r"C:\DEV\Ciseg_0925\Aulas\A6\file1.json"
if os.path.exists(MFICHEIRO):  # Verifica se o ficheiro já existe
    with open(MFICHEIRO, 'r', encoding='utf-8') as f:      
        dicionario=json.load(f)  # Tenta carregar os dados do JSON

print(dicionario)
print("Keys : ", dicionario[0].keys())

with open(MFICHEIRO, 'w', encoding='utf-8') as f:
    # json.dump salva o dicionário no arquivo como texto JSON
    # indent=4 deixa o JSON formatado
    # f: é o file handler, o arquivo aberto em modo escrita "w".
    # ensure_ascii=False permite acentos e caracteres especiais
    json.dump(dicionario, f, indent=4, ensure_ascii=False)