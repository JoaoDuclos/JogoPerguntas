import threading
import time

class Timer:
    # Inicializa o objeto com a duração especificada
    # Cria threading.Event que vai ser usado para sinalizar quando o timer tem que parar
    def __init__(self, duration):
        self.duration = duration
        self.user_input_event = threading.Event()

    # Metodo privado que serve para calcular o tempo final de acrodo com a duração e checar continuamente se start_time passou do tempo final
    # Se user_input_event é set, a função retorna, caso contrario printa a mensagem
    def _timer_thread_func(self):
        start_time = time.time()
        end_time = start_time + self.duration
        while time.time() < end_time:
            if self.user_input_event.is_set():
                return
        print('Seu tempo acabou.')

    # Cria uma thread para poder rodar em paralelo com a pergunta e inicializa ela
    def start(self):
        timer_thread = threading.Thread(target=self._timer_thread_func)
        timer_thread.start()

    # Indica que o temporizador tem que parar
    def stop(self):
        self.user_input_event.set()

