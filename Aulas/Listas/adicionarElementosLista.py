import time
nomes=[]
para=""

while para!="S" and para!="s":
    para=input("Deseja parar de intrud nomes S / N")
    if para=="S" or para=="s":
        continue
    nomes.append(input("Intrud Nome"))

i=0
arebenta=0
while True:
    print("oi")
    time.sleep(1)
    print("i = ", i ) 
    print("arebenta = ", arebenta ) 
    print(len(nomes))
    arebenta+= 3
    while i< arebenta : 
        print(nomes[i])
        print("i = ", i )
        time.sleep(1)
        i+=1            
    
