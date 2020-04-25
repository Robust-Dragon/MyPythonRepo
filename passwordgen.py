from random import choice
import json

def salvarSenha(senha):
	nome = input("Nome do arquivo: ")
	tipo = input("json ou txt ?: ")
	
	nome = nome.replace(" ","")
	tipo = tipo.replace(" ","")
	
	if tipo == "json":
		senha = "{'nome':'" + nome + "','senha':'" + senha + "'}"
		
		senha = json.dumps(senha)
		
		with open("/storage/sdcard0/" + nome + "." + tipo,"w") as f:
			f.write(senha)
			f.close
			
	elif tipo == "txt":
		with open("/storage/sdcard0/" + nome + "." + tipo,"w") as f:
			f.write(senha)
			f.close



def gerarSenha(tamanho,tipo):
	tamanho = tamanho.replace(" ","")
	tipo = tipo.replace(" ","")
	senha = ""
	
	caracteres = ""
	if tipo == "numerico":
		caracteres = "1234567890"
		
	elif tipo == "texto":
		caracteres = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
		
	elif tipo == "textoupper":
		caracteres = "QWERTYUIOPASDFGHJKLZXCVBNM"
		
	elif tipo == "textolower":
		caracteres = "qwertyuiopasdfghjklzxcvbnm"
		
	elif tipo == "complexo":
		caracteres = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm#$&_-?@()=+!':%/\",.~[]{}<>;"
		
	elif tipo == "normal" or " ":
		caracteres = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
		
	else:
		print("Tipo não definido!")
		gerarSenha(input("Tamanho: "),input("Tipo: "))
		
	for caractere in range(int(tamanho)):
		senha += choice(caracteres)
		
	return senha
	
def painel():
	senha = gerarSenha(input("Tamanho: "),input("Tipo: "))
	print(senha)
	
	save = input("Salvar senha?(s ou n): ")
	save = save.replace(" ","")
	
	if save == "s":
		salvarSenha(senha)
		
	elif save == "n":
		exit
		
	else:
		print("Essa opção não esta definida!")
		painel()
		
painel()
