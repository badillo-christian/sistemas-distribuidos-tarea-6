import socket

def main():
	HOST = '127.0.0.1'
	PORT = 7199
	messageOK= "ok"
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((HOST,PORT))

	print("Conectado a: ", "localhost", "en el port: ", PORT)
	print("Esperando por los otros jugadores...")

	clientSocket.sendall(bytes("play",'utf-8'))
	res = clientSocket.recv(2048)
	print(res.decode("utf-8"))
	clientSocket.sendall(bytes(messageOK,'utf-8'))

	while(1):
		try:
			res = clientSocket.recv(2048)
		except (BrokenPipeError,ConnectionResetError):
			break
		if res != b'':
			if res.decode("utf-8") == "espera":
				print("Esperando que otro jugador adivine...")
				message = messageOK
			elif res.decode("utf-8") == "enTurno":
				message = input("Introduce una letra: ")
			else:
				print(res.decode("utf-8"))
				message = messageOK
		try:
			clientSocket.sendall(bytes(message,'utf-8'))
		except (BrokenPipeError,ConnectionResetError,OSError):
			break

		if message == "/q":
			print("Juego Finalizado!")
			break
	clientSocket.close()		

if __name__ == "__main__":
	main()