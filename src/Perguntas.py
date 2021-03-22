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

		['Voce esta sentindo cansaco frequentemente?','cansaco'],
		['Voce tem sentido dificuldade para respirar?','faltaar'],
		['Voce tem sentido dor no peito?','dorpeito'],
		['Voce tem tido tosse seca?','tosseseca'],
		['Voce tem tido tosse com sangue?','tossesangue'],
		['Voce tem soado durante a noite?','suornoite'],

		['Voce tem apresentado manchas vermelhas na pele?','manchasvermelhascorpo'],
		['Voce tem apresentado manchas brancas no interior da boca?','manchasbrancasboca'],
		['Voce esta com conjuntivite ou vermelhidao nos olhos?','conjuntivite'],

		['Voce tem sentido sensibilidade a luz?','sensluz'],
		['Voce tem sentido nauseas?','nausea'],
		['Voce tem sentido aumento no batimento cardiaco ou palpitacoes?','palpitacoes'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
