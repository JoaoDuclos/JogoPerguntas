import time
import random
from categorias import categories, options
from  classes import Button
from timer import Timer

def get_user_input():
    while True:
        try:
            resposta = input('Resposta: ')
            if resposta == '':
                resposta = 0
                break
            resposta = int(resposta)
        except ValueError:
            print('Selecione uma das opções')
        else:
            break
    return resposta

# Printa as perguntas e alternativas
def printingQuestion(pergunta):   
    print(pergunta['pergunta'])
    print()
    for i, alternativa in enumerate(pergunta['alternativas']):
        print(f'{i+1}) {alternativa}')

# Faz a pergunta e começa o timer, se o timer acabar a questão é dada como erro
def askingQuestionTimer(duration):
    timer = Timer(duration)
    timer.start()
    resposta = get_user_input()
    timer.stop()
    if resposta and timer.is_time_up() == False:
        if resposta in [1, 2, 3, 4]:
            return resposta
        print('Opção tem que estar entre 1 e 4')
    print('O tempo acabou sua resposta será invalida')
    return -1
        
# Checa se a resposta fornecida e retorna 1 se for correta e 0 caso contrario
def checkingAnswer(pergunta, resposta):
    if pergunta['resposta'] == pergunta['alternativas'][resposta-1]:
        print('\nResposta Certa\n')
        time.sleep(1)
        return 1
    else:
        print('\nResposta Errada\n')
        time.sleep(1)
        return 0

# Gera todas as perguntas de uma categoria
def makingAllQuestions(cat):
    print('Você terá 10 segundos para responder cada pergunta')
    time.sleep(1)
    print()
    for pergunta in categories[cat]:
        makingTheQuestion(pergunta)


def makingTheQuestion(pergunta, duration):
    printingQuestion(pergunta)
    resposta = askingQuestionTimer(duration)
    if resposta == -1:
        print('Resposta Errada\n')
        time.sleep(1)
        return 0
    return checkingAnswer(pergunta, resposta)


def playGame(available_questions, duration):
    life = 3
    print('São 10 perguntas!')
    print('Você terá 10 segundos para responder cada pergunta')
    time.sleep(1)
    for i in range(1,11):
        categorie = options[random.randint(0,len(categories)-1)]
        time.sleep(1)
        print()
        print(f'{i})', end=' ')
        result = makingTheQuestion(available_questions[categorie].pop(random.randint(0, len(available_questions[categorie])-1)), duration)
        if result:
            print(f'Você tem {life} vidas\n')
            time.sleep(1)
        else:
            life-=1
            print(f'Você tem {life} vidas\n')
            time.sleep(1)
        if life == 0:
            break
    if life == 0:
        print('Você perdeu!')
    else:
        print('Você ganhou!')

def main():
    available_questions = categories.copy()
    for i, category in enumerate(categories):
        print(f'{i+1}) {category}')
    print(f'6) Jogar')
    cat = get_user_input()
    duration = 5
    # Chama makingAllQuestions com base na categoria escolhida pelo jogador ou inicia o jogo diretamente
    if cat == 1:
        makingAllQuestions(options[0], duration)
    elif cat == 2:
        makingAllQuestions(options[1], duration)
    elif cat == 3:
        makingAllQuestions(options[2], duration)
    elif cat == 4:
        makingAllQuestions(options[3], duration)
    elif cat == 5:
        makingAllQuestions(options[4], duration)
    elif cat == 6:
        playGame(available_questions, duration)
    else:
        print('Opção inválida')

if __name__ == "__main__":
    main()