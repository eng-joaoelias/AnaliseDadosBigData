import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

tabela = pd.read_csv("clientes.csv")

#print(tabela.info())

#tipo de credito: good(bom), standart (ok) ou ruim (bad)

#preparar a base de dados
#criar e treinar a IA: passar info do historico (informacoes em formato de numero)
#usar label encoder pra informacoes em texto-> transforma texto pra numero (profissao, mix_credito, comportamento_pagamento)

'''
como usar label encoder
#1. importar o label encoder: from sklearn.preprocessing import LabelEncoder
#2. criar o label encoder
#3. aplicar o label encoder
'''

codificador = LabelEncoder() #2

tabela["profissao"] = codificador.fit_transform(tabela["profissao"]) #3

tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"]) #3

tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"]) #3

'''
#fazer divisoes para aprendizado da ia: duas divisoes
quem eu quero prever (isso e o x, o resto da base de dados, as colunas que serao usada pra entrada)
que eu quero usar pra previsao (isso eh a saida y)
'''

y = tabela["score_credito"] #saida, o resultado a ser previsto
x = tabela.drop(columns=["score_credito", "id_cliente"]) #entrada, usados pra previsao. vou tirar score_credito, id do cliente e o nome. os dois ultimos n sao necessarios

'''
Agora, precisamos separar os dados em treinamento e teste
'''

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y) #separa os dados em treino e teste. eh o aprendizado de maquina. dps qe ela aprede com os dados de treino, botamos uma prova com os dados de teste

#criar a inteligencia artificial
#arvore de decisao random forest e knn (vizinhos proximos, nearest neighbors)

'''
3 passos 
importa a IA
cria a IA
treina a IA
'''

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

#treinar a IA (usamos os dois modelos, lembrando)
modelo_arvoredecisao.fit(x_teste, y_teste)
modelo_knn.fit(x_teste, y_teste)

#testar os modelos: queremos saber qual o melhor modelo
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

#calcular a acuracia: quanto ele acertou e quanto errou
#print(100*accuracy_score(y_teste, previsao_arvoredecisao)) #acuracia de 100%
#print(100*accuracy_score(y_teste, previsao_knn)) #acuracia de 75.74%

tabela_nova = pd.read_csv("novos_clientes.csv")

print(tabela_nova)

codificador = LabelEncoder() #2

tabela_nova["profissao"] = codificador.fit_transform(tabela_nova["profissao"]) #3

tabela_nova["mix_credito"] = codificador.fit_transform(tabela_nova["mix_credito"]) #3

tabela_nova["comportamento_pagamento"] = codificador.fit_transform(tabela_nova["comportamento_pagamento"]) #3

previsoes = modelo_arvoredecisao.predict(tabela_nova)
print(previsoes)
