#!/usr/bin/env python
# coding: utf-8




import pandas as pd
from pandas import DataFrame


data = pd.read_csv('teste.csv',',')

df = DataFrame(data)

df.head(100)





from sklearn.naive_bayes import MultinomialNB


features = df[['idade','altura','peso','hipertrofia','lentes_contato','alergia',
'tabagismo','bebida_alcoolica','medicamento','epilepsia','convulsoes','doenca',
'cirurgia_plastica','cortes','abrasoes','inchacos','Ombro','Torax','Cintura',
'Quadris','Pescoco','Biceps','Antebraco','Peito','Coxas','Panturrilha','imc']].values

saidas = df['ex1-nome'].values


classifier = MultinomialNB()


classifier.fit(features, saidas)


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



novocontrato = [[idade,altura,peso,hipertrofia,lentes_contato,alergia,
tabagismo,bebida_alcoolica,medicamento,epilepsia,convulsoes,doenca,
cirurgia_plastica,cortes,abrasoes,inchacos,Ombro,Torax,Cintura,Quadris,
Pescoco,Biceps,Antebraco,Peito,Coxas,Panturrilha,imc]]

predictions = classifier.predict(novocontrato)

print(predictions)



