#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Documentação
   1 - Instalação das dependências
    pip install -r requirements.txt
   2 - Execução do programa
   python main.py
"""

__author__  = "Gustavo Afonso de Oliveira, xxx , xxx"
__email__   = "gustavoafonso.gu@gmail.com"
__version__ = "0.1"

import sys
import pandas as pd
from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from utils import CalculadoraMedidas
from utils import cores


c = cores()
def title():
    print(c.OKGREEN+c.BOLD+"""
  _______ _____ _____ _____ _____                                                  
 |__   __|_   _|  __ \_   _|  __ \                                                 
    | |    | | | |  | || | | |__) |                                                
    | |    | | | |  | || | |  _  /                                                 
    | |   _| |_| |__| || |_| | \ \                                                 
  __|_|_ |_____|_____/_____|_|  \_\      _                           _             
 |  \/  |          | |   (_)            | |                         (_)            
 | \  / | __ _  ___| |__  _ _ __   ___  | |     ___  __ _ _ __ _ __  _ _ __   __ _ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ | |    / _ \/ _` | '__| '_ \| | '_ \ / _` |
 | |  | | (_| | (__| | | | | | | |  __/ | |___|  __/ (_| | |  | | | | | | | | (_| |
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___| |______\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ 
                                                                                """+c.ENDC)
if __name__ == '__main__':
    #Verifica se esta rodando no python3
    if sys.version_info < (3,0):
        print("Desculpe, é nessesário Python 3.x para rodar")
        sys.exit(1)
    try:
        data = pd.read_csv('banco.csv',',')
    except NameError as e:
        print("Erro - {0}".format(e))
    except Exception as e:
        print("Erro - {0}".format(e))
    title()
    
    df = DataFrame(data)
    print(c.BOLD+c.OKBLUE+'[*]Banco de dados utilizado:'+c.ENDC+'\n'+str(df))

    entrada = df[['idade','altura','peso','hipertrofia','lentes_contato','alergia',
    'tabagismo','bebida_alcoolica','medicamento','epilepsia','convulsoes','doenca',
    'cirurgia_plastica','cortes','abrasoes','inchacos','Ombro','Torax','Cintura',
    'Quadris','Pescoco','Biceps','Antebraco','Peito','Coxas','Panturrilha','imc']]

    print(c.BOLD+c.OKBLUE+'[*]Variaveis de entrada:'+c.ENDC+'\n'+str(entrada))

    print(c.BOLD+c.OKBLUE+'[*]Perguntas para o classificador'+c.ENDC)
    cm = CalculadoraMedidas()
    print(c.BOLD+c.OKBLUE+'[*]Informações básicas'+c.ENDC)
    resposta = input("[?]Qual a sua idade?")
    idade = int(resposta)
    resposta = input("[?]Qual a sua altura?\n(*casa decimal com \".\"")
    altura = float(resposta)
    resposta = input("[?]Qual é seu peso:")
    peso = int(resposta)
    print('[*]Informações amnase')
    resposta = input("[?]Hipertrofia:(s/n)")
    if 's' or 'S' in resposta:
        hipertrofia = 1
    else:
        hipertrofia = 0
    resposta = input("[?]Usa lentes de contato? (s/n)")
    if 's' or 'S' in resposta:
        lentes_contato = 1
    else:
        lentes_contato = 0
    resposta = input("[?]Possui alguma alergia? (s/n)")
    if 's' or 'S' in resposta:
        alergia = 1
    else:
        alergia = 0
    resposta = input("[?]É tabagista? (s/n)")
    if 's' or 'S' in resposta:
        tabagismo = 1
    else:
        tabagismo = 0
    resposta = input("[?]Ingere bebidas alcoolicas? (s/n)")
    if 's' or 'S' in resposta:
        bebida_alcoolica = 1
    else:
        bebida_alcoolica = 0
    resposta = input("[?]Faz uso de algum medicamento? (s/n)")
    if 's' or 'S' in resposta:
        medicamento = 1
    else:
        medicamento = 0
    resposta = input("[?]Já teve epilepsia? (s/n)")
    if 's' or 'S' in resposta:
        epilepsia = 1
    else:
        epilepsia = 0
    resposta = input("[?]Já teve convulções? (s/n)")
    if 's' or 'S' in resposta:
        convulsoes = 1
    else:
        convulsoes = 0
    resposta = input("[?]Possui alguma doença? (s/n)")
    if 's' or 'S' in resposta:
        doenca = 1
    else:
        doenca = 0
    resposta = input("[?]Já fez cirurgia plástica? (s/n)")
    if 's' or 'S' in resposta:
        cirurgia_plastica = 1
    else:
        cirurgia_plastica = 0
    resposta = input("[?]Possui algum corte no corpo? (s/n)")
    if 's' or 'S' in resposta:
        cortes = 1
    else:
        cortes = 0
    resposta = input("[?]Possui alguma abrasão? (s/n)")
    if 's' or 'S' in resposta:
        abrasoes = 1
    else:
        abrasoes = 0
    resposta = input("[?]Tem algum inchaço no corpo? (s/n)")
    if 's' or 'S' in resposta:
        inchacos = 1
    else:
        inchacos = 0
    print(c.BOLD+c.OKBLUE+'[*]Medidas corporais\n(*casa decimal com \".\"'+c.ENDC)
    resposta = input("[?]Qual a medida dos seus ombros?")
    Ombro = float(resposta)
    resposta = input("[?]Qual a medida do seu torax?")
    Torax = float(resposta)
    resposta = input("[?]Qual a medida da sua cintura?")
    Cintura = float(resposta)
    resposta = input("[?]Qual a medida dos seus quadris?")
    Quadris = float(resposta)
    resposta = input("[?]Qual a medida do seu pescoco?")
    Pescoco = float(resposta)
    resposta = input("[?]Qual a medida do seu biceps?")
    Biceps = float(resposta)
    resposta = input("[?]Qual a medida do seu antebraco?")
    Antebraco = float(resposta)
    resposta = input("[?]Qual a medida do seu peito?")
    Peito = float(resposta)
    resposta = input("[?]Qual a medida das suas coxas?")
    Coxas = float(resposta)
    resposta = input("[?]Qual a medida das suas panturrilhas?")
    Panturrilha = float(resposta)
    imc = cm.calculaIMC(peso,altura)
    print("[Calculo de IMC] %s"%cm.statusIMC(imc))

    #Classificador
    lista_saidas = ['ex1-nome','ex2-nome','ex3-nome','ex4-nome','ex5-nome',
    'ex6-nome','ex7-nome','ex8-nome','ex9-nome','ex10-nome']
    exercicios = []
    for x in range(10):
        saidas = df[lista_saidas[x]]
        classifier = MultinomialNB()
        classifier.fit(entrada.values, saidas.values)
        entrada_do_classificador = [[idade,altura,peso,hipertrofia,lentes_contato,alergia,
        tabagismo,bebida_alcoolica,medicamento,epilepsia,convulsoes,doenca,
        cirurgia_plastica,cortes,abrasoes,inchacos,Ombro,Torax,Cintura,Quadris,
        Pescoco,Biceps,Antebraco,Peito,Coxas,Panturrilha,imc]]
        exercicios.append(classifier.predict(entrada_do_classificador)[0])



    print(c.BOLD+"\n\nFicha:\nExercicios:"+c.FAIL)
    x=0
    for exercicio in exercicios:
        x+=1
        print("["+str(x)+"]"+exercicio)
    print("-----------------------"+c.ENDC)
   



    