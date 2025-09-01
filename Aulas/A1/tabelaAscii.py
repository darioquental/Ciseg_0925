import time
# Tabela ascci
i=0
while i<258:
    time.sleep(0.1)
    #cast chr = de int para caracter // ord  = caratere para int
    print(chr(i))
    print(ord(chr(i)))
    i+=1