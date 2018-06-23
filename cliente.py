#Cliente
import socket

Server_IP = "localhost"
Server_Port = 30802


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((Server_IP, Server_Port))

while True:

	msg =input("Envie algo ao servidor:")
	msg1 = bytes(msg,'utf-8')
	

	if msg1 == b'ls':
		cliente.send(msg1)
		resposta = cliente.recv(1024)
		print(resposta.decode('utf-8'))

	elif msg1 == b'enviar':

		cliente.send(msg1)
		resposta = cliente.recv(1024)
		print(resposta.decode('utf-8'))

		flname = 'cliente_to_serv.txt'
		fyle = open(flname, 'rb')
		arquivo = fyle.read(6053)
		cliente.send(arquivo)
		print('Aquivo enviado!')

	elif msg1 == b'receb':

		cliente.send(msg1)
		resposta = cliente.recv(1024)
		print(resposta.decode('utf-8'))

		flname = input("Escreva o nome do arquivo:")
		fyle =open(flname,'wb')
		fyle.write(cliente.recv(6053))
		fyle.close()
		print('Arquivo recebido')



	elif msg1 == b'sair':
		cliente.send(msg1)
		break

cliente.close()
