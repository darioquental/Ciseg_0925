import socket

# Criar a socket do cliente
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Definindo o endereço do servidor e a porta
porta=12345
host="127.0.0.1"

# Conectar ao servidor
clientSocket.connect((host,porta))

# Fecha a conexão
clientSocket.close()