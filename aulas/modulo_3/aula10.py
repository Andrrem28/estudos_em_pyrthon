'''
method vs @classmethod vs @staticmethod
method - sel, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático (X self, X cls) (X = sem uso)
'''

class Connection:
	def __init__(self, host = 'localhost'):
		self.host = host
		self.user = None
		self.password = None

	def set_user(self, user):
		self.user = user

	def set_password(self, password):
		self.password = password

	@classmethod
	def auth_user(cls, user, password):
		connection = cls()
		connection.user = user
		connection.password = password
		return connection

	@staticmethod
	def log(msg):
		return msg


c1 = Connection.auth_user('Barquinhos', 123)
print(c1.user, c1.password)

print(Connection.log('Mensagem para o Log'))
# c1.user = 'Barquinhos'
# c1.password = 123

# print(c1.user, c1.password)