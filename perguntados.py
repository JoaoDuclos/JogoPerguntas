perguntas = [
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Quanto é 2 + 2', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
    {'pergunta':'Qual o nome do rei(a) da inglaterra?', 'resposta':'Rei Charles','alternativas':['Rainha Elizabeth', 'Rei Charles', 'Rei Arthur', 'Rei Do Mate']},
]

for pergunta in perguntas:
    print(pergunta['pergunta'])
    for i, auternativa in enumerate(pergunta['alternativas']):
        print(f'{i+1}) {auternativa}')
    resposta = int(input('Resposta: '))
    if pergunta['resposta'] == pergunta['alternativas'][resposta-1]:
        print('Resposta Certa')
    else:
        print('Resposta Errada')
