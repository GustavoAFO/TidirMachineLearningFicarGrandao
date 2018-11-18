#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import csv
import sys


class GeradorExercicios:
    exercicios = [{'nome': 'Supino reto', 'categoria': 'peito'}, {'nome': 'Crucifixo inclinado', 'categoria': 'peito'},
                  {'nome': 'Crosshover', 'categoria': 'peito'}, {'nome': 'Triceps pulley unilateral', 'categoria': 'triceps'},
                  {'nome': 'Cable crunch', 'categoria': 'abdominal'}, {'nome': 'Puxada frente polia alta', 'categoria': 'costas'},
                  {'nome': 'Remada articulada', 'categoria': 'costas'}, {'nome': 'Rosca direta', 'categoria': 'biceps'},{'nome': 'Rosca alternada', 'categoria': 'biceps'}, 
                  {'nome': 'Flexao lateral do tronco', 'categoria': 'abdominal'},{'nome': 'Puxada alta com bracos estendidos', 'categoria': 'costas'}, 
                  {'nome': 'Abdominal com flexao de pernas', 'categoria': 'abdominal'},{'nome': 'Abdominal frontal', 'categoria': 'abdominal'}, 
                  {'nome': 'Abdominal bicicleta', 'categoria': 'abdominal'},{'nome': 'Abdominal com inversao', 'categoria': 'abdominal'},
                  {'nome': 'Abdominal com bracos estendidos', 'categoria': 'abdominal'},{'nome': 'Prancha abdominal', 'categoria': 'abdominal'}, 
                  {'nome': 'Obliquos com elastico', 'categoria': 'abdominal'},{'nome': 'Agachamento livre', 'categoria': 'perna'}, 
                  {'nome': 'Leg-press 45 graus', 'categoria': 'perna'},{'nome': 'Desenvolvimento Arnold', 'categoria': 'ombro'}, 
                  {'nome': 'Elevacao lateral', 'categoria': 'ombro'},{'nome': 'Flexao de joelho', 'categoria': 'perna'}, 
                  {'nome': 'Banco adutor', 'categoria': 'perna'},{'nome': 'Encolhimento no smith', 'categoria': 'trapezio'}, 
                  {'nome': 'Agachamento', 'categoria': 'gluteos'},{'nome': 'Banco extensor', 'categoria': 'coxa'}, 
                  {'nome': 'Banco flexor', 'categoria': 'perna'},{'nome': 'Banco abdutor', 'categoria': 'gluteo'}, 
                  {'nome': 'Abducao quadril', 'categoria': 'gluteo'},{'nome': 'Encolhimento com halteres', 'categoria': 'trapezio'},
                  {'nome': 'Encolhimento com barra por tras', 'categoria': 'trapezio'},{'nome': 'Encolhimento com barra pela frente', 'categoria': 'trapezio'},
                  {'nome': 'Remada alta', 'categoria': 'trapezio'},{'nome': 'Crucifixo invertido na polia', 'categoria': 'trapezio'},
                  {'nome': 'Crucifixo invertido deitado com halteres', 'categoria': 'trapezio'},{'nome': 'Elevacao lateral alternada com polia baixa', 'categoria': 'trapezio'},
                  {'nome': 'Rosca concentrada', 'categoria': 'biceps'},{'nome': 'Rosca com o cabo', 'categoria': 'biceps'},
                  {'nome': 'Rosca direta em pe com a barra', 'categoria': 'biceps'},{'nome': 'Barra fixa', 'categoria': 'biceps'},
                  {'nome': 'Rosca com barra EZ pegada fechada', 'categoria': 'biceps'},{'nome': 'Rosca com barra W pegada fechada', 'categoria': 'biceps'},
                  {'nome': 'Rosca com barra EZ', 'categoria': 'biceps'},{'nome': 'Rosca com barra W', 'categoria': 'biceps'},
                  {'nome': 'Rosca com barra EZ pegada aberta', 'categoria': 'biceps'},{'nome': 'Rosca com barra W  pegada aberta', 'categoria': 'biceps'},
                  {'nome': 'Rosca inclinada', 'categoria': 'biceps'},{'nome': 'Rosca scott', 'categoria': 'biceps'},
                  {'nome': 'Supino reto com barra', 'categoria': 'peito'},{'nome': 'Supino reto com halteres', 'categoria': 'peito'},
                  {'nome': 'Flexao basica', 'categoria': 'peito'},{'nome': 'Flexao inclinada', 'categoria': 'peito'},
                  {'nome': 'Supino inclinado com barra', 'categoria': 'peito'},{'nome': 'Supino inclinado com halteres', 'categoria': 'peito'},
                  {'nome': 'Voador no cabo com banco inclinado', 'categoria': 'peito'},{'nome': 'Crosshover reto', 'categoria': 'peito'},
                  {'nome': 'Extensao de triceps deitado', 'categoria': 'triceps'},{'nome': 'Supino no banco reto com pegada fechada', 'categoria': 'triceps'},
                  {'nome': 'Mergulho no banco', 'categoria': 'triceps'},{'nome': 'Triceps no banco', 'categoria': 'triceps'},
                  {'nome': 'Extensao de halteres sob a cabeca', 'categoria': 'triceps'},{'nome': 'Mergulho com peso nas paralelas', 'categoria': 'triceps'},
                  {'nome': 'Mergulho de triceps na maquina', 'categoria': 'triceps'},{'nome': 'Extensao no cabo sob a cabeca com corda', 'categoria': 'triceps'},
                  {'nome': 'Triceps Frances', 'categoria': 'triceps'},{'nome': 'Triceps Pulley', 'categoria': 'triceps'},
                  {'nome': 'Barra fixa', 'categoria': 'costas'},{'nome': 'Remada curvada', 'categoria': 'costas'},
                  {'nome': 'Barra fixa com pegada larga', 'categoria': 'costas'},{'nome': 'Remada unilateral com haltere', 'categoria': 'costas'},
                  {'nome': 'Pullover com haltere', 'categoria': 'costas'},{'nome': 'Remada baixa sentada', 'categoria': 'costas'},
                  {'nome': 'Remada em pe na barra T', 'categoria': 'costas'},{'nome': 'Remada curvada com pegada invertida', 'categoria': 'costas'},
                  {'nome': 'Remada no Smith com pegada invertida', 'categoria': 'costas'},{'nome': 'Pull-down de pegada fechada', 'categoria': 'costas'},
                  {'nome': 'Pull-down', 'categoria': 'costas'},{'nome': 'Remada no banco inclinado com halteres', 'categoria': 'costas'},
                  {'nome': 'Elevacao lateral deitado', 'categoria': 'costas'},{'nome': 'Levantamento terra com barra', 'categoria': 'costas'},
                  {'nome': 'Agachamento frontal', 'categoria': 'costas'},        
                  {'nome': 'ombros com halteres', 'categoria': 'ombro'},{'nome': 'ombros com barra', 'categoria': 'ombro'},
                  {'nome': 'Desenvolvimento Arnold', 'categoria': 'ombro'},{'nome': 'Elevacao lateral com halteres', 'categoria': 'ombro'},
                  {'nome': 'Crucifixo invertido com halteres', 'categoria': 'ombro'},{'nome': 'Flexao hindu', 'categoria': 'ombro'},
                  {'nome': 'Remada alta em pe com halteres', 'categoria': 'ombro'},{'nome': 'Remada alta no cabo', 'categoria': 'ombro'},
                  {'nome': 'Remada alta no Smith', 'categoria': 'ombro'},{'nome': 'Voador invertido na maquina', 'categoria': 'ombro'},
                  {'nome': 'Agachamento', 'categoria': 'perna'},{'nome': 'Levantamento Terra', 'categoria': 'perna'},
                  {'nome': 'Agachamento Frente', 'categoria': 'perna'},{'nome': 'Agachamento bulgaro', 'categoria': 'perna'},
                  {'nome': 'Avanco', 'categoria': 'perna'},{'nome': 'Stiff ', 'categoria': 'perna'},
                  {'nome': 'Deadlift', 'categoria': 'perna'},{'nome': 'Leg Press', 'categoria': 'perna'},
                  {'nome': 'Agachamento com bola', 'categoria': 'coxa'},{'nome': 'Agachamento pliometrico', 'categoria': 'coxa'},
                  {'nome': 'Agachamento cossack', 'categoria': 'coxa'},{'nome': 'Agachamento com barra', 'categoria': 'coxa'},
                  {'nome': 'Avanco', 'categoria': 'coxa'},{'nome': 'Agachamento com o peso do corpo', 'categoria': 'coxa'},
                  {'nome': 'Agachamento com halter', 'categoria': 'coxa'},{'nome': 'Extensao de pernas', 'categoria': 'coxa'},
                  {'nome': 'Adutor de coxas', 'categoria': 'coxa'},{'nome': 'Agachamento no Smith', 'categoria': 'coxa'}]



    def gerarListaNova(self,x):
        exercicios_novo = []
        for ex in self.exercicios:
            if x in ex['categoria']:
                exercicios_novo.append(ex)
        return exercicios_novo

    def randomLista(self,lista,num):
        ex = random.sample(lista,num)
        return ex

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
    name = ['Abda Silva','Abigail Santos','Acacia Silva','Adalgisa  Santos','Adeilce Silva','Adelaide Santos','Adelia Silva','Adriana Santos','Agnes Silva','Aida Santos','Aidee Dias','Aime Santos','Aimee Dias','Aira Santos','Aisla Dias','Alana Santos','Alanis Dias','Alaide Santos','Alba Dias','Albertina Santos','Alcina Dias','Alcione Santos','Aldete Dias','Alecya','Alessandra Dias','Alena','Alenis Dias','Alessia','Alexa','Alexandra','Alice','Alicia','Aline','Alison','Alriana','Alzira','Amalia','Amanda','Amelia','America','Ana','Anabel','Anabelle','Ananda','Anastacia','Andrea','Andressa','Anete','Angela','Angelica','Angelina','Anita','Antonia','Antonieta','Antuerpia','Aparecida','Araci','Ariane','Ariene','Arisla','Arissa','Arlette','Arminda','Aryana','Astrid','Audrey','Adelinda','Assuncao','Audrey','Augusta','Aura','Aurelia','Aarao','Abdala','Abdemis','Abel','Abelardo','Abraao','Acacio','Adalberto','Adamastor','Adao','Adauto','Ademar','Adib','Adolfo','Adriano','Aecio','Aelington','Agnaldo','Alan','Alberico','Alberto','Alceu','Alcir','Aldo','Alencar','Alessandro','Alessio','Alex','Alexsander','Alfredo','Alfeu','Almir','Aluisio','Alvaro','Altamir','Amadeu','Amauri','Americo','Amin','Amâncio','Amilcar','Amir','Amon','Anat','Andre','Andrew','Angel','Angelo','Anibal','Anselmo','Antero','Anthony','Antonio','Arlindo','Apolo','Aquiles','Aristoteles','Armando','Arnaldo','Arthur','Ary','Atanasio','Atilio','Augusto','Aurelio','Ayram','Ayrton ','Badia','Barbara','Bartira','Beatriz','Bela','Belinda','Berenice','Bernadete','Berta','Betânia','Beth','Beverly','Betina','Bianca','Blanca','Brenda','Brigida','Brigite','Brisa','Bruna Balbo','Baldoc','Basilio','Batista','Benicio','Benito','Benjamin','Bento','Bernardo','Billy','Bolivar','Bonifacio','Bosco','Brad','Bras','Brayan','Brendon','Breno','Brian','Bruce','Bruno ','Cacilda','Camila','Candida','Carla','Carlota','Carmela','Carmem','Carol','Carole','Carolina','Cassandra','Cassia','Cassiane','Catarina','Cecile','Cecilia','Celene','Celeste','Celia','Celina','Chantal','Charlote','Chaylla','Chiara','Cibele','Cintia','Clara','Clariana','Clarissa','Claudia','Cleide','Clelia','Cleo','Cleonice','Cleonir','Cleopatra','Cleuza','Clotilde','Conceicao','Constance','Corina','Cristiane','Cristina ','Caetano','Caim','Caia','Caio','Caique','Camilo','Carlito','Carlos','Carmelo','Casimiro','Cassio','Cauê','Cecil','Celio','Celso','Cesar','Charles','Chris','Christian','Cid','Cirano','Cirilo','Ciro','Claudio','Cleber','Clesio','Clicie','Clovis','Conrado','Constantino','Cornelio','Cosme','Crigor','Cristian','Cristiano','Dafnee','Daisy','Dalia','Dalita','Dalva','Danelise','Daniela','Debora','Deidre','Delia','Denise','Diana','Dilma','Dinah','Dinorah','Dolores','Dominique','Doris','Doroty','Dulcineia','Dunia ','Dan','Daniel','Danilo','Dante','Damiano','Dario','David','Decio','Demetrio','Denis','Deoclides','Dercio','Dereck','Deusdete','Diego','Dieter','Dilson','Dimas','Diogo','Dionisio','Dirceu','Domingos','Dorival','Douglas','Durval Eda','Edênia','Edilia','Edimary','Edimercia','Edmagna','Edith','Edna','Eduarda','Edwirge','Egle','Elaine','Elen','Elena','Eleonora','Eliane','Elida','Elide','Elisa','Elisabeth','Elisiana','Elke','Else','Eloisa','Elvira','Elza','Emanuele','Emilia','Emmeline','Eneida','Erenilda','Erica','Erlaine','Erminia','Estela','Ester','Eugenia','Eulalia','Eunice','Eva','Evangelina','Evelyn','Evelyne Ebion','Ed','Eder','Edilson','Ediraldo','Edmilson','Ednei','Edson','Eduardo','Edvaldo','Eivaldo','Elias','Eliezer','Eliseu','Eloy','Elton','Emerson','Emil','Emilio','Enio','Estevao','Eric','Erinaldo','Ernani','Ernesto','Ettore','Eugenio','Eurico','Euzebio','Evair','Evandro','Everaldo ','Fabia','Fabiana','Fabiane','Fabiola','Fabricia','Fany','Fatima','Fenicia','Fernanda','Filomena','Fiona','Flavia','Flaviana','Flora','Franciely','Francini','Francoise','Frederica','Fúlvia ','Fabian','Fabiano','Fabio','Fabricio','Fausto','Fauzer','Feliciano','Felicio','Felinto','Felipe','Felix','Fernando','Firmino','Firmo','Flavio','Francisco','Franz','Frederico','Fúlvio','Gabriela','Gardênia','Geralda','Germana','Geilsa','Geny','Georgia','Gilda','Gina','Gioconda','Giovana','Giselda','Gisele','Gislaine','Giulia','Giuliana','Giulliane','Gladis','Glaucia','Glória','Gorete','Graca','Grace','Gracia','Graziela','Gudrun ','Gabriel','Gaspar','George','Geraldo','Gerd','Germano','Gerson','Gesualdo','Getúlio','Giacomo','Gian','Giancarlo','Gianfranco','Gil','Gilberto','Gilson','Gilvan','Giovani','Glauco','Gregory','Guido','Guilherme','Guilhermino','Gustavo Haidee','Hanna','Heide','Helen','Helena','Helga','Heloisa','Heriette','Hilda','Hortência ','Harley','Haroldo','Hector','Helder','Heitor','Helio','Helmut','Henri','Heraldo','Herbert','Herculano','Hercules','Hermano','Heron','Hidelbrando','Homero','Honorio','Horacio','Hugo','Humberto ','Iasmim','Idiene','Ilana','Ilce','Indira','Inês','Ingrid','Imaculada','Inara','Iolanda','Ione','Iracema','Iraides','Irene','Irina','Iris','Isabel','Isabela','Isadora','Isis','Isolda','Ivana','Ivani','Iverly','Ivete','Ivna','Ivonete','Ivone','Izilda Ibrahim','icaro','Igino','Igor','Ilario','Ilton','Inacio','Irineu','Isaac','Isaias','Ismael','Israel','Iuri','Ivan','Ivich','Ivo','Jacilei','Jade','Jacqueline','Jaimerina','Janaina','Jandineia','Janete','Janey','Jaqueline','Jasmim','Jeane','Jennifer','Joana','Joelle','Johanna','Jordana','Josefina','Joselma','Josie','Joyce','Jucilene','Judith','Julia','Juliana','Julieta','Jurema','Jussara Jacques','Jaime','Jair','Jairo','James','Jason','Jean','Jefferson','Jeremias','Jesus','Joao ','Joaquim','Joel','Joelmir','Johanes','Johann','John','Johnny','Jonas','Jonathan','Jorge','Jose','Josualdo','Josue','Judas','Julio','Juscelino','Justo Kalliope','Kamilla','Karen','Karina','Karyne','Kate','Katherina','Katia','Kedma','Kelly','Kênia','Kristen Klaus','Keid','Keith','Kennedy','Kenneth','Kenzo','Kevin','Kleber','Kleiton Laila','Lais','Lara','Larissa','Lavinia','Lauanda','Laura','Laylla','Laysa','Leda','Leila','Lenemar','Lenise','Lenora','Lesley','Leticia','Lidia','Liege','Ligia','Lilian','Liliana','Liliane','Linda','Lindsey','Liney','Lis','Lisete','Lisley','Lismara','Livia','Lolita','Loredana','Lorena','Lorraine','Louise','Luana','Luce','Lúcia','Luciana','Luciane','Luciene','Lucila','Lucilia','Lucivane','Lucy','Ludmila','Ludicea','Luiza','Lurdes','Luzia Ladislau','Laercio','Laerte','Lauro','Leandro','Leo','Leon','Leonardo','Levi','Lineu','Livio','Lorenzo','Louis','Lourival','Lucas','Luciano','Lucio','Luigi','Luis','LukeMabel','Madalena','Magali','Magda','Maira','Maitê','Malka','Malú','Manuela','Mara','Marcela','Marcia','Margarete','Margareth','Margarida','Maria','Mariana','Mariane','Maricy','Marieli','Marjore','Marilda','Marilena','Marilia','Marilisa','Marilu','Marina','Marinela ','Maris','Marisa','Marise','Maristela','Marjorie','Marlene','Marli','Marta','Martina','Marucia','Matilde','Maura','Maureen','Maya','Mayara','Maysa','Melania','Melayne ','Melissa','Milane','Milena','Milene','Mircia','Mirela','Miriam','Maciel','Manoel','Mantovaine','Marcel','Marcelo','Marciano','Marcilio','Marcio','Marco','Marcos','Mariano','Marino','Mario','Martin','Massimo','Mateus','Matias','Mauricio','Mauro','Max','Maximiliano','Michel','Miguel','Milton','Moacir','Moises','Mohsen','Morris','Murilo Nadia','Naiara','Nair','Nancy','Natalia','Natasha','Nayara','Naylla','Nayma','Nayra','Neia','Neuza','Nicia','Nicole','Nilda','Nilva','Nina','Ninke','Nivia','Noemia','Norma','Nuria Nairon','Narciso','Natan','Natanael','Nelio','Nelson','Nereo','Nevio','Newton','Ney','Nicolas','Nilton','Nivaldo Odessa','Odete','Odila','Odilia','Ofelia','Olga','Olides','Olinda','Olimpia','Olivia','Ondina','Oraides','Otavia','Otilia Odair','Odecio','Odherban','Odilon','Odilson','Odir','Odorico','Oduvaldo','Olavo','Olegario','Olivier','Onofre','Orfeu','Orides','Orlando','Omar','Oscar','Osias','Osmar','Osni','Osório','Oswaldo','Otacilio','Otaviano','Otavio','Otelo','Otoni','Otto','Oton','Ozeias','Ozias Pamela','Paola','Patricia','Paula','Paulete','Pedrina','Pedrita','Persia','Perla','Petra','Petrúcia','Pia','Pietra','Pilar','Poliana','Priscila','Próspera','Prudencia Pablo','Pascoal','Patrick','Paulo','Pedro','Percival','Peter','Petrucio','Pierluigi','Pierpaulo','Piero','Pio','Placido','Plinio','Procopio Quenia','Quiteria Quentin','Quincas','Quirino Rafaela','Raissa','Raquel','Rebeca','Regina','Rejane','Renata','Riane','Rita','Roberta','Roclides','Rogeria','Romana','Rosa','Rosali','Rosalia','Rosamaria','Rosana','Rosangela','Rosaria','Roseane','Roseli','Rosicler','Rossandra','Ruth Rafael','Raimundo','Ralf','Ramon','Randolpho','Rariton','Raul','Reginaldo','Reinaldo','Renato','Ricardo','Roberto','Robson','Rodney','Rodrigo','Roger','Rogerio','Romero','Romeu','Romulo','Ronaldo','Roney','Roni','Roque','Rosselio','Rubens Sabine','Sabrina','Salete','Samanta','Samia','Samira','Sandra','Sarah','Sarina','Selma','Sharon','Sheeva','Sheila','Shirley','Sibele','Sibila','Silmara','Silvana','Silvia','Simone','Sioma','Sofia','Solange','Sonia','Sophia','Soraia','Stefane','Stefania','Stephanie','Stela','Suedia','Sueli','Sumaia','Susan','Suzana','Suzel','Suzete Salvador','Salvio','Sandro','Samir','Samuel','Sante','Saul','Sebastiao','Sebastian','Sergio','Sidney','Silas','Silvain','Silvano','Silverio','Silvio','Sócrates','Stefano','Sunny Taciana','Talia','Talita','Tamara','Tania','Tatiana','Telcilene','Teodora','Teresa','Teri','Thais','Thauany','Thayna','Thelma','Tiana','Ticiana','Tricia','Tônia','Tunia Tadeu','Tarcisio','Teobaldo','Teodoro','Thales','Theo','Theophilo','Theseo','Thomas','Timoteo','Torquato Ulla','Urania','Ursula','Ursulina Ubaldino','Ubaldo','Ubirajara','Ulisses','Ulpiano','Umbelino','Umberto','Urbano','Uriel Valderez','Valdinea','Valentina','Valeria','Valeska','Vanderleia','Vanessa','Vani','Vania','Vanusa','Vera','Veralice','Veridiana','Veronica','Virginia','Vitoria','Vivian','Viviane Valentino','Valdir','Valmir','Vanderley','Vasco','Venâncio','Venceslau','Vicente','Vinicius','Vitor','Vivaldo','Vladimir','Vlamir Xaquira','Xaukia','Xênia Xavier Yara','Yanna','Yasmin','Yolanda','Yole','Yone','Yose Yago','Yan','Yasson','Yglesio','Yuki','Yuri','Yuso W Z Walquiria','Wanda','Wanderleia','Wanessa','Wendy','Wilma Wagner','Wald','Waldir','Wallace','Walter','Wander','Wando','Washington','Weblen','Wellington','Welson','Wesley','Willian','Wilson','Wolf Zaira','Zarifa','Zelia','Zelinda','Zelita','Zenaide','Zenilde','Zenir','Zila','Zilda','Zilena','Zilma','Zita','Zora','Zoraide','Zulmira','Zyndal ','Zacarias','Zelio','Zenóbio ','Zeus','Ziraldo','Zozimo']


    last = ['Agostinho', 'Aguiar', 'Albuquerque', 'Alegria', 'Alencastro',
            'Almada', 'Alves', 'Alvim', 'Amorim', 'Andrade', 'Antunes', 'Aparicio', 'Apolinario', 'Araújo',
            'Arruda', 'Assis', 'Assuncao', 'avila', 'Azambuja', 'Baptista', 'Barreto', 'Barros', 'Beira-Mar',
            'Belchior', 'Belem', 'Bernardes', 'Bittencourt', 'Boaventura', 'Bonfim', 'Botelho', 'Brites',
            'Brito', 'Caetano', 'Calixto', 'Camacho', 'Camilo', 'Capelo', 'Castro', 'Cavalcante', 'Chaves',
            'Conceicao', 'Corte Real', 'Cortês', 'Coutinho', 'Crespo', 'Cunha', 'Curado', 'Custódio',
            'Córdoba',  'Damasio', 'Dantas', 'Dias', 'Dinis', 'Domingues', 'Dorneles', 'dos Reis',
            'Drumond', 'D’avila', 'Escobar', 'Espinosa', 'Esteves', 'Evangelista', 'Farias', 'Ferrari',
            'Figueiredo', 'Figueiroa', 'Flores', 'Fogaca', 'Freitas', 'Frutuoso', 'Furtado', 'Felix',
            'Galvao', 'Garcia', 'Gaspar', 'Gentil', 'Geraldes', 'Gil', 'Godinho', 'Gomes', 'Gonzaga',
            'Goulart', 'Gouveia', 'Guedes', 'Guimaraes', 'Guterres', 'Góis', 'Hernandes', 'Hilario',
            'Hipólito', 'Ibrahim', 'Ilha', 'Infante',  'Jaques', 'Jesus', 'Jordao', 'Lacerda',
            'Lancastre', 'Leiria', 'Lessa', 'Machado', 'Maciel', 'Magalhaes', 'Maia', 'Maldonado', 'Marinho',
            'Marques', 'Martins', 'Medeiros', 'Meireles', 'Mello', 'Mendes', 'Menezes', 'Mesquita', 'Modesto',
            'Monteiro', 'Morais', 'Moreira', 'Morgado', 'Moura', 'Muniz', 'Neves', 'Nogueira', 'Novais',
            'Nóbrega', 'Ornelas', 'Oliveira', 'Ourique', 'Pacheco', 'Padilha', 'Paiva', 'Paraiso', 'Paris',
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



    def myround(self,x, base=5): 
        return int(base * round(float(x)/base))

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
    if(len(sys.argv)<2):
        print("Insira o nome do banco e a quantidade de dados a ser gerada\npython [nome] [quant]")
        sys.exit(0)
    else:
        nome = sys.argv[1]
        quantidade = int(sys.argv[2])

    with open(nome, 'w', newline='') as csvfile:
        gp = GeradorPessoas()
        ge = GeradorExercicios()
        ga = GeradorAmnase()
        gm = GeradorMedidas()
        
        #'nome', 
        campos = ['idade', 'altura', 'peso', 'ex1-nome', 'ex1-categoria', 'ex1-serie','ex1-repeticao',
        'ex2-nome', 'ex2-categoria', 'ex2-serie', 'ex2-repeticao','ex3-nome', 'ex3-categoria', 'ex3-serie', 'ex3-repeticao',
        'ex4-nome', 'ex4-categoria', 'ex4-serie', 'ex4-repeticao','ex5-nome', 'ex5-categoria', 'ex5-serie', 'ex5-repeticao',
        'ex6-nome', 'ex6-categoria', 'ex6-serie', 'ex6-repeticao','ex7-nome', 'ex7-categoria', 'ex7-serie', 'ex7-repeticao',
        'ex8-nome', 'ex8-categoria', 'ex8-serie', 'ex8-repeticao','ex9-nome', 'ex9-categoria', 'ex9-serie', 'ex9-repeticao',
        'ex10-nome', 'ex10-categoria', 'ex10-serie', 'ex10-repeticao',
        'ex11-nome', 'ex11-categoria', 'ex11-serie', 'ex11-repeticao',
        'ex12-nome', 'ex12-categoria', 'ex12-serie', 'ex12-repeticao',
        'ex13-nome', 'ex13-categoria', 'ex13-serie', 'ex13-repeticao',
        'ex14-nome', 'ex14-categoria', 'ex14-serie', 'ex14-repeticao',
        'ex15-nome', 'ex15-categoria', 'ex15-serie', 'ex15-repeticao',
        'esteira','bicicleta',
        'hipertrofia','lentes_contato','alergia','tabagismo',
        'bebida_alcoolica','medicamento','epilepsia','convulsoes','doenca','cirurgia_plastica','cortes','abrasoes','inchacos',
        'Ombro','Torax','Cintura','Quadris','Pescoco','Biceps','Antebraco','Peito','Coxas','Panturrilha','imc','status_imc']

        writer = csv.DictWriter(csvfile, fieldnames=campos)

        writer.writeheader()

        for x in range(quantidade):
            amnase = ga.gerar()

            #Ficha superior A = 5EX
            peitos = ge.gerarListaNova('peito')
            peitos = ge.randomLista(peitos,1)

            triceps = ge.gerarListaNova('triceps')
            triceps = ge.randomLista(triceps,2)

            abdominal = ge.gerarListaNova('abdominal')
            abdominal = ge.randomLista(abdominal, 1)

            biceps = ge.gerarListaNova('biceps')
            biceps = ge.randomLista(biceps, 1)

            #Ficha Superior B = 4EX
            ombro = ge.gerarListaNova('ombro')
            ombro = ge.randomLista(ombro, 1)

            trapezio = ge.gerarListaNova('trapezio')
            trapezio = ge.randomLista(trapezio, 2)

            costas = ge.gerarListaNova('costas')
            costas = ge.randomLista(costas, 1)

            #Ficha Perna C = 6EX
            perna = ge.gerarListaNova('perna')
            perna = ge.randomLista(perna, 3)

            gluteos = ge.gerarListaNova('gluteos')
            gluteos = ge.randomLista(gluteos,1)

            coxa = ge.gerarListaNova('coxa')
            coxa = ge.randomLista(coxa, 2)



            

            listaEx = ge.gerarExercicio(10)
            serie = random.randint(2, 4)
            repeticao = random.choice([10, 15, 20])
            peso_gerado = gp.gerar_peso()
            altura_gerada = gp.gerar_altura()
            imc_gerado = gm.calculaIMC(peso_gerado,altura_gerada)
            status_imc_gerado = gm.statusIMC(imc_gerado)
            tempo_corrida = imc_gerado/1.5
            tempo_corrida = gm.myround(tempo_corrida)
           
            #'nome': gp.gerar_nome_completo(), 
            writer.writerow({'idade': gp.gerar_idade(), 'altura': altura_gerada, 'peso': peso_gerado,
             'ex1-nome': peitos[0]['nome'], 'ex1-categoria': peitos[0]['categoria'], 'ex1-serie': serie, 'ex1-repeticao': repeticao,
             'ex2-nome': triceps[0]['nome'], 'ex2-categoria': triceps[0]['categoria'], 'ex2-serie': serie, 'ex2-repeticao': repeticao,
             'ex3-nome': triceps[1]['nome'], 'ex3-categoria': triceps[1]['categoria'], 'ex3-serie': serie, 'ex3-repeticao': repeticao,
             'ex4-nome': abdominal[0]['nome'], 'ex4-categoria': abdominal[0]['categoria'], 'ex4-serie': serie, 'ex4-repeticao': repeticao,
             'ex5-nome': biceps[0]['nome'], 'ex5-categoria': biceps[0]['categoria'], 'ex5-serie': serie, 'ex5-repeticao': repeticao,
             'ex6-nome': ombro[0]['nome'], 'ex6-categoria': ombro[0]['categoria'], 'ex6-serie': serie, 'ex6-repeticao': repeticao,
             'ex7-nome': trapezio[0]['nome'], 'ex7-categoria': trapezio[0]['categoria'], 'ex7-serie': serie, 'ex7-repeticao': repeticao,
             'ex8-nome': trapezio[1]['nome'], 'ex8-categoria': trapezio[1]['categoria'], 'ex8-serie': serie, 'ex8-repeticao': repeticao,
             'ex9-nome': costas[0]['nome'], 'ex9-categoria': costas[0]['categoria'], 'ex9-serie': serie, 'ex9-repeticao': repeticao,
             'ex10-nome': perna[0]['nome'], 'ex10-categoria': perna[0]['categoria'], 'ex10-serie': serie, 'ex10-repeticao': repeticao, 
             'ex11-nome': perna[1]['nome'], 'ex11-categoria': perna[1]['categoria'], 'ex11-serie': serie, 'ex11-repeticao': repeticao,
             'ex12-nome': perna[2]['nome'], 'ex12-categoria': perna[2]['categoria'], 'ex12-serie': serie, 'ex12-repeticao': repeticao,
             'ex13-nome': gluteos[0]['nome'], 'ex13-categoria': gluteos[0]['categoria'], 'ex13-serie': serie, 'ex13-repeticao': repeticao,
             'ex14-nome': coxa[0]['nome'], 'ex14-categoria': coxa[0]['categoria'], 'ex14-serie': serie, 'ex14-repeticao': repeticao,
             'ex15-nome': coxa[1]['nome'], 'ex15-categoria': coxa[1]['categoria'], 'ex15-serie': serie, 'ex15-repeticao': repeticao,
             'esteira': tempo_corrida,'bicicleta': tempo_corrida,
             'hipertrofia' : amnase[0],'lentes_contato':amnase[1],'alergia':amnase[2],'tabagismo':amnase[3],'bebida_alcoolica':amnase[4],
             'medicamento':amnase[5],'epilepsia':amnase[6],'convulsoes':amnase[7],'doenca':amnase[8],'cirurgia_plastica': amnase[9],
             'cortes':amnase[10],'abrasoes':amnase[11],'inchacos':amnase[12],'Ombro':gm.gerarOmbro(),'Torax':gm.gerarTorax(),'Cintura':gm.gerarCintura(),
             'Quadris':gm.gerarQuadris(),'Pescoco':gm.gerarPescoco(),'Biceps':gm.gerarBiceps(),'Antebraco':gm.gerarAntebraco(),'Peito':gm.gerarPeito(),
             'Coxas':gm.gerarCoxas(),'Panturrilha':gm.gerarPanturrilha(),'imc':float("{0:.2f}".format(imc_gerado)),'status_imc':status_imc_gerado
             })