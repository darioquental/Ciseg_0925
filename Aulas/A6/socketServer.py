import socket

# Criar o socket do servidor
servSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Definindo o endereço IP e a porta
porta=12345
host="127.0.0.1"

# Bind (vincula) o socket à porta e ao IP
servSocket.bind((host,porta))

# Começa a escutar conexões
servSocket.listen(1)

print (f" Servidor Ligado em {host} : {porta}, aguardando conexão... ")

# Aceita a conexão do cliente
clientsoket , enderecoclient = servSocket.accept()
print (f" Conexão estabelecida com {enderecoclient} ")

# Fecha a conexão com o cliente e o servidor
clientsoket.close()
servSocket.close()