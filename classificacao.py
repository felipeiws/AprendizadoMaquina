from sklearn.naive_bayes import MultinomialNB

#Declarar e ensinar a maquina
#Eh gordinho? Tem perna curta? Faz au au?
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]
#Listo os dados
dados = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
#Digo o que cada dado e 1 = porco e -1 = cachorro
marcacoes = [1,1,1,-1,-1,-1]
#Estanciando
modelo = MultinomialNB()
#Treinamento
modelo.fit(dados,marcacoes)
#Dados para teste
misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]
teste = [misterioso1,misterioso2,misterioso3]
#Marcacao para teste
marcacao_teste = [-1,1,1]
#Previsao
previsao = modelo.predict(teste)
for x in previsao:
	if x == 1:
		print('Porco')
	elif x == -1:
		print('Cachorro')
#Verificar se errou
erros = previsao - marcacao_teste
acertos = [y for y in erros if y==0]
total_acertos = len(acertos)
total_testes  = len(teste)
taxa_acerto = 100.0 * total_acertos/total_testes
print(taxa_acerto)