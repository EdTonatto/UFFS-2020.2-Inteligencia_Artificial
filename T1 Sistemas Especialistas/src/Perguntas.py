from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Voce esta sentindo febre?', 'febre'],
		['Voce esta sentindo dor muscular?','dormuscular'],
		['Voce esta sentindo dor de cabeca?','dorcabeca'],
		['Voce esta sentindo dor de garganta?','dorgarganta'],
		['Voce esta sentindo calafrios?','calafrio'],
		['Voce tem sentindo perda de apetite?','faltaapetite'],	
		['Voce tem tido tosse seca?','tosseseca'],
		['Voce esta apresentando coriza?','coriza'],
		['Voce esta com dificuldade para respirar?','difrespirar'],
		['Voce tem sentido cansaco frequentemente?','cansaco'],
		['Voce tem apresentado disturbios gastrintestinais (nauseas/vomitos/diarreia)','gastrintestinais'],
		['Voce apresenta alteracao no paladar?','altpaladar'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
