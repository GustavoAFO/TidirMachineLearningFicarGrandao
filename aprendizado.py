#!/usr/bin/env python
# coding: utf-8

# # Primeiro projeto de classificador
#Passo 1: Leia os dados do arquivo TopEsp_AprendizadoSupervisionado_Credito.csv
# Historico (0 - Negativo / 1 - Desconhecido / 2 - Positivo)
# Endividamento: (0 - menor que 30% / 1 - maior que 30 %)
# Garantias (0 - Não / 1 - Sim )
# FaixadeValor (0 - menor que 15k / 1 - entre 15k e 35k / 2 - maior que 35k)
# In[5]:


import pandas as pd
from pandas import DataFrame
# lendo o arquivo
data = pd.read_csv('teste.csv',',')
# visualizando os dados
df = DataFrame(data)

df.head(100)


# Passo 2: Treine seu classificador

# In[6]:


from sklearn.naive_bayes import MultinomialNB


# define qual a saida correta para cada registro
features = df[['idade','altura','peso','hipertrofia','lentes_contato','alergia',
'tabagismo','bebida_alcoolica','medicamento','epilepsia','convulsoes','doenca',
'cirurgia_plastica','cortes','abrasoes','inchacos','Ombro','Torax','Cintura',
'Quadris','Pescoco','Biceps','Antebraco','Peito','Coxas','Panturrilha','imc']].values
# define qual a saida correta para cada registro
saidas = df['ex1-nome'].values
# cria o classificador
classifier = MultinomialNB()
# realiza o treinamento do classificador
classifier.fit(features, saidas)

# Passo 3: teste o classificador com um novo dado

# In[9]:


# Historico (0 - Negativo / 1 - Desconhecido / 2 - Positivo)
# Endividamento: (0 - menor que 30% / 1 - maior que 30 %)
# Garantias (0 - Não / 1 - Sim )
# FaixadeValor (0 - menor que 15k / 1 - entre 15k e 35k / 2 - maior que 35k)

idade= 21
altura= 1.72
peso= 70
hipertrofia= 1
lentes_contato= 0
alergia= 0
tabagismo= 0
bebida_alcoolica= 0
medicamento= 1
epilepsia= 0
convulsoes= 0
doenca= 0
cirurgia_plastica= 0
cortes= 1
abrasoes= 0
inchacos= 0
Ombro= 13.71
Torax= 104.29
Cintura= 109.68
Quadris= 108.69
Pescoco= 38.76
Biceps= 44.7
Antebraco= 30.69
Peito= 115.13
Coxas= 54.69
Panturrilha= 44.88
imc = 26.89
status_imc = 1



# nomes das colunas
novocontrato = [[idade,altura,peso,hipertrofia,lentes_contato,alergia,
tabagismo,bebida_alcoolica,medicamento,epilepsia,convulsoes,doenca,
cirurgia_plastica,cortes,abrasoes,inchacos,Ombro,Torax,Cintura,Quadris,
Pescoco,Biceps,Antebraco,Peito,Coxas,Panturrilha,imc]]

predictions = classifier.predict(novocontrato)

print(predictions)
# if predictions[0] == 0:
#     print("Dar o crédito")
# else:
#     print("Não dar o crédito")


# Desafio: Agora que o modelo está treinado vamos verificar se ele funciona mesmo. 
# 1) Leia o arquivo "TopEsp_AprendizadoSupervisionado_BasedeTeste.csv"
# 2) Como no passo 2 separe as colunas da saída
# 3) rode o comando classifier.predict para cada um dos dados da base de teste
# 4) Verifique se o seu classificador acertou comparando a saida predictions[0] com a saida dos dados




