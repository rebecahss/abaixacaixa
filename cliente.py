#Cliente
import socket
import sys


#Server_IP = "localhost"
#Server_Port = 30802

Server_IP = str(sys.argv[1])
Server_Port = int(sys.argv[2])



cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((Server_IP, Server_Port))

def protocolo(cliente):

	resposta = cliente.recv(1024)
	return resposta

#predefinições
path_atual = []


#Boas Vindas ,Cadasatro e login

print('Bem-Vindo ao AbaixaCaixa!')
print()




a=0

while a == 0:
	login = input('Se ainda não possui cadastro digite "Criar", Se já é cadastrado digite "Entrar" : ')
	cliente.send(bytes(login,'utf-8'))

	if login == 'Entrar':
		user =input('Digite o nome usuário: ')
		user = bytes(user,'utf-8')
		cliente.send(user)
		resposta = cliente.recv(1024)
		print(resposta)

		senha =input('Digite sua senha: ')
		senha = bytes(senha,'utf-8')
		cliente.send(senha)
		resposta = cliente.recv(1024)
		print(resposta)
		if resposta == b'OK':
			a=1
		else:
			print('SENHA OU USUÁRIO INVÁLIDO')
			a=0

	elif login == 'Criar':
		user = input('Escolha um nome de usuário: ')
		user = bytes(user,'utf-8')
		cliente.send(user)
		resposta = cliente.recv(1024)
		print (resposta)

		senha =input('Digite sua senha: ')
		senha = bytes(senha,'utf-8')
		cliente.send(senha)
		resposta = cliente.recv(1024)
		print(resposta)
		a=1
	else:
		print("Comando Inválido. te")
path_atual = '/home/'+user.decode('utf-8')+'/'
#MENU DE COMANDOS

print('Seja bem vindo(a)',user.decode('utf-8'),'!')
print()
print("Lista de Comandos")
print()
print('- checkdir -> Apresenta pastas e arquivos no diretorio corrente')
print('- mv -> Move um arquivo para um diretório destino')
print('- rm -> Remove o arquivo ou um diretório"')
print('- makedir -> Cria um novo diretório')
print('- upload -> Faz upload de um arquivo para o servidor')
print('- download -> faz o download de um arquivo para a sua maquina')
print()





while True:


	msg =input("Digite um comando:")
	msg1 = bytes(msg,'utf-8')
	

	if msg1 == b'menu':
		print('Seja bem vindo(a)',user,'!')
		print()
		print("Lista de Comandos")
		print()
		print('- checkdir -> Apresenta pastas e arquivos no diretorio corrente')
		print('- mv -> Move um arquivo para um diretório destino')
		print('- rm -> Remove o arquivo ou um diretório"')
		print('- makedir -> Cria um novo diretório')
		print('- upload -> Faz upload de um arquivo para o servidor')
		print('- download -> faz o download de um arquivo para a sua maquina')
		print()
				

	elif msg1 == b'upload':

		cliente.send(msg1)
		resposta = cliente.recv(1024)

		flname = input('Digite o nome do path: ')
		nome_arq = input('Escreva o nome do arquivo: ')
		enviar=flname+'/'+nome_arq
		cliente.send(bytes(enviar,'utf-8'))

		fyle = open(nome_arq, 'rb')
		arquivo = fyle.read(6053)
		cliente.send(arquivo)
		print('Aquivo enviado!')

	elif msg1 == b'download':

		cliente.send(msg1)
		resposta = cliente.recv(1024)

		flname = input("Escreva o nome do path: ")
		nome_arq = input('Escreva o nome do arquivo: ')
		enviar =flname+'/'+nome_arq
		cliente.send(bytes(enviar,'utf-8'))

		fyle =open(nome_arq,'wb')
		fyle.write(cliente.recv(6053))
		fyle.close()
		print('Arquivo recebido')

	elif msg1 == b'checkdir':
		cliente.send(msg1)
		resposta = cliente.recv(1024)
		path_novo=input('Escreva o path diretorio: ')
		cliente.send(bytes(path_novo,'utf-8'))
		tamanho=cliente.recv(1024)
		tamanho = tamanho.decode('utf-8')
		tamanho = int(tamanho)
		for i in range(tamanho):
			resposta = cliente.recv(1024)
			print(resposta.decode('utf-8'))

	elif msg1 == b'makedir':
		cliente.send(msg1)
		resposta = cliente.recv(1024)
		path_novo=input('Escreva o path do novo diretorio')
		cliente.send(bytes(path_novo,'utf-8'))

	elif msg1 == b'rm':

		cliente.send(msg1)
		resposta = cliente.recv(1024)
		flname=input('Escreva o path onde o arquivo esta: ')
		nome_arq = input('Escreva o nome do arquivo: ')
		enviar =flname+'/'+nome_arq
		cliente.send(bytes(enviar,'utf-8'))
		resposta2= cliente.recv(1024)
		print(resposta2.decode('utf-8'))




		

	elif msg1 == b'sair':
		cliente.send(msg1)
		break
	else:
		print("Comando Inválido")

cliente.close()
