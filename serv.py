#Servidor
import socket
import sys
import os
from _thread import *

IP = ""
Port = int(sys.argv[1])




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	server.bind((IP,Port))

except Exception as erro:
	print (erro)
	server.close()


server.listen(10)

print ("Escutanto com" ,IP,Port)

def protocolo(obj,mensagem):

	mensagem = bytes(mensagem,'utf-8')
	obj.send(mensagem)

def find_user(user,senha):
	usuario = user+' '+senha+'\n'
	arq = open('users.txt','r')
	datafile=arq.readlines()
	print(usuario)

	for line in datafile:
		if usuario in line:
			ret = 1
		else:
			ret = 0
	arq.close()
	return ret




def clientthread(obj):

	dir_atual = []

	

	while True:
		
		 
		msg = obj.recv(1024)
		msg1 = msg.decode('utf-8')
		#autenticação do usuário

		while msg1 == 'Criar' or msg1 =='Entrar':
			
		
			if msg1 == 'Criar':
				user = obj.recv(1024)
				user = user.decode('utf-8')
				obj.send(b'OK')

				senha = obj.recv(1024)
				senha = senha.decode('utf-8')
				obj.send(b'OK')
				flname = 'users.txt'
				fyle =open(flname,'a+')
				fyle.write(user+' '+senha+'\n')
				fyle.close()
				print(senha)
				os.makedirs(user)
				print('Diretorio criado')
				msg = obj.recv(1024)
				msg1 = msg.decode('utf-8')
				

			elif msg1 == 'Entrar':
				user = obj.recv(1024)
				user = user.decode('utf-8')
				
				obj.send(b'OK')

				senha = obj.recv(1024)
				senha = senha.decode('utf-8')
				
				ret=find_user(user,senha)
				print(ret)
				if ret == 1:
					obj.send(b'OK')
				else:
					obj.send(b'nao')

				
				aux = 1
				msg = obj.recv(1024)
				msg1 = msg.decode('utf-8')
				
			else:
				print('Cadastro Falhou')
			
			

		

		
		print ("O que foi enviado:", msg1)
		
		if msg1 == 'ls':
			print("Você escolheu o comando ls")
			obj.send(b'Resposta do servidor')

		elif msg1 == 'upload':
			protocolo(obj, 'Fazendo Upload')
			
			flname = obj.recv(6053)
			flname = flname.decode('utf-8')
			
			fyle =open(flname,'wb')
			fyle.write(obj.recv(6053))
			fyle.close()
			print('Arquivo recebido')


		elif msg1 == 'download':
			protocolo(obj, 'Fazendo download')

			flname = obj.recv(1024)
			flname = flname.decode('utf-8')

			fyle = open(flname, 'rb')
			arquivo = fyle.read(6053)
			obj.send(arquivo)
			print('Aquivo enviado!')


		elif msg1 == 'menu':
			print(menu)

		#elif msg1 == 'checkdir':

		#elif msg1 == 'cd':

		#elif msg1 == 'mv':

		#elif msg1 == 'rm':

		#elif msg1 == 'makedir':
	



		elif msg1 == 'sair':
			break

		else:
			print('Comando Inválido')

	obj.close()


while True:

	conn, cliente = server.accept() 
	start_new_thread(clientthread, (conn,))

	
	
				

server.close()



