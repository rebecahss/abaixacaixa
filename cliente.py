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
login = input('Se ainda não possui cadastro digite "Criar", Se já é cadastrado digite "Entrar" : ')



a=0

while a == 0:
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
		a=1

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

#MENU DE COMANDOS

print('Seja bem vindo(a)',user,'!')
print()
print("Lista de Comandos")
print()
print('- checkdir -> Apresenta pastas e arquivos no diretorio corrente')
print('- cd path_to_dir -> Permite acesso ao diretório "path_to_dir"')
print('- mv org_file dest_dir -> Move "org_file" para o diretório "dest_dir"')
print('- rm file -> Remove o arquivo ou diretório de nome "dirname"')
print('- makedir dirname -> Cria um novo diretório"de nome dirname"')
print('- upload path_to_file -> Faz upload de um arquivo em path_to_file para o servidor')
print('- download file -> faz o download do arquivo "file" para a sua maquina')






while True:


	msg =input("Digite um comando:")
	msg1 = bytes(msg,'utf-8')
	

	if msg1 == b'menu':
		print('Seja bem vindo(a)',user,'!')
		print()
		print("Lista de Comandos")
		print()
		print('- checkdir -> Apresenta pastas e arquivos no diretorio corrente')
		print('- cd path_to_dir -> Permite acesso ao diretório "path_to_dir"')
		print('- mv org_file dest_dir -> Move "org_file" para o diretório "dest_dir"')
		print('- rm file -> Remove o arquivo ou diretório de nome "dirname"')
		print('- makedir dirname -> Cria um novo diretório"de nome dirname"')
		print('- upload path_to_file -> Faz upload de um arquivo em path_to_file para o servidor')
		print('- download file -> faz o download do arquivo "file" para a sua maquina')

		cliente.send(msg1)

		resposta = cliente.recv(1024)
		print(resposta.decode('utf-8'))

	elif msg1 == b'upload':

		cliente.send(msg1)
		reposta = protocolo(obj)

		flname = input('Digite o nome do arquivo: ')
		fyle = open(flname, 'rb')
		arquivo = fyle.read(6053)
		cliente.send(arquivo)
		print('Aquivo enviado!')

	elif msg1 == b'download':

		cliente.send(msg1)
		resposta = cliente.recv(1024)
		print(resposta.decode('utf-8'))

		flname = input("Escreva o nome do arquivo:")
		fyle =open(flname,'wb')
		fyle.write(cliente.recv(6053))
		fyle.close()
		print('Arquivo recebido')

	elif msg1 == b'checkdir':

	elif msg1 == b'cd':

	elif msg1 == b'mv':

	elif msg1 == b'rm':

	elif msg1 == b'makedir':






	elif msg1 == b'sair':
		cliente.send(msg1)
		break

cliente.close()
