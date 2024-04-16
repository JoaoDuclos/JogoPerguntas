import time
categories = {
    'general': [
        {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
        {'pergunta':'Qual é o maior planeta do sistema solar?', 'resposta':'Júpiter','alternativas':['Vênus', 'Marte', 'Saturno', 'Júpiter']},
        {'pergunta':'Qual é o maior planeta do sistema solar?', 'resposta':'Júpiter','alternativas':['Vênus', 'Marte', 'Saturno', 'Júpiter']},
        {'pergunta':'Quantos elementos químicos naturais existem?', 'resposta':'90','alternativas':['50', '90', '118', '63']},
        {'pergunta':'Quem escreveu "Dom Quixote"?', 'resposta':'Miguel de Cervantes','alternativas':['William Shakespeare', 'Miguel de Cervantes', 'Jorge Luis Borges', 'Gabriel García Márquez']},
        {'pergunta':'Qual é o maior animal terrestre?', 'resposta':'Elefante africano','alternativas':['Baleia-azul', 'Elefante africano', 'Girafa', 'Rinoceronte-branco']},
        {'pergunta':'Qual é a capital do Canadá?', 'resposta':'Ottawa','alternativas':['Toronto', 'Montreal', 'Ottawa', 'Vancouver']},
        {'pergunta':'Qual é a maior cordilheira do mundo?', 'resposta':'Cordilheira dos Andes','alternativas':['Montanhas Rochosas', 'Cordilheira dos Andes', 'Cordilheira do Himalaia', 'Cordilheira dos Alpes']},
        {'pergunta':'Quem é considerado o "pai da psicanálise"?', 'resposta':'Sigmund Freud','alternativas':['Carl Jung', 'Sigmund Freud', 'B.F. Skinner', 'Ivan Pavlov']},
        {'pergunta':'Quantas estrelas existem na bandeira dos Estados Unidos?', 'resposta':'50','alternativas':['48', '50', '52', '54']},
        {'pergunta':'Qual é o metal mais caro do mundo?', 'resposta':'Ródio','alternativas':['Ouro', 'Platina', 'Ródio', 'Paládio']},
        {'pergunta':'Quem foi o primeiro homem a pisar na Lua?', 'resposta':'Neil Armstrong','alternativas':['Buzz Aldrin', 'Neil Armstrong', 'Yuri Gagarin', 'Alan Shepard']}
    ],
    'history': [
        {'pergunta':'Quem foi o nome mais famoso da revolução francesa?', 'resposta':'Napoleão','alternativas':['Napoleão', 'Hitler', 'Bejamin', 'Arthur']},
        {'pergunta':'Quem foi o primeiro presidente dos Estados Unidos?', 'resposta':'George Washington','alternativas':['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'John Adams']},
        {'pergunta':'Quem foi o primeiro imperador romano?', 'resposta':'César Augusto','alternativas':['Júlio César', 'Calígula', 'Nero', 'César Augusto']},
        {'pergunta':'Quem foi o presidente dos EUA durante a Segunda Guerra Mundial?', 'resposta':'Franklin D. Roosevelt','alternativas':['Harry S. Truman', 'Dwight D. Eisenhower', 'Franklin D. Roosevelt', 'John F. Kennedy']},
        {'pergunta':'Qual foi a capital do Império Romano do Ocidente?', 'resposta':'Roma','alternativas':['Atenas', 'Cartago', 'Constantinopla', 'Roma']},
        {'pergunta':'Quem foi o líder da Revolução Russa de 1917?', 'resposta':'Vladimir Lênin','alternativas':['Joseph Stalin', 'Vladimir Lênin', 'Leon Trotsky', 'Mikhail Gorbachev']},
        {'pergunta':'Qual foi o primeiro país a conceder o direito de voto às mulheres?', 'resposta':'Nova Zelândia','alternativas':['Estados Unidos', 'Reino Unido', 'Nova Zelândia', 'Suécia']},
        {'pergunta':'Quem foi o líder da Revolução Cubana de 1959?', 'resposta':'Fidel Castro','alternativas':['Che Guevara', 'Fidel Castro', 'Raul Castro', 'Hugo Chávez']},
        {'pergunta':'Qual foi o ano do "Descobrimento do Brasil"?', 'resposta':'1500','alternativas':['1400', '1492', '1500', '1520']},
        {'pergunta':'Qual cidade foi a capital do Império Inca?', 'resposta':'Cusco','alternativas':['Machu Picchu', 'Cusco', 'Lima', 'Bogotá']},
        {'pergunta':'Quem foi o primeiro presidente da África do Sul após o apartheid?', 'resposta':'Nelson Mandela','alternativas':['Frederik de Klerk', 'Thabo Mbeki', 'Nelson Mandela', 'Jacob Zuma']},
        {'pergunta':'Qual foi o período conhecido como "Idade das Trevas" na Europa?', 'resposta':'Idade Média','alternativas':['Renascimento', 'Idade Média', 'Idade Antiga', 'Idade Moderna']}
    ],
    'science': [
        {'pergunta':'Qual é o elemento mais abundante no universo?', 'resposta':'Hidrogênio','alternativas':['Oxigênio', 'Nitrogênio', 'Carbono', 'Hidrogênio']},
        {'pergunta':'Qual é a velocidade da luz no vácuo?', 'resposta':'299,792,458 metros por segundo','alternativas':['150,000,000 metros por segundo', '299,792,458 metros por segundo', '500,000,000 metros por segundo', '100,000,000 metros por segundo']},
        {'pergunta':'Qual é o valor da aceleração da gravidade na superfície da Terra?', 'resposta':'9.81 metros por segundo quadrado','alternativas':['10 metros por segundo quadrado', '9.8 metros por segundo quadrado', '9.81 metros por segundo quadrado', '10.1 metros por segundo quadrado']},
        {'pergunta':'Qual é o elemento mais leve da tabela periódica?', 'resposta':'Hidrogênio','alternativas':['Hélio', 'Lítio', 'Hidrogênio', 'Neônio']},
        {'pergunta':'Qual é a temperatura de fusão do gelo em graus Celsius?', 'resposta':'0°C','alternativas':['-10°C', '0°C', '10°C', '20°C']},
        {'pergunta':'Quem propôs a teoria da relatividade?', 'resposta':'Albert Einstein','alternativas':['Isaac Newton', 'Albert Einstein', 'Galileu Galilei', 'Stephen Hawking']},
        {'pergunta':'Qual é a camada mais externa da Terra?', 'resposta':'Crosta','alternativas':['Núcleo', 'Manto', 'Crosta', 'Astenosfera']},
        {'pergunta':'Qual é o nome dado à energia proveniente do Sol?', 'resposta':'Energia Solar','alternativas':['Energia Eólica', 'Energia Hidrelétrica', 'Energia Nuclear', 'Energia Solar']},
        {'pergunta':'Qual é a unidade básica de medida de corrente elétrica?', 'resposta':'Ampère','alternativas':['Watt', 'Volts', 'Ohm', 'Ampère']},
        {'pergunta':'Qual é o planeta mais próximo do Sol?', 'resposta':'Mercúrio','alternativas':['Vênus', 'Terra', 'Marte', 'Mercúrio']},
        {'pergunta':'Quem propôs a teoria do Big Bang?', 'resposta':'Georges Lemaître','alternativas':['Albert Einstein', 'Stephen Hawking', 'Georges Lemaître', 'Carl Sagan']},
        {'pergunta':'Qual é o processo pelo qual as plantas produzem seu próprio alimento?', 'resposta':'Fotossíntese','alternativas':['Respiração', 'Fotossíntese', 'Digestão', 'Transpiração']}
    ],
    'geography': [
        {'pergunta':'Qual é o maior país do mundo em área terrestre?', 'resposta':'Rússia','alternativas':['Canadá', 'Estados Unidos', 'China', 'Rússia']},
        {'pergunta':'Qual é o rio mais longo do mundo?', 'resposta':'Rio Amazonas','alternativas':['Rio Nilo', 'Rio Amazonas', 'Rio Mississipi', 'Rio Yangtzé']},
        {'pergunta':'Qual é o maior oceano do mundo?', 'resposta':'Oceano Pacífico','alternativas':['Oceano Atlântico', 'Oceano Índico', 'Oceano Pacífico', 'Oceano Ártico']},
        {'pergunta':'Qual é o país mais populoso do mundo?', 'resposta':'China','alternativas':['Índia', 'Estados Unidos', 'China', 'Indonésia']},
        {'pergunta':'Qual é o deserto mais quente do mundo?', 'resposta':'Deserto do Saara','alternativas':['Deserto do Atacama', 'Deserto do Saara', 'Deserto de Gobi', 'Deserto da Arábia']},
        {'pergunta':'Qual é a maior ilha do mundo?', 'resposta':'Groenlândia','alternativas':['Austrália', 'Groenlândia', 'Nova Guiné', 'Borneo']},
        {'pergunta':'Qual é o maior arquipélago do mundo?', 'resposta':'Indonésia','alternativas':['Filipinas', 'Indonésia', 'Japão', 'Havaí']},
        {'pergunta':'Qual é o maior lago de água doce do mundo em volume?', 'resposta':'Lago Baikal','alternativas':['Lago Vitória', 'Lago Superior', 'Lago Titicaca', 'Lago Baikal']},
        {'pergunta':'Qual é a montanha mais alta da África?', 'resposta':'Monte Kilimanjaro','alternativas':['Monte Elbrus', 'Monte Everest', 'Monte Kilimanjaro', 'Monte McKinley']},
        {'pergunta':'Qual é o país com maior quantidade de vulcões ativos?', 'resposta':'Indonésia','alternativas':['Japão', 'Itália', 'Chile', 'Indonésia']},
        {'pergunta':'Qual é o maior país da América do Sul em área territorial?', 'resposta':'Brasil','alternativas':['Argentina', 'Brasil', 'Peru', 'Colômbia']},
        {'pergunta':'Qual é o maior rio da América do Sul em volume de água?', 'resposta':'Rio Amazonas','alternativas':['Rio Paraná', 'Rio Amazonas', 'Rio Orinoco', 'Rio São Francisco']}
    ],
    'sport': [
        {'pergunta':'Qual foi o país que ganhou a primeira copa do mundo?', 'resposta':'Uruguai','alternativas':['França', 'Uruguai', 'Brasil', 'Holanda']},
        {'pergunta':'Quem é o jogador com mais títulos na história do futebol?', 'resposta':'Messi','alternativas':['Messi', 'Puskás', 'Pelé', 'Zidane']},
        {'pergunta':'Qual é o esporte mais popular no Japão?', 'resposta':'Beisebol','alternativas':['Sumô', 'Futebol', 'Beisebol', 'Tênis']},
        {'pergunta':'Qual é o único país a ter participado de todas as Copas do Mundo de Futebol?', 'resposta':'Brasil','alternativas':['Argentina', 'Brasil', 'Alemanha', 'Itália']},
        {'pergunta':'Qual é o esporte mais popular no mundo?', 'resposta':'Futebol','alternativas':['Basquete', 'Tênis', 'Futebol', 'Críquete']},
        {'pergunta':'Qual é o esporte mais assistido nos Estados Unidos?', 'resposta':'Futebol Americano','alternativas':['Basquete', 'Basebol', 'Futebol Americano', 'Hóquei no Gelo']},
        {'pergunta':'Qual é o esporte em que se pratica o "Grand Slam"?', 'resposta':'Tênis','alternativas':['Golfe', 'Tênis', 'Futebol', 'Rúgbi']},
        {'pergunta':'Quem é o único jogador de basquete a marcar 100 pontos em um único jogo da NBA?', 'resposta':'Wilt Chamberlain','alternativas':['Michael Jordan', 'Kobe Bryant', 'LeBron James', 'Wilt Chamberlain']},
        {'pergunta':'Qual é o esporte em que se utiliza uma "puck"?', 'resposta':'Hóquei no Gelo','alternativas':['Rugby', 'Hóquei no Gelo', 'Polo Aquático', 'Lacrosse']},
        {'pergunta':'Qual é o esporte em que se utiliza uma "rede" para marcar pontos?', 'resposta':'Vôlei','alternativas':['Basquete', 'Tênis', 'Vôlei', 'Badminton']},
        {'pergunta':'Qual é o esporte que usa a expressão "touchdown"?', 'resposta':'Futebol Americano','alternativas':['Rúgbi', 'Futebol Americano', 'Hóquei no Gelo', 'Polo']},
        {'pergunta':'Quem foi o primeiro homem a correr a milha em menos de quatro minutos?', 'resposta':'Roger Bannister','alternativas':['Carl Lewis', 'Usain Bolt', 'Roger Bannister', 'Mo Farah']},
        {'pergunta':'Qual é o esporte em que se utiliza uma "vara" para saltar?', 'resposta':'Salto com Vara','alternativas':['Salto Triplo', 'Salto em Distância', 'Salto com Vara', 'Salto em Altura']},
        {'pergunta':'Qual é o esporte mais popular nos Jogos Olímpicos de Inverno?', 'resposta':'Patinagem Artística','alternativas':['Esqui Alpino', 'Patinagem de Velocidade', 'Hóquei no Gelo', 'Patinagem Artística']}
    ]
}

for i, category in enumerate(categories):
    print(f'{i+1}) {category}')
cat = int(input('Qual genero você deseja? '))

def makingTheQuestion(cat):
    for pergunta in categories[cat]:
        print(pergunta['pergunta'])
        for i, auternativa in enumerate(pergunta['alternativas']):
            print(f'{i+1}) {auternativa}')
        resposta = int(input('Resposta: '))
        if pergunta['resposta'] == pergunta['alternativas'][resposta-1]:
            print('Resposta Certa')
        else:
            print('Resposta Errada')

if cat == 1:
    makingTheQuestion('general')
elif cat == 2:
    makingTheQuestion('history')
elif cat == 3:
    makingTheQuestion('science')
elif cat == 4:
    makingTheQuestion('geography')
elif cat == 5:
    makingTheQuestion('sport')
else:
    print('Opção inválida')

