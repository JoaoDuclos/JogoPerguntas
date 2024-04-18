import time
import threading
import random
from categorias import categories, options
#from classes import *

def get_user_input() -> int:
    while True:
        try:
            resposta = int(input('Resposta: '))
        except ValueError:
            print('Opção tem que estar entre 1 e 4')
        else:
            break
    return resposta

# Roda um timer de um tempo determinado em segundos
def timer(duration, user_input_event):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        if user_input_event.is_set():
            return
    print('Seu tempo acabou.')

# Printa as perguntas e alternativas
def printingQuestion(pergunta):   
    print(pergunta['pergunta'])
    print()
    for i, alternativa in enumerate(pergunta['alternativas']):
        print(f'{i+1}) {alternativa}')

# Faz a pergunta e começa o timer, se o timer acabar a questão é dada como erro
def askingQuestionTimer():
    SEGUNDOS = 10
    user_input_event = threading.Event()
    timer_thread = threading.Thread(target=timer, args=(SEGUNDOS, user_input_event))
    timer_thread.start()

    resposta = get_user_input()
    user_input_event.set()  
    if resposta:
        if resposta in [1, 2, 3, 4]:
            return resposta
        print('Opção tem que estar entre 1 e 4')
    return 0
        
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


def makingTheQuestion(pergunta):
    printingQuestion(pergunta)
    resposta = askingQuestionTimer()
    return checkingAnswer(pergunta, resposta)


def playGame(available_questions):
    life = 3
    print('São 10 perguntas!')
    print('Você terá 10 segundos para responder cada pergunta')
    time.sleep(1)
    for i in range(1,11):
        categorie = options[random.randint(0,len(categories)-1)]
        time.sleep(1)
        print()
        print(f'{i})', end=' ')
        result = makingTheQuestion(available_questions[categorie].pop(random.randint(0, len(available_questions[categorie])-1)))
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
    cat = int(input('Qual genero você deseja? '))
    # Chama makingAllQuestions com base na categoria escolhida pelo jogador ou inicia o jogo diretamente
    if cat == 1:
        makingAllQuestions(options[0])
    elif cat == 2:
        makingAllQuestions(options[1])
    elif cat == 3:
        makingAllQuestions(options[2])
    elif cat == 4:
        makingAllQuestions(options[3])
    elif cat == 5:
        makingAllQuestions(options[4])
    elif cat == 6:
        playGame(available_questions)
    else:
        print('Opção inválida')

if __name__ == "__main__":
    main()