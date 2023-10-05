from colgados import COLGADOS


class Ahorcado:

	def __init__(self, nivelAhorcado, palabraRandom):
		self.nivelAhorcado = nivelAhorcado
		self.resuleto = '-' * len(palabraRandom)

	def incrementaNivelAhorcado(self):
		self.nivelAhorcado += 1

	def obtenNivelAhorcado(self):
		return self.nivelAhorcado

	def estaResuelto(self):
		return self.resuleto

	def obtenAhorcado(self):
	
		un_ahorcado = COLGADOS[self.nivelAhorcado]
		print(self.nivelAhorcado)
		return un_ahorcado

	def resuelvePalabra(self,letra,palabra):

		arr = list(self.resuleto)
		arrStr = ""
		for i in range(0,len(palabra)):
			if letra == palabra[i]:
				if arr[i] == '-':
					arr[i] = letra

		self.resuleto = arrStr.join(arr)

	def esJuegoFinalizado(self):
		return "-" not in self.resuleto