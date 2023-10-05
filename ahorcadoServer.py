
import socket
from juegoAhorcado import *

def main():
	HOST = '127.0.0.1'
	PORT = 7199
	MAX_REQ = 4
	conn = 0

	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	serverSocket.bind((HOST,PORT))
	serverSocket.listen(MAX_REQ)

	print("Servidor escuchando en: localhost en el port: ", PORT)
	(welcomeMessage,un_ahorcado,palabra) = inicializaAhorcado()

	while(conn < 4):
		if conn == 0:
			(clientSocket, address) = serverSocket.accept()
		elif conn == 1:
			(clientSocket2, address) = serverSocket.accept()
		elif conn == 2:
			(clientSocket3, address) = serverSocket.accept()
		else:
			(clientSocket4, address) = serverSocket.accept()			
		conn += 1

		print("Nuevo cliente conectado ", address)
	
	try:
		res = clientSocket.recv(2048)
		res2 = clientSocket2.recv(2048)
		res3 = clientSocket3.recv(2048)
		res4 = clientSocket4.recv(2048)

		clientSocket.sendall(bytes(welcomeMessage,'utf-8'))
		clientSocket2.sendall(bytes(welcomeMessage,'utf-8'))
		clientSocket3.sendall(bytes(welcomeMessage,'utf-8'))
		clientSocket4.sendall(bytes(welcomeMessage,'utf-8'))

		res = clientSocket.recv(2048)
		res2 = clientSocket2.recv(2048)
		res3 = clientSocket3.recv(2048)
		res4 = clientSocket4.recv(2048)
	except BrokenPipeError:
		serverSocket.close()
	else:
		turn = 0
		mensaje_usuario = ""

		while(1):

			if turn % 4 == 0:
				clientSocket.sendall(bytes("enTurno",'utf-8'))
				clientSocket2.sendall(bytes("espera",'utf-8'))
				clientSocket3.sendall(bytes("espera",'utf-8'))
				clientSocket4.sendall(bytes("espera",'utf-8'))

				res = clientSocket.recv(2048)
				clientSocket2.recv(2048)
				clientSocket3.recv(2048)
				clientSocket4.recv(2048)

				if res.decode("utf-8") == "/q":
					clientSocket2.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket3.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket4.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					res = clientSocket2.recv(2048)
					break
			elif turn % 3 == 0:
				clientSocket.sendall(bytes("espera",'utf-8'))
				clientSocket2.sendall(bytes("enTurno",'utf-8'))
				clientSocket3.sendall(bytes("espera",'utf-8'))
				clientSocket4.sendall(bytes("espera",'utf-8'))

				res = clientSocket2.recv(2048)
				clientSocket.recv(2048)
				clientSocket3.recv(2048)
				clientSocket4.recv(2048)

				if res.decode("utf-8") == "/q":
					clientSocket.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket3.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket4.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					res = clientSocket.recv(2048)
					break
			
			elif turn % 2 == 0:
				clientSocket.sendall(bytes("espera",'utf-8'))
				clientSocket2.sendall(bytes("espera",'utf-8'))
				clientSocket3.sendall(bytes("enTurno",'utf-8'))
				clientSocket4.sendall(bytes("espera",'utf-8'))

				res = clientSocket3.recv(2048)
				clientSocket.recv(2048)
				clientSocket2.recv(2048)
				clientSocket4.recv(2048)

				if res.decode("utf-8") == "/q":
					clientSocket.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket2.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket4.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					res = clientSocket.recv(2048)
					break
			
			else:
				clientSocket.sendall(bytes("espera",'utf-8'))
				clientSocket2.sendall(bytes("espera",'utf-8'))
				clientSocket3.sendall(bytes("espera",'utf-8'))
				clientSocket4.sendall(bytes("enTurno",'utf-8'))

				res = clientSocket4.recv(2048)
				clientSocket.recv(2048)
				clientSocket2.recv(2048)
				clientSocket3.recv(2048)

				if res.decode("utf-8") == "/q":
					clientSocket.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket2.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					clientSocket3.sendall(bytes("Un jugador salió del juego, juego terminado",'utf-8'))
					res = clientSocket.recv(2048)
					break

			if jugarAhorcado(res.decode("utf-8"),palabra,un_ahorcado):
				mensaje_usuario = "\nBien Hecho!!!!\nEl intento fue: " + res.decode("utf-8") + "\n\nPalabra secreta: " + un_ahorcado.estaResuelto()

				if un_ahorcado.esJuegoFinalizado():
					mensaje_usuario = "\n*********!!!!********\nGanaste evitaste que fuera ahorcado!!\nLa palabra secreta era: " + palabra + "\n\n"
					clientSocket.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket2.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket3.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket4.sendall(bytes(mensaje_usuario,'utf-8'))
					break
			else:
				if un_ahorcado.obtenNivelAhorcado() < 6:
					mensaje_usuario = "\nNo se encuentra esa letra en la palabra!!!\n" + un_ahorcado.obtenAhorcado() + "\n\nEl intento fue: " + res.decode("utf-8") + "\n\nLa palabra secreta es: " + un_ahorcado.estaResuelto()
				else:
					mensaje_usuario = un_ahorcado.obtenAhorcado() + "\n\nEl intento fue: " + res.decode("utf-8") + "\n\nOh no! El amigo ha sido ahorcado...\n\nLa palabra secreta era: " + palabra + "\n"
					clientSocket.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket2.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket3.sendall(bytes(mensaje_usuario,'utf-8'))
					clientSocket4.sendall(bytes(mensaje_usuario,'utf-8'))
					break

			clientSocket.sendall(bytes(mensaje_usuario,'utf-8'))
			clientSocket2.sendall(bytes(mensaje_usuario,'utf-8'))
			clientSocket3.sendall(bytes(mensaje_usuario,'utf-8'))
			clientSocket4.sendall(bytes(mensaje_usuario,'utf-8'))

			clientSocket.recv(2048)
			clientSocket2.recv(2048)
			clientSocket3.recv(2048)
			clientSocket4.recv(2048)

			turn += 1

		serverSocket.close()
	
if __name__ == "__main__":
	main()