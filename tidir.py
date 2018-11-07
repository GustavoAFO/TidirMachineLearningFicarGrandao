#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import csv


class GeradorExercicios:
    exercicios = [{'nome': 'Supino reto', 'categoria': 'peito'}, {'nome': 'Crucifixo inclinado', 'categoria': 'peito'},
                  {'nome': 'Crosshover', 'categoria': 'peito'}, {'nome': 'Tríceps pulley unilateral', 'categoria': 'triceps'},
                  {'nome': 'Cable crunch', 'categoria': 'abdominal'}, {'nome': 'Puxada frente polia alta', 'categoria': 'costas'},
                  {'nome': 'Remada articulada', 'categoria': 'costas'}, {'nome': 'Rosca direta', 'categoria': 'biceps'},{'nome': 'Rosca alternada', 'categoria': 'biceps'}, 
                  {'nome': 'Flexao lateral do tronco', 'categoria': 'abdominal'},{'nome': 'Puxada alta com braços estendidos', 'categoria': 'costas'}, 
                  {'nome': 'Abdominal com flexao de pernas', 'categoria': 'abdominal'},{'nome': 'Abdominal frontal', 'categoria': 'abdominal'}, 
                  {'nome': 'Abdominal bicicleta', 'categoria': 'abdominal'},{'nome': 'Abdominal com inversão', 'categoria': 'abdominal'},
                  {'nome': 'Abdominal com braços estendidos', 'categoria': 'abdominal'},{'nome': 'Prancha abdominal', 'categoria': 'abdominal'}, 
                  {'nome': 'Obliquos com elástico', 'categoria': 'abdominal'},{'nome': 'Agachamento livre', 'categoria': 'perna'}, 
                  {'nome': 'Leg-press 45 graus', 'categoria': 'perna'},{'nome': 'Desenvolvimento Arnold', 'categoria': 'ombro'}, 
                  {'nome': 'Elevacao lateral', 'categoria': 'ombro'},{'nome': 'Flexão de joelho', 'categoria': 'perna'}, 
                  {'nome': 'Banco adutor', 'categoria': 'perna'},{'nome': 'Encolhimento no smith', 'categoria': 'trapezio'}, 
                  {'nome': 'Agachamento', 'categoria': 'gluteos'},{'nome': 'Banco extensor', 'categoria': 'coxa'}, 
                  {'nome': 'Banco flexor', 'categoria': 'perna'},{'nome': 'Banco abdutor', 'categoria': 'gluteo'}, 
                  {'nome': 'Abdução quadril', 'categoria': 'gluteo'}]
    serie = random.randint(2, 4)

    def gerarExercicio(self, x):
        ex = random.sample(self.exercicios, x)
        return ex

    def __str__(self):
        exercicio = random.choice(self.exercicios)
        return 'Exercicio: %s(%s) | Serie: %d | Repeticao: %d' % (exercicio['nome'], exercicio['categoria'], self.serie, random.choice([10, 15, 20]))


class GeradorPessoas:
    sequencia = 0
    objetos = []
    name = ['Abda Silva','Abigail Santos','Acácia Silva','Adalgisa  Santos','Adeilce Silva','Adelaide Santos','Adélia Silva','Adriana Santos','Agnes Silva','Aida Santos','Aidée Dias','Aime Santos','Aimée Dias','Aira Santos','Aisla Dias','Alana Santos','Alanis Dias','Alaíde Santos','Alba Dias','Albertina Santos','Alcina Dias','Alcione Santos','Aldete Dias','Alécya','Alessandra Dias','Alena','Alenis Dias','Aléssia','Alexa','Alexandra','Alice','Alicia','Aline','Alison','Alriana','Alzira','Amalia','Amanda','Amelia','América','Ana','Anabel','Anabelle','Ananda','Anastácia','Andréa','Andressa','Anete','Angela','Angélica','Angelina','Anita','Antonia','Antonieta','Antuérpia','Aparecida','Araci','Ariane','Ariene','Arisla','Arissa','Arlette','Arminda','Aryana','Astrid','Audrey','Adelinda','Assunção','Audrey','Augusta','Aura','Aurelia','Aarão','Abdala','Abdemis','Abel','Abelardo','Abraão','Acácio','Adalberto','Adamastor','Adão','Adauto','Ademar','Adib','Adolfo','Adriano','Aécio','Aelington','Agnaldo','Alan','Alberico','Alberto','Alceu','Alcir','Aldo','Alencar','Alessandro','Alessio','Alex','Alexsander','Alfredo','Alfeu','Almir','Aluisio','Alvaro','Altamir','Amadeu','Amauri','Américo','Amin','Amâncio','Amilcar','Amir','Amon','Anat','André','Andrew','Angel','Angelo','Anibal','Anselmo','Antero','Anthony','Antonio','Arlindo','Apolo','Aquiles','Aristoteles','Armando','Arnaldo','Arthur','Ary','Atanasio','Atilio','Augusto','Aurelio','Ayram','Ayrton ','Badia','Barbara','Bartira','Beatriz','Bela','Belinda','Berenice','Bernadete','Berta','Betânia','Beth','Beverly','Betina','Bianca','Blanca','Brenda','Brigida','Brigite','Brisa','Bruna Balbo','Baldoc','Basilio','Batista','Benicio','Benito','Benjamin','Bento','Bernardo','Billy','Bolivar','Bonifácio','Bosco','Brad','Brás','Brayan','Brendon','Breno','Brian','Bruce','Bruno ','Cacilda','Camila','Candida','Carla','Carlota','Carmela','Carmem','Carol','Carole','Carolina','Cassandra','Cassia','Cassiane','Catarina','Cecile','Cecília','Celene','Celeste','Célia','Celina','Chantal','Charlote','Chaylla','Chiara','Cibele','Cintia','Clara','Clariana','Clarissa','Cláudia','Cleide','Clélia','Cléo','Cleonice','Cleonir','Cleopatra','Cleuza','Clotilde','Conceição','Constance','Corina','Cristiane','Cristina ','Caetano','Caim','Caiã','Caio','Caique','Camilo','Carlito','Carlos','Carmelo','Casimiro','Cassio','Cauê','Cécil','Célio','Celso','Cesar','Charles','Chris','Christian','Cid','Cirano','Cirilo','Ciro','Claudio','Cleber','Clésio','Clície','Clovis','Conrado','Constantino','Cornelio','Cosme','Crigor','Cristian','Cristiano','Dafnee','Daisy','Dalia','Dalita','Dalva','Danelise','Daniela','Debora','Deidre','Delia','Denise','Diana','Dilma','Dinah','Dinorah','Dolores','Dominique','Doris','Doroty','Dulcineia','Dunia ','Dan','Daniel','Danilo','Dante','Damiano','Dario','David','Decio','Demétrio','Denis','Deoclides','Dercio','Dereck','Deusdete','Diego','Dieter','Dilson','Dimas','Diogo','Dionisio','Dirceu','Domingos','Dorival','Douglas','Durval Eda','Edênia','Edilia','Edimary','Edimercia','Edmagna','Edith','Edna','Eduarda','Edwirge','Egle','Elaine','Elen','Elena','Eleonora','Eliane','Elida','Elide','Elisa','Elisabeth','Elisiana','Elke','Else','Eloisa','Elvira','Elza','Emanuele','Emilia','Emmeline','Eneida','Erenilda','Erica','Erlaine','Erminia','Estela','Ester','Eugenia','Eulalia','Eunice','Eva','Evangelina','Evelyn','Evelyne Ebion','Ed','Eder','Edilson','Ediraldo','Edmilson','Ednei','Edson','Eduardo','Edvaldo','Eivaldo','Elias','Eliezer','Eliseu','Eloy','Elton','Emerson','Emil','Emilio','Enio','Estevão','Eric','Erinaldo','Ernani','Ernesto','Ettore','Eugenio','Eurico','Euzebio','Evair','Evandro','Everaldo ','Fábia','Fabiana','Fabiane','Fabíola','Fabrícia','Fany','Fátima','Fenicia','Fernanda','Filomena','Fiona','Flávia','Flaviana','Flora','Franciely','Francini','Françoise','Frederica','Fúlvia ','Fabian','Fabiano','Fabio','Fabricio','Fausto','Fauzer','Feliciano','Felicio','Felinto','Felipe','Felix','Fernando','Firmino','Firmo','Flavio','Francisco','Franz','Frederico','Fúlvio','Gabriela','Gardênia','Geralda','Germana','Geilsa','Geny','Georgia','Gilda','Gina','Gioconda','Giovana','Giselda','Gisele','Gislaine','Giulia','Giuliana','Giulliane','Gladis','Glaucia','Glória','Gorete','Graça','Grace','Gracia','Graziela','Gudrun ','Gabriel','Gaspar','George','Geraldo','Gerd','Germano','Gerson','Gesualdo','Getúlio','Giacomo','Gian','Giancarlo','Gianfranco','Gil','Gilberto','Gilson','Gilvan','Giovani','Glauco','Gregory','Guido','Guilherme','Guilhermino','Gustavo Haidee','Hanna','Heide','Helen','Helena','Helga','Heloisa','Heriette','Hilda','Hortência ','Harley','Haroldo','Hector','Helder','Heitor','Helio','Helmut','Henri','Heraldo','Herbert','Herculano','Hercules','Hermano','Heron','Hidelbrando','Homero','Honorio','Horacio','Hugo','Humberto ','Iasmim','Idiene','Ilana','Ilce','Indira','Inês','Ingrid','Imaculada','Inara','Iolanda','Ione','Iracema','Iraídes','Irene','Irina','Iris','Isabel','Isabela','Isadora','Isis','Isolda','Ivana','Ivani','Iverly','Ivete','Ivna','Ivonete','Ivone','Izilda Ibrahim','Ícaro','Igino','Igor','Ilário','Ilton','Inacio','Irineu','Isaac','Isaias','Ismael','Israel','Iuri','Ivan','Ivich','Ivo','Jacilei','Jade','Jacqueline','Jaimerina','Janaina','Jandineia','Janete','Janey','Jaqueline','Jasmim','Jeane','Jennifer','Joana','Joelle','Johanna','Jordana','Josefina','Joselma','Josie','Joyce','Jucilene','Judith','Julia','Juliana','Julieta','Jurema','Jussara Jacques','Jaime','Jair','Jairo','James','Jason','Jean','Jefferson','Jeremias','Jesus','João ','Joaquim','Joel','Joelmir','Johanes','Johann','John','Johnny','Jonas','Jonathan','Jorge','José','Josualdo','Josué','Judas','Julio','Juscelino','Justo Kalliope','Kamilla','Karen','Karina','Karyne','Kate','Katherina','Kátia','Kédma','Kelly','Kênia','Kristen Klaus','Keid','Keith','Kennedy','Kenneth','Kenzo','Kevin','Kleber','Kleiton Laila','Lais','Lara','Larissa','Lavinia','Lauanda','Laura','Laylla','Laysa','Leda','Leila','Lenemar','Lenise','Lenora','Lesley','Letícia','Lidia','Liége','Ligia','Lilian','Liliana','Liliane','Linda','Lindsey','Liney','Lis','Lisete','Lisley','Lismara','Lívia','Lolita','Loredana','Lorena','Lorraine','Louise','Luana','Luce','Lúcia','Luciana','Luciane','Luciene','Lucila','Lucília','Lucivane','Lucy','Ludmila','Ludicea','Luiza','Lurdes','Luzia Ladislau','Laercio','Laerte','Lauro','Leandro','Leo','Leon','Leonardo','Levi','Lineu','Livio','Lorenzo','Louis','Lourival','Lucas','Luciano','Lucio','Luigi','Luis','LukeMabel','Madalena','Magali','Magda','Maira','Maitê','Malka','Malú','Manuela','Mara','Marcela','Marcia','Margarete','Margareth','Margarida','Maria','Mariana','Mariane','Maricy','Marieli','Márjore','Marilda','Marilena','Marilia','Marilisa','Marilu','Marina','Marinela ','Maris','Marisa','Marise','Maristela','Marjorie','Marlene','Marli','Marta','Martina','Marucia','Matilde','Maura','Maureen','Mayã','Mayara','Maysa','Melania','Melayne ','Melissa','Milane','Milena','Milene','Mircia','Mirela','Miriam','Maciel','Manoel','Mantovaine','Marcel','Marcelo','Marciano','Marcilio','Marcio','Marco','Marcos','Mariano','Marino','Mario','Martin','Massimo','Mateus','Matias','Mauricio','Mauro','Max','Maximiliano','Michel','Miguel','Milton','Moacir','Moises','Mohsen','Morris','Murilo Nadia','Naiara','Nair','Nancy','Natália','Natasha','Nayara','Naylla','Nayma','Nayra','Néia','Neuza','Nicia','Nicole','Nilda','Nilva','Nina','Ninke','Nivia','Noemia','Norma','Nuria Nairon','Narciso','Natan','Natanael','Nelio','Nelson','Nereo','Nevio','Newton','Ney','Nicolas','Nilton','Nivaldo Odessa','Odete','Odila','Odília','Ofélia','Olga','Olides','Olinda','Olímpia','Olivia','Ondina','Oraides','Otávia','Otília Odair','Odécio','Odherban','Odilon','Odilson','Odir','Odorico','Oduvaldo','Olavo','Olegário','Olivier','Onofre','Orfeu','Orides','Orlando','Omar','Oscar','Osias','Osmar','Osni','Osório','Oswaldo','Otacílio','Otaviano','Otavio','Otelo','Otoni','Otto','Oton','Ozeias','Ozias Pamela','Paola','Patricia','Paula','Paulete','Pedrina','Pedrita','Persia','Perla','Petra','Petrúcia','Pia','Pietra','Pilar','Poliana','Priscila','Próspera','Prudencia Pablo','Pascoal','Patrick','Paulo','Pedro','Percival','Peter','Petrucio','Pierluigi','Pierpaulo','Piero','Pio','Plácido','Plinio','Procopio Quenia','Quitéria Quentin','Quincas','Quirino Rafaela','Raissa','Raquel','Rebeca','Regina','Rejane','Renata','Riane','Rita','Roberta','Roclides','Rogeria','Romana','Rosa','Rosali','Rosalia','Rosamaria','Rosana','Rosangela','Rosaria','Roseane','Roseli','Rosicler','Rossandra','Ruth Rafael','Raimundo','Ralf','Ramon','Randolpho','Ráriton','Raul','Reginaldo','Reinaldo','Renato','Ricardo','Roberto','Robson','Rodney','Rodrigo','Roger','Rogerio','Romero','Romeu','Romulo','Ronaldo','Roney','Roni','Roque','Rossélio','Rubens Sabine','Sabrina','Salete','Samanta','Samia','Samira','Sandra','Sarah','Sarina','Selma','Sharon','Sheeva','Sheila','Shirley','Sibele','Sibila','Silmara','Silvana','Silvia','Simone','Sioma','Sofia','Solange','Sonia','Sophia','Soraia','Stefane','Stefania','Stephanie','Stela','Suédia','Sueli','Sumaia','Susan','Suzana','Suzel','Suzete Salvador','Salvio','Sandro','Samir','Samuel','Sante','Saul','Sebastião','Sebastian','Sergio','Sidney','Silas','Silvain','Silvano','Silverio','Silvio','Sócrates','Stefano','Sunny Taciana','Talia','Talita','Tamara','Tania','Tatiana','Telcilene','Teodora','Teresa','Téri','Thais','Thauany','Thayná','Thelma','Tiana','Ticiana','Tricia','Tônia','Tunia Tadeu','Tarcisio','Teobaldo','Teodoro','Thales','Theo','Theophilo','Theseo','Thomas','Timoteo','Torquato Ulla','Urania','Ursula','Ursulina Ubaldino','Ubaldo','Ubirajara','Ulisses','Ulpiano','Umbelino','Umberto','Urbano','Uriel Valderez','Valdinea','Valentina','Valeria','Valeska','Vanderleia','Vanessa','Vani','Vania','Vanusa','Vera','Veralice','Veridiana','Veronica','Virginia','Vitoria','Vivian','Viviane Valentino','Valdir','Valmir','Vanderley','Vasco','Venâncio','Venceslau','Vicente','Vinicius','Vitor','Vivaldo','Vladimir','Vlamir Xaquira','Xaukia','Xênia Xavier Yara','Yanna','Yasmin','Yolanda','Yole','Yone','Yose Yago','Yan','Yasson','Yglésio','Yuki','Yuri','Yuso W Z Walquiria','Wanda','Wanderleia','Wanessa','Wendy','Wilma Wagner','Wald','Waldir','Wallace','Walter','Wander','Wando','Washington','Weblen','Wellington','Welson','Wesley','Willian','Wilson','Wolf Zaira','Zarifa','Zelia','Zelinda','Zelita','Zenaide','Zenilde','Zenir','Zilá','Zilda','Zilena','Zilma','Zita','Zora','Zoraide','Zulmira','Zyndal ','Zacarias','Zélio','Zenóbio ','Zeus','Ziraldo','Zozimo']


    last = ['Agostinho', 'Aguiar', 'Albuquerque', 'Alegria', 'Alencastro',
            'Almada', 'Alves', 'Alvim', 'Amorim', 'Andrade', 'Antunes', 'Aparício', 'Apolinário', 'Araújo',
            'Arruda', 'Assis', 'Assunção', 'Ávila', 'Azambuja', 'Baptista', 'Barreto', 'Barros', 'Beira-Mar',
            'Belchior', 'Belém', 'Bernardes', 'Bittencourt', 'Boaventura', 'Bonfim', 'Botelho', 'Brites',
            'Brito', 'Caetano', 'Calixto', 'Camacho', 'Camilo', 'Capelo', 'Castro', 'Cavalcante', 'Chaves',
            'Conceição', 'Corte Real', 'Cortês', 'Coutinho', 'Crespo', 'Cunha', 'Curado', 'Custódio',
            'Córdoba',  'Damásio', 'Dantas', 'Dias', 'Dinís', 'Domingues', 'Dorneles', 'dos Reis',
            'Drumond', 'D’Ávila', 'Escobar', 'Espinosa', 'Esteves', 'Evangelista', 'Farias', 'Ferrari',
            'Figueiredo', 'Figueiroa', 'Flores', 'Fogaça', 'Freitas', 'Frutuoso', 'Furtado', 'Félix',
            'Galvão', 'Garcia', 'Gaspar', 'Gentil', 'Geraldes', 'Gil', 'Godinho', 'Gomes', 'Gonzaga',
            'Goulart', 'Gouveia', 'Guedes', 'Guimarães', 'Guterres', 'Góis', 'Hernandes', 'Hilário',
            'Hipólito', 'Ibrahim', 'Ilha', 'Infante',  'Jaques', 'Jesus', 'Jordão', 'Lacerda',
            'Lancastre', 'Leiria', 'Lessa', 'Machado', 'Maciel', 'Magalhães', 'Maia', 'Maldonado', 'Marinho',
            'Marques', 'Martins', 'Medeiros', 'Meireles', 'Mello', 'Mendes', 'Menezes', 'Mesquita', 'Modesto',
            'Monteiro', 'Morais', 'Moreira', 'Morgado', 'Moura', 'Muniz', 'Neves', 'Nogueira', 'Novais',
            'Nóbrega', 'Ornélas', 'Oliveira', 'Ourique', 'Pacheco', 'Padilha', 'Paiva', 'Paraíso', 'Paris',
            'Peixoto', 'Peralta', 'Peres', 'Pilar', 'Pimenta', 'Pinheiro', 'Portela', 'Quaresma', 'Quarteira',
            'Queiroz', 'Ramires', 'Ramos', 'Rebelo', 'Resende', 'Ribeiro', 'Salazar', 'Sales', 'Salgado',
            'Salgueiro', 'Sampaio', 'Sanches', 'Santana', 'Siqueira', 'Soares', 'Subtil', 'Tavares', 'Taveira',
            'Teixeira', 'Teles', 'Torres', 'Trindade', 'Varela', 'Vargas', 'Vasconcelos', 'Vasques', 'Veiga',
            'Veloso', 'Vidal', 'Vieira', 'Vilela', 'Xavier', 'Ximenes', 'Xisco', 'Zagalo', 'Zanette', 'Zaganelli']

    def salva(self):
        self.__class__.sequencia += 1
        self.__class__.objetos.append(self)

    def __str__(self):
        return "Nome: %s\nSexo: Masculino\nIdade: %d anos\nAltura: %.2fm \nPeso: %dkg" % (self.gerar_nome_completo(), self.gerar_idade(), self.gerar_altura(), self.gerar_peso())

    @classmethod
    def listar_todas_instancias(cls):
        return cls.objetos

    def gerar_nome(self):
        return random.choice(self.name)

    def gerar_sobrenome(self):
        return random.choice(self.last)

    def gerar_nome_completo(self):
        return self.gerar_nome()+" "+self.gerar_sobrenome()+" "+self.gerar_sobrenome()

    def gerar_idade(self):
        return random.randint(17, 45)

    def gerar_altura(self):
        return round(random.uniform(1.5, 2.0), 2)

    def gerar_peso(self):
        return random.randint(50, 110)

class GeradorAmnase:
    hipertrofia = ""
    lentes_contato = ""
    alergia = ""
    tabagismo = ""
    bebida_alcoolica = ""
    medicamento = ""
    epilepsia = ""
    convulsoes = ""
    doenca = ""
    cirurgia_plastica = ""
    cortes = ""
    abrasoes = ""
    inchacos = ""

    resposta_normal = [1,0]
    resposta_complexa = [1,0]

    def gerar(self):
        self.hipertrofia = random.choice(self.resposta_normal)
        self.lentes_contato = random.choice(self.resposta_normal)
        self.alergia = random.choice(self.resposta_normal)
        self.tabagismo = random.choice(self.resposta_normal)
        self.bebida_alcoolica = random.choice(self.resposta_complexa)
        self.medicamento = random.choice(self.resposta_normal)
        self.epilepsia = 0
        self.convulsoes = 0
        self.doenca = random.choice(self.resposta_normal)
        self.cirurgia_plastica = random.choice(self.resposta_normal)
        self.cortes = random.choice(self.resposta_normal)
        self.abrasoes = random.choice(self.resposta_normal)
        self.inchacos = random.choice(self.resposta_normal)

        return [self.hipertrofia,self.lentes_contato,self.alergia,self.tabagismo,self.bebida_alcoolica,self.medicamento,self.epilepsia,self.convulsoes,self.doenca,self.cirurgia_plastica,self.cortes,self.abrasoes,self.inchacos]

class GeradorMedidas:
    def calculaIMC(self,peso,altura):
        return peso/altura**2
    
    def statusIMC(self,imc):
        if(imc < 18.5):
            return 'Abaixo do peso'
        elif(imc >= 18.5 and imc <= 25):
            return 'Normal'
        elif(imc > 25 and imc <= 30):
            return 'Acima do peso'
        elif(imc > 30 and imc <= 35):
            return 'Obesidade'
        else:
            return 'Obesidade severa'

    def gerarOmbro(self):
        return round(random.uniform(13, 16.5), 2)

    def gerarTorax(self):
        return round(random.uniform(92, 120), 2)

    def gerarCintura(self):
        return round(random.uniform(70, 120), 2)

    def gerarQuadris(self):
        return round(random.uniform(90, 116), 2)

    def gerarPescoco(self):
        return round(random.uniform(38, 45), 2)

    def gerarBiceps(self):
        return round(random.uniform(35, 45), 2)

    def gerarAntebraco(self):
        return round(random.uniform(27, 37), 2)

    def gerarPeito(self):
        return round(random.uniform(92, 125), 2)

    def gerarCoxas(self):
        return round(random.uniform(50, 67), 2)
    
    def gerarPanturrilha(self):
        return round(random.uniform(33,45),2)


if __name__ == '__main__':
    with open('teste.csv', 'wb') as csvfile:
        gp = GeradorPessoas()
        ge = GeradorExercicios()
        ga = GeradorAmnase()
        gm = GeradorMedidas()

        campos = ['nome', 'idade', 'altura', 'peso', 'ex1-nome', 'ex1-categoria', 'ex1-serie','ex1-repeticao',
        'ex2-nome', 'ex2-categoria', 'ex2-serie', 'ex2-repeticao','ex3-nome', 'ex3-categoria', 'ex3-serie', 'ex3-repeticao',
        'ex4-nome', 'ex4-categoria', 'ex4-serie', 'ex4-repeticao','ex5-nome', 'ex5-categoria', 'ex5-serie', 'ex5-repeticao',
        'ex6-nome', 'ex6-categoria', 'ex6-serie', 'ex6-repeticao','ex7-nome', 'ex7-categoria', 'ex7-serie', 'ex7-repeticao',
        'ex8-nome', 'ex8-categoria', 'ex8-serie', 'ex8-repeticao','ex9-nome', 'ex9-categoria', 'ex9-serie', 'ex9-repeticao',
        'ex10-nome', 'ex10-categoria', 'ex10-serie', 'ex10-repeticao','hipertrofia','lentes_contato','alergia','tabagismo',
        'bebida_alcoolica','medicamento','epilepsia','convulsoes','doenca','cirurgia_plastica','cortes','abrasoes','inchacos',
        'Ombro','Torax','Cintura','Quadris','Pescoco','Biceps','Antebraco','Peito','Coxas','Panturrilha','imc','status_imc']

        writer = csv.DictWriter(csvfile, fieldnames=campos)

        writer.writeheader()

        for x in range(112):
            amnase = ga.gerar()
            listaEx = ge.gerarExercicio(10)
            serie = random.randint(2, 4)
            repeticao = random.choice([10, 15, 20])
            peso_gerado = gp.gerar_peso()
            altura_gerada = gp.gerar_altura()
            imc_gerado = gm.calculaIMC(peso_gerado,altura_gerada)

            writer.writerow({'nome': gp.gerar_nome_completo(), 'idade': gp.gerar_idade(), 'altura': altura_gerada, 'peso': peso_gerado,
             'ex1-nome': listaEx[0]['nome'], 'ex1-categoria': listaEx[0]['categoria'], 'ex1-serie': serie, 'ex1-repeticao': repeticao,
             'ex2-nome': listaEx[1]['nome'], 'ex2-categoria': listaEx[1]['categoria'], 'ex2-serie': serie, 'ex2-repeticao': repeticao,
             'ex3-nome': listaEx[2]['nome'], 'ex3-categoria': listaEx[2]['categoria'], 'ex3-serie': serie, 'ex3-repeticao': repeticao,
             'ex4-nome': listaEx[3]['nome'], 'ex4-categoria': listaEx[3]['categoria'], 'ex4-serie': serie, 'ex4-repeticao': repeticao,
             'ex5-nome': listaEx[4]['nome'], 'ex5-categoria': listaEx[4]['categoria'], 'ex5-serie': serie, 'ex5-repeticao': repeticao,
             'ex6-nome': listaEx[5]['nome'], 'ex6-categoria': listaEx[5]['categoria'], 'ex6-serie': serie, 'ex6-repeticao': repeticao,
             'ex7-nome': listaEx[6]['nome'], 'ex7-categoria': listaEx[6]['categoria'], 'ex7-serie': serie, 'ex7-repeticao': repeticao,
             'ex8-nome': listaEx[7]['nome'], 'ex8-categoria': listaEx[7]['categoria'], 'ex8-serie': serie, 'ex8-repeticao': repeticao,
             'ex9-nome': listaEx[8]['nome'], 'ex9-categoria': listaEx[8]['categoria'], 'ex9-serie': serie, 'ex9-repeticao': repeticao,
             'ex10-nome': listaEx[9]['nome'], 'ex10-categoria': listaEx[9]['categoria'], 'ex10-serie': serie, 'ex10-repeticao': repeticao, 
             'hipertrofia' : amnase[0],'lentes_contato':amnase[1],'alergia':amnase[2],'tabagismo':amnase[3],'bebida_alcoolica':amnase[4],
             'medicamento':amnase[5],'epilepsia':amnase[6],'convulsoes':amnase[7],'doenca':amnase[8],'cirurgia_plastica': amnase[9],
             'cortes':amnase[10],'abrasoes':amnase[11],'inchacos':amnase[12],'Ombro':gm.gerarOmbro(),'Torax':gm.gerarTorax(),'Cintura':gm.gerarCintura(),
             'Quadris':gm.gerarQuadris(),'Pescoco':gm.gerarPescoco(),'Biceps':gm.gerarBiceps(),'Antebraco':gm.gerarAntebraco(),'Peito':gm.gerarPeito(),
             'Coxas':gm.gerarCoxas(),'Panturrilha':gm.gerarPanturrilha(),'imc':imc_gerado,'status_imc':gm.statusIMC(imc_gerado)
             })
