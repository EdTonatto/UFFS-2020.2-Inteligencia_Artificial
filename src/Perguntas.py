from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Voce esta sentindo febre?', 'febre'],
		['Voce esta sentindo calafrios?','calafrio'],
		['Voce esta sentindo dor de cabeca?','dorcabeca'],
		['Voce esta sentindo dor de garganta?','dorgarganta'],
		['Voce esta sentindo dor muscular?','dormuscular'],
		['Voce tem sentindo perda de apetite?','faltaapetite'],	
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
