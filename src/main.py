from Diagnostico import *
from Perguntas import *

#Inferência
diagnostico = Diagnostico()
pergunta = Pergunta()


while diagnostico.probabilidade() != 100:
	string = pergunta.texto()
	diagnostico.pergunta(string[0],string[1])
	print('probabilidade é %d' %(diagnostico.probabilidade()))
	print(diagnostico.resultado)
	if diagnostico.probabilidade() == 100:
		print('Voce esta: ',diagnostico.resultado[0])
