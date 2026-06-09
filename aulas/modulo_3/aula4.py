# Mantendo estados dentro da classe
class Camera:
	def __init__(self, nome, filmando = False):
		self.nome = nome
		self.filmando = filmando

	def filmar(self):
		self.verifica_camera()

		print(f'{self.nome} está filmando.')
		self.filmando = True

	def para_filmagem(self):
		self.verifica_camera()

		print(f'{self.nome} está parando de filmar.')
		self.filmando = False

	def fotografar(self):
		if self.filmando:
			print(f'{self.nome} não pode tirar fotos.')
			return

		print(f'{self.nome} está fotografando...')

	def verifica_camera(self):
		if self.filmando:
			print(f'{self.nome} já está filmando.')
			return

		if not self.filmando:
			print(f'{self.nome} não está filmando.')
			return


c1 = Camera('Sony')
c2 = Camera('Cannon')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmagem()
c1.fotografar()