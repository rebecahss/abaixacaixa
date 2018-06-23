#Servidor

import socket

IP = ""
Port = 30801
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
		
		print ("O que foi enviado:", msg)
		msg1 = msg.decode('utf-8')
		if msg1 == 'ls':
			print("Você escolheu o comando ls")
			obj.send(b'Resposta do servidor')

		elif msg1== 'sair':
			break

		else:
			print("Comando Inválido")
	
				

	server.close()
except Exception as erro:
	print (erro)
	server.close()



