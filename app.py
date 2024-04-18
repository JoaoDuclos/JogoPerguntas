import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perguntados")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (106, 159, 181)
GREEN = (155, 206, 120)

title_font = pygame.font.SysFont('comicsans', 60)
text_font = pygame.font.SysFont('comicsans', 30)

def initial_screen():
    screen.fill(WHITE)
    
    mouse_position = pygame.mouse.get_pos()

    title_text = title_font.render("Perguntados", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH/2, HEIGHT/4))
    screen.blit(title_text, title_rect)
    
    # Instructions
    instructions_text1 = text_font.render("Precione espaço para começar", True, BLACK)
    instructions_rect1 = instructions_text1.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(instructions_text1, instructions_rect1)
    
    instructions_text2 = text_font.render("Precione Q para sair", True, BLACK)
    instructions_rect2 = instructions_text2.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    screen.blit(instructions_text2, instructions_rect2)

    pygame.display.update()

def display_message(message):
    # Display a message on the screen
    text = text_font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()

def draw_start_screen():
    screen.fill(WHITE)
    
    # Message text
    message_text = text_font.render("São 10 perguntas!", True, BLACK)
    message_rect = message_text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(message_text, message_rect)

    pygame.display.update()

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Start the game

                    draw_start_screen()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        initial_screen()

if __name__ == "__main__":
    main()