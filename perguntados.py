categories = {
    'general': [{'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']}],
    'history': [{'pergunta':'Quem foi o nome mais famoso da revolução francesa?', 'resposta':'Napoleão','alternativas':['Napoleão', 'Hitler', 'Bejamin', 'Arthur']}],
    'science': [{'pergunta':'Qual é o elemento mais abundante no universo?', 'resposta':'Hidrogênio','alternativas':['Oxigênio', 'Nitrogênio', 'Carbono', 'Hidrogênio']}],
    'geography': [{'pergunta':'Qual é o maior país do mundo em área terrestre?', 'resposta':'Rússia','alternativas':['Canadá', 'Estados Unidos', 'China', 'Rússia']}]
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

