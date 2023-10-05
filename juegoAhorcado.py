
import random
from ahorcado import *

def inicializaAhorcado():

	palabras = ['master','sistemas','socket','ahorcado','oso','carita']

	palabraRandom = palabras[random.randint(0,len(palabras)-1)]


	un_ahorcado = Ahorcado(0,palabraRandom)

	intro = "Intenta salvar al amigo de ser colgado adivinando la palabra"
	intro += "\n\n Escribe \\q para finalizar el juego...."
	intro += un_ahorcado.obtenAhorcado()

	return (intro,un_ahorcado,palabraRandom)

def jugarAhorcado(intento,palabra,un_ahorcado):

	if intento in palabra:
		un_ahorcado.resuelvePalabra(intento,palabra)
		return True
	else: # 
		un_ahorcado.incrementaNivelAhorcado()

	return False