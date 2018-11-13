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
from tkinter import *




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



class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.segundoSubtitulo = Frame(master)
        self.segundoSubtitulo["pady"] = 10
        self.segundoSubtitulo.pack()

        self.medidas1Container = Frame(master)
        self.medidas1Container["padx"] = 120
        self.medidas1Container["pady"] = 5
        self.medidas1Container.pack(fill=X)

        self.medidas2Container = Frame(master)
        self.medidas2Container["padx"] = 120
        self.medidas2Container["pady"] = 5
        self.medidas2Container.pack(fill=X)

        self.medidas3Container = Frame(master)
        self.medidas3Container["padx"] = 120
        self.medidas3Container["pady"] = 5
        self.medidas3Container.pack(fill=X)

        self.medidas4Container = Frame(master)
        self.medidas4Container["padx"] = 120
        self.medidas4Container["pady"] = 5
        self.medidas4Container.pack(fill=X)

        self.medidas5Container = Frame(master)
        self.medidas5Container["padx"] = 120
        self.medidas5Container["pady"] = 5
        self.medidas5Container.pack(fill=X)


        self.primeiroSubtitulo = Frame(master)
        self.primeiroSubtitulo["pady"] = 10
        self.primeiroSubtitulo.pack()

        


        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 120
        self.quintoContainer["pady"] = 5
        self.quintoContainer.pack(fill=X)

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 120
        self.sextoContainer["pady"] = 5
        self.sextoContainer.pack(fill=X)

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 120
        self.setimoContainer["pady"] = 5
        self.setimoContainer.pack(fill=X)


        self.oitavoContainer = Frame(master)
        self.oitavoContainer["padx"] = 120
        self.oitavoContainer["pady"] = 5
        self.oitavoContainer.pack(fill=X)

        self.nonoContainer = Frame(master)
        self.nonoContainer["padx"] = 120
        self.nonoContainer["pady"] = 5
        self.nonoContainer.pack(fill=X)


        self.decimoContainer = Frame(master)
        self.decimoContainer["padx"] = 120
        self.decimoContainer["pady"] = 5
        self.decimoContainer.pack(fill=X)


        self.especialContainer = Frame(master)
        self.especialContainer["padx"] = 70
        self.especialContainer["pady"] = 5
        self.especialContainer.pack(fill=X)
  
        # self.terceiroContainer = Frame(master)
        # self.terceiroContainer["padx"] = 20
        # self.segundoContainer["pady"] = 30
        # self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.idadeLabel = Label(self.segundoContainer, text="Idade", font=self.fontePadrao)
        self.idadeLabel.pack(padx=(15,0),side=LEFT)
  
        self.idade = Entry(self.segundoContainer)
        self.idade["width"] = 30
        self.idade["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.idade.pack(side=LEFT)

        ## A PARTIR DAQUI NAO SEI DE NADA 

        self.alturaLabel = Label(self.terceiroContainer, text="Altura", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)
  
        def callbackaltura(self,altura):
            teste = self.altura.get()
            self.altura.delete(0,END)
            self.altura.insert(0,teste.replace(",","."))
            if(self.peso.get()):
               
                #self.imc.config(state="normal")
               
                altura = float(self.altura.get())
                peso2 =   float(self.peso.get())

                try:
                    imc_calc = peso2/altura**2
                except Exception as exe:
                    pass
               
                imc_calc = float("{:.2f}".format(imc_calc))
                
                # self.imc.delete(0,END)
                # self.imc.insert(0,imc_calc)
                # self.imc.config(state="disabled")
                self.imcValueLabel["text"] = imc_calc

        altura = StringVar()
        altura.trace("w", lambda name, index, mode, altura=altura: callbackaltura(self,altura))

        self.altura = Entry(self.terceiroContainer, textvariable=altura)
        self.altura["width"] = 30
        self.altura["font"] = self.fontePadrao
        #self.altura["show"] = "*"
        self.altura.pack(side=LEFT)


        self.pesoLabel = Label(self.terceiroContainer, text="Peso", font=self.fontePadrao)
        self.pesoLabel.pack(padx=(15,0),side=LEFT)
        
        def callbackpeso(self,peso):
            teste = self.peso.get()
            self.peso.delete(0,END)
            self.peso.insert(0,teste.replace(",","."))
            if(self.altura.get()):
               
                # self.imc.config(state="normal")
               
                altura = float(self.altura.get())
                peso2 =   float(self.peso.get())

                try:
                    imc_calc = peso2/altura**2
                except Exception as exe:
                    pass
                
                imc_calc = float("{:.2f}".format(imc_calc))
                
                # self.imc.delete(0,END)
                # self.imc.insert(0,imc_calc)
                # self.imc.config(state="disabled")
                self.imcValueLabel["text"] = imc_calc
       

        peso = StringVar()
        peso.trace("w", lambda name, index, mode, peso=peso: callbackpeso(self,peso))

       


        self.peso = Entry(self.terceiroContainer, textvariable=peso)
        self.peso["width"] = 30
        self.peso["font"] = self.fontePadrao
        #self.peso["show"] = "*"
        self.peso.pack(side=LEFT)


        ###############################################################################
        #MEDIDAS CORPORAIS
        self.titulo = Label(self.segundoSubtitulo, text="Medidas corporais")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()


        self.ombroLabel = Label(self.medidas1Container,text="Ombros", font=self.fontePadrao)
        self.ombroLabel.pack(side=LEFT)
  
        self.ombro = Entry(self.medidas1Container)
        self.ombro["width"] = 30
        self.ombro["font"] = self.fontePadrao
        self.ombro.pack(padx=(15,0),side=LEFT)
  
        self.toraxLabel = Label(self.medidas1Container, text="Torax", font=self.fontePadrao)
        self.toraxLabel.pack(padx=(15,0),side=LEFT)
  
        self.torax = Entry(self.medidas1Container)
        self.torax["width"] = 30
        self.torax["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.torax.pack(padx=(35,0),side=LEFT)

        ##


        self.cinturaLabel = Label(self.medidas2Container,text="Cintura", font=self.fontePadrao)
        self.cinturaLabel.pack(side=LEFT)
  
        self.cintura = Entry(self.medidas2Container)
        self.cintura["width"] = 30
        self.cintura["font"] = self.fontePadrao
        self.cintura.pack(padx=(20,0),side=LEFT)
  
        self.quadrisLabel = Label(self.medidas2Container, text="Quadris", font=self.fontePadrao)
        self.quadrisLabel.pack(padx=(15,0),side=LEFT)
  
        self.quadris = Entry(self.medidas2Container)
        self.quadris["width"] = 30
        self.quadris["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.quadris.pack(padx=(25,0),side=LEFT)


        ##


        self.pescocoLabel = Label(self.medidas3Container,text="Pescoço", font=self.fontePadrao)
        self.pescocoLabel.pack(side=LEFT)
  
        self.pescoco = Entry(self.medidas3Container)
        self.pescoco["width"] = 30
        self.pescoco["font"] = self.fontePadrao
        self.pescoco.pack(padx=(10,0),side=LEFT)
  
        self.bicepsLabel = Label(self.medidas3Container, text="Biceps", font=self.fontePadrao)
        self.bicepsLabel.pack(padx=(15,0),side=LEFT)
  
        self.biceps = Entry(self.medidas3Container)
        self.biceps["width"] = 30
        self.biceps["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.biceps.pack(padx=(30,0),side=LEFT)



        ##


        self.antebracoLabel = Label(self.medidas4Container,text="Antebraço", font=self.fontePadrao)
        self.antebracoLabel.pack(side=LEFT)
  
        self.antebraco = Entry(self.medidas4Container)
        self.antebraco["width"] = 30
        self.antebraco["font"] = self.fontePadrao
        self.antebraco.pack(padx=(2,0),side=LEFT)
  
        self.peitoLabel = Label(self.medidas4Container, text="Peito", font=self.fontePadrao)
        self.peitoLabel.pack(padx=(15,0),side=LEFT)
  
        self.peito = Entry(self.medidas4Container)
        self.peito["width"] = 30
        self.peito["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.peito.pack(padx=(40,0),side=LEFT)



        ##


        self.coxasLabel = Label(self.medidas5Container,text="Coxas", font=self.fontePadrao)
        self.coxasLabel.pack(side=LEFT)
  
        self.coxas = Entry(self.medidas5Container)
        self.coxas["width"] = 30
        self.coxas["font"] = self.fontePadrao
        self.coxas.pack(padx=(25,0),side=LEFT)
  
        self.panturrilhasLabel = Label(self.medidas5Container, text="Panturrilhas", font=self.fontePadrao)
        self.panturrilhasLabel.pack(padx=(15,0),side=LEFT)
  
        self.panturrilhas = Entry(self.medidas5Container)
        self.panturrilhas["width"] = 30
        self.panturrilhas["font"] = self.fontePadrao
        #self.idade["show"] = "*"
        self.panturrilhas.pack(side=LEFT)


        ##############################################################################

        self.titulo = Label(self.primeiroSubtitulo, text="Amnase")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()


        self.lentesLabel = Label(self.quintoContainer, text="Usa Lentes de contato? ", font=self.fontePadrao)
        self.lentesLabel.pack(side=LEFT)

        self.lentes = IntVar()
        Radiobutton(self.quintoContainer, text="Sim", variable=self.lentes, value=1).pack(side=LEFT)
        Radiobutton(self.quintoContainer, text="Não", variable=self.lentes, value=0).pack(side=LEFT)

        self.alergiaLabel = Label(self.quintoContainer, text="Possui alguma alergia?", font=self.fontePadrao)
        self.alergiaLabel.pack(padx=(55,0),side=LEFT)

        self.alergia = IntVar()
        Radiobutton(self.quintoContainer, text="Sim", variable=self.alergia, value=1).pack(side=LEFT)
        Radiobutton(self.quintoContainer, text="Não", variable=self.alergia, value=0).pack(side=LEFT)



        self.tabagistaLabel = Label(self.sextoContainer, text="É Tabagista?", font=self.fontePadrao)
        self.tabagistaLabel.pack(side=LEFT)

        self.tabagista = IntVar()
        Radiobutton(self.sextoContainer, text="Sim", variable=self.tabagista, value=1).pack(side=LEFT)
        Radiobutton(self.sextoContainer, text="Não", variable=self.tabagista, value=0).pack(side=LEFT)



        self.bebidasLabel = Label(self.sextoContainer, text="Ingere bebidas alcoólicas?", font=self.fontePadrao)
        self.bebidasLabel.pack(padx=(120,0),side=LEFT)

        self.bebidas = IntVar()
        Radiobutton(self.sextoContainer, text="Sim", variable=self.bebidas, value=1).pack(side=LEFT)
        Radiobutton(self.sextoContainer, text="Não", variable=self.bebidas, value=0).pack(side=LEFT)
       



        self.medicamentosLabel = Label(self.setimoContainer, text="Faz uso de medicamentos?", font=self.fontePadrao)
        self.medicamentosLabel.pack(side=LEFT)

        self.medicamentos = IntVar()
        Radiobutton(self.setimoContainer, text="Sim", variable=self.medicamentos, value=1).pack(side=LEFT)
        Radiobutton(self.setimoContainer, text="Não", variable=self.medicamentos, value=0).pack(side=LEFT)




        self.eplLabel = Label(self.setimoContainer, text="Já teve epilepsia?", font=self.fontePadrao)
        self.eplLabel.pack(padx=(35,0),side=LEFT)

        self.epilepsia = IntVar()
        Radiobutton(self.setimoContainer, text="Sim", variable=self.epilepsia, value=1).pack(side=LEFT)
        Radiobutton(self.setimoContainer, text="Não", variable=self.epilepsia, value=0).pack(side=LEFT)


        self.convLabel = Label(self.oitavoContainer, text="Já teve convulsões?", font=self.fontePadrao)
        self.convLabel.pack(side=LEFT)

        self.convulsao = IntVar()
        Radiobutton(self.oitavoContainer, text="Sim", variable=self.convulsao, value=1).pack(side=LEFT)
        Radiobutton(self.oitavoContainer, text="Não", variable=self.convulsao, value=0).pack(side=LEFT)


        self.doencLabel = Label(self.oitavoContainer, text="Possui alguma doença?", font=self.fontePadrao)
        self.doencLabel.pack(padx=(75,0),side=LEFT)

        self.doenca = IntVar()
        Radiobutton(self.oitavoContainer, text="Sim", variable=self.doenca, value=1).pack(side=LEFT)
        Radiobutton(self.oitavoContainer, text="Não", variable=self.doenca, value=0).pack(side=LEFT)



        self.cirurgiaPlasticaLabel = Label(self.nonoContainer, text="Já fez alguma cirurgia?", font=self.fontePadrao)
        self.cirurgiaPlasticaLabel.pack(side=LEFT)

        self.cirurgia = IntVar()
        Radiobutton(self.nonoContainer, text="Sim", variable=self.cirurgia, value=1).pack(side=LEFT)
        Radiobutton(self.nonoContainer, text="Não", variable=self.cirurgia, value=0).pack(side=LEFT)


        self.corteLabel = Label(self.nonoContainer, text="Possui algum corte?", font=self.fontePadrao)
        self.corteLabel.pack(padx=(60,0),side=LEFT)

        self.corte = IntVar()
        Radiobutton(self.nonoContainer, text="Sim", variable=self.corte, value=1).pack(side=LEFT)
        Radiobutton(self.nonoContainer, text="Não", variable=self.corte, value=0).pack(side=LEFT)





        self.abrasaoLabel = Label(self.decimoContainer, text="Possui alguma abrasão?", font=self.fontePadrao)
        self.abrasaoLabel.pack(side=LEFT)

        self.abrasao = IntVar()
        Radiobutton(self.decimoContainer, text="Sim", variable=self.abrasao, value=1).pack(side=LEFT)
        Radiobutton(self.decimoContainer, text="Não", variable=self.abrasao, value=0).pack(side=LEFT)

        self.inchacoLabel = Label(self.decimoContainer, text="Possui algum inchaço?", font=self.fontePadrao)
        self.inchacoLabel.pack(padx=(50,0),side=LEFT)

        self.inchaco = IntVar()
        Radiobutton(self.decimoContainer, text="Sim", variable=self.inchaco, value=1).pack(side=LEFT)
        Radiobutton(self.decimoContainer, text="Não", variable=self.inchaco, value=0).pack(side=LEFT)


        self.hiperLabel = Label(self.especialContainer, text="Possui como objetivo 'Hipertrofia'?", font=self.fontePadrao)
        self.hiperLabel.pack(padx=(50,0),side=LEFT)

        self.hipertrofia = IntVar()
        Radiobutton(self.especialContainer, text="Sim", variable=self.hipertrofia, value=1).pack(side=LEFT)
        Radiobutton(self.especialContainer, text="Não", variable=self.hipertrofia, value=0).pack(side=LEFT)

        self.imcLabel = Label(self.especialContainer,text="IMC", font=self.fontePadrao)
        self.imcLabel.pack(padx=(100,0),side=LEFT)

        self.imcValueLabel = Label(self.especialContainer,text="-", font=self.fontePadrao)
        self.imcValueLabel.pack(side=LEFT)
  
        # self.imc = Entry(self.especialContainer,state="disabled")
        # self.imc["width"] = 10
        # self.imc["font"] = self.fontePadrao
        # self.imc.pack(side=LEFT)


        ## VOLTEI A SABER

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Gerar Ficha"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.gerarFicha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método gerar ficha
    def gerarFicha(self):

       
        

        if (self.nome.get() and
        self.idade.get() and
        self.altura.get() and
        self.peso.get() and
        self.ombro.get() and
        self.torax.get() and
        self.cintura.get() and
        self.quadris.get() and
        self.pescoco.get() and
        self.biceps.get() and
        self.antebraco.get() and
        self.peito.get() and
        self.coxas.get() and
        self.panturrilhas.get()
        # self.lentes.get() and 
        # self.alergia.get() and 
        # self.tabagista.get() and 
        # self.bebidas.get() and
        # self.medicamentos.get() and 
        # self.epilepsia.get() and
        # self.convulsao.get() and
        # self.doenca.get() and
        # self.cirurgia.get() and
        # self.corte.get() and 
        # self.abrasao.get() and
        # self.inchaco.get() and
        #self.hipertrofia.get()
        ):
            self.mensagem["text"] = ""

            imc = float(self.imcValueLabel["text"])
            print("[Calculo de IMC] %s"%imc)
           
            # print("TESTE")
            # print(self.corte.get())

            #Classificador
            lista_saidas = ['ex1-nome','ex2-nome','ex3-nome','ex4-nome','ex5-nome',
            'ex6-nome','ex7-nome','ex8-nome','ex9-nome','ex10-nome','ex11-nome','ex12-nome','ex13-nome','ex14-nome','ex15-nome']
            exercicios = []
            for x in range(15):
                saidas = df[lista_saidas[x]]
                classifier = MultinomialNB()
                classifier.fit(entrada.values, saidas.values)
                entrada_do_classificador = [[int(self.idade.get()),float(self.altura.get()),float(self.peso.get()),int( self.hipertrofia.get()),int(self.lentes.get()),int(self.alergia.get()),int(
                self.tabagista.get()),int(self.bebidas.get()),int(self.medicamentos.get()),int(self.epilepsia.get()),int(self.convulsao.get()),int(self.doenca.get()),int(
                self.cirurgia.get()),int(self.corte.get()),int(self.abrasao.get()),int(self.inchaco.get()),float(self.ombro.get()),float(self.torax.get()),float(self.cintura.get()),float(self.quadris.get()),float(
                self.pescoco.get()),float(self.biceps.get()),float(self.antebraco.get()),float(self.peito.get()),float(self.coxas.get()),float(self.panturrilhas.get()),float(imc)]]
                
                #print(entrada_do_classificador)
                exercicios.append(classifier.predict(entrada_do_classificador)[0])
                #exercicios.append((entrada_do_classificador)[0])

            print(c.BOLD+"\n\nFicha:\nExercicios:"+c.FAIL)
            x=0
            for exercicio in exercicios:
                x+=1
                print("["+str(x)+"]"+exercicio)
            print("-----------------------"+c.ENDC)
            #print(exercicios)  
        else:
            self.mensagem["text"] = "Preencha os campos"
            print('input required') 
       
       

root = Tk()
root.title("Sistema de evolução continua em processamento de fichas de musculação baseado em machine learning")
root.resizable(False,False)
root.geometry("800x650")
Application(root)
root.mainloop()



