import time
import threading
import random
from categorias import categories, options
#from classes import *

def get_user_input():
    resposta = input('Resposta: ')
    return resposta.strip()

def timer(duration, user_input_event):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        if user_input_event.is_set():
            return
    print('Seu tempo acabou.')

def makingAllQuestions(cat):
    for pergunta in categories[cat]:
        makingTheQuestion(pergunta)


# Função para apresentar uma pergunta e verificar a resposta do usuário
def makingTheQuestion(pergunta):
    print(pergunta['pergunta'])
    print()
    for i, alternativa in enumerate(pergunta['alternativas']):
        print(f'{i+1}) {alternativa}')

    user_input_event = threading.Event()
    timer_thread = threading.Thread(target=timer, args=(10, user_input_event))
    timer_thread.start()

    resposta = get_user_input()
    user_input_event.set()  # Signal to stop the timer thread

    if resposta:
        resposta = int(resposta)
        if resposta in [1, 2, 3, 4]:
            if pergunta['resposta'] == pergunta['alternativas'][resposta-1]:
                print('\nResposta Certa\n')
                time.sleep(1)
                return 1
            else:
                print('\nResposta Errada\n')
                time.sleep(1)
                return 0
        else:
            print('Opção tem que estar entre 1 e 4')
    return 0

# recebe a cópia como parametro para poder remover a pergunta após ser respondida evitando duplicatas
def playGame(available_questions):
    life = 3
    i=0
    print('São 10 perguntas!')
    print('Você terá 10 segundos para responder cada pergunta')
    time.sleep(1)
    # Controla o fluxo do jogo, determina as vidas do jogador e itera sobre 10 perguntas aleatórias de diferentes categorias
    while i < 10:
        i+=1
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
    #copia do dicionario com as perguntas
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