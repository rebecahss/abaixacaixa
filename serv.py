#Servidor

import socket
import os

IP = ""
Port = 30802
mensagem = [b'Recebido pelo servidor']


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	server.bind((IP,Port))

	server.listen(5)

	print ("Escutanto" ,IP,Port)

	obj, cliente = server.accept() 
	#print (cliente[0])''

	while True:
		msg = obj.recv(1024)
		msg1 = msg.decode('utf-8')
		
		print ("O que foi enviado:", msg1)
		
		if msg1 == 'ls':
			print("Você escolheu o comando ls")
			obj.send(b'Resposta do servidor')

		elif msg1 == 'enviar':
			print("recebendo arquivo")
			obj.send(b'Voce esta enviando arquivo')

			flname = 'recebido.txt'
			fyle =open(flname,'wb')
			fyle.write(obj.recv(6053))
			fyle.close()
			print('Arquivo recebido')

		elif msg1 == 'receb':
			obj.send(b'Voce esta recebendo arquivo.')

			flname = 'serv_to_cliente.txt'
			fyle = open(flname, 'rb')
			arquivo = fyle.read(6053)
			obj.send(arquivo)
			print('Aquivo enviado!')



		elif msg1 == 'sair':
			break

		else:
			print('Comando Inválido')
	
				

	server.close()
except Exception as erro:
	print (erro)
	server.close()



