#Servidor
import socket
import sys
import os
import os.path
from _thread import *

IP = ""
Port = int(sys.argv[1])
path_server = '/home/rebeca/Desktop/server' #Trocar esse path quando o servirdor trocar de pasta




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

def find_user(user,senha): #Procura o usuario
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

				os.makedirs(user)# cria um dir para o cliente
				flname= path_server+'/'+user+'/home.txt'#arquivo com informações
				fyle = open(flname,'w')
				flle.close()
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
					dir_atual = user
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
			flname2 = path_server+'/'+(flname[6:])
			print(flname2)
			fyle =open(flname2,'wb')
			fyle.write(obj.recv(6053))
			fyle.close()
			print('Arquivo recebido')
			


		elif msg1 == 'download':
			protocolo(obj, 'Fazendo download')

			flname = obj.recv(1024)
			flname = flname.decode('utf-8')
			flname2 = path_server+'/'+(flname[6:])

			fyle = open(flname2, 'rb')
			arquivo = fyle.read(6053)
			obj.send(arquivo)
			print('Aquivo enviado!')


		elif msg1 == 'menu':
			print(menu)

		elif msg1 == 'checkdir':
			protocolo(obj, 'Mostrar um diretorio')
			path_novo=obj.recv(1024)
			path_novo = path_novo.decode('utf-8')
			path_novo2=path_server+'/'+(path_novo[6:]) 
			diret =os.listdir(path_novo2)
			tamanho = len(diret)
			tamnho = str(tamanho)
			obj.send(bytes(tamanho))
			for i in range(len(diret)):
				i = str(i)
				obj.send(bytes(i, 'utf-8'))

		#elif msg1 == 'mv':

		elif msg1 == 'rm':
			protocolo(obj, 'Remover arquivo')
			path_novo=obj.recv(1024)
			path_novo = path_novo.decode('utf-8')
			path_novo2=path_server+'/'+(path_novo[6:]) 

			if os.path.isfile(path_novo2) == True:
				os.remove(path_novo2)
				obj.send(b'Arquivo removido')
			else:
				obj.send(b'Arquivo nao existe')



		elif msg1 == 'makedir':
			protocolo(obj, 'Criar um diretorio')
			path_novo=obj.recv(1024)
			path_novo = path_novo.decode('utf-8')
			path_novo2=path_server+'/'+(path_novo[6:]) 
			os.makedirs(path_novo2)
			print('Diretorio criado!')


		elif msg1 == 'sair':
			break

		else:
			print('Comando Inválido')

	obj.close()


while True:

	conn, cliente = server.accept() 
	start_new_thread(clientthread, (conn,))

	
	
				

server.close()



