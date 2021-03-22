from Diagnostico import *
from Perguntas import *

#Inferência
diagnostico = Diagnostico()
pergunta = Pergunta()


while diagnostico.probabilidade() != 100:
	string = pergunta.texto()
	diagnostico.pergunta(string[0],string[1])
	print('Probabilidade de %d' %(diagnostico.probabilidade()))
	print(diagnostico.resultado)
	if diagnostico.probabilidade() == 100:
		if diagnostico.resultado[0] == 'Saudavel':
			print('Voce esta: ', diagnostico.resultado[0])
		else:
			print('Voce pode estar com: ',diagnostico.resultado[0])
