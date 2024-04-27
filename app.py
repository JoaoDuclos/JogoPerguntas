import pygame
import sys
from classes import Button
import perguntados

pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perguntados")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (106, 159, 181)
GREEN = (155, 206, 120)

title_font = pygame.font.SysFont('comicsans', 60)
text_font = pygame.font.SysFont('comicsans', 30)

def play():
    pygame.display.set_caption("Perguntados")

    screen.fill(BLACK)

    back_button_image = pygame.image.load("menubutton\squarebottons\squarebuttons\_back_quarebutton.png")
    back_button_surface = pygame.transform.scale(back_button_image, (50, 50))
    back_button_press_image = pygame.image.load("menubutton\squarebottons\coloredsquarebottons\_back_col_squarebutton.png")
    back_button_press_surface = pygame.transform.scale(back_button_press_image, (50, 50))

    back_button = Button(back_button_surface, back_button_press_surface, 40, 40)

    option_one_image = pygame.image.load("menubutton\largebuttons\largebuttons\load_button.png")
    option_one_surface = pygame.transform.scale(option_one_image, (450, 150))
    option_one_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\load_colbutton.png")
    option_one_press_surface = pygame.transform.scale(option_one_press_image, (450, 150))

    option_one = Button(option_one_surface, option_one_press_surface, WIDTH/4, 300)

    option_two_image = pygame.image.load("menubutton\largebuttons\largebuttons\load_button.png")
    option_two_surface = pygame.transform.scale(option_two_image, (450, 150))
    option_two_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\load_colbutton.png")
    option_two_press_surface = pygame.transform.scale(option_two_press_image, (450, 150))

    option_two = Button(option_two_surface, option_two_press_surface, 3*WIDTH/4, 300)

    option_three_image = pygame.image.load("menubutton\largebuttons\largebuttons\load_button.png")
    option_three_surface = pygame.transform.scale(option_three_image, (450, 150))
    option_three_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\load_colbutton.png")
    option_three_press_surface = pygame.transform.scale(option_three_press_image, (450, 150))

    option_three = Button(option_three_surface, option_three_press_surface, WIDTH/4, 500)

    option_four_image = pygame.image.load("menubutton\largebuttons\largebuttons\load_button.png")
    option_four_surface = pygame.transform.scale(option_four_image, (450, 150))
    option_four_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\load_colbutton.png")
    option_four_press_surface = pygame.transform.scale(option_four_press_image, (450, 150))

    option_four = Button(option_four_surface, option_four_press_surface, 3*WIDTH/4, 500)

    while True:
        screen.fill(WHITE)

        mouse_position = pygame.mouse.get_pos()

        title_text = title_font.render("Perguntados", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH/2, 100))
        screen.blit(title_text, title_rect)

        for button in [back_button, option_one, option_three, option_two, option_four]:
            button.update()
            button.changeColor(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_position):
                    initial_screen()
                if option_one.checkForInput(mouse_position):
                    print('Option 1')
                if option_two.checkForInput(mouse_position):
                    print('Option 2')
                if option_three.checkForInput(mouse_position):
                    print('Option 3')
                if option_four.checkForInput(mouse_position):
                    print('Option 4')

        pygame.display.update()

def initial_screen():
    pygame.display.set_caption("Menu")

    start_button_image = pygame.image.load("menubutton\largebuttons\largebuttons\start_button.png")
    start_button_surface = pygame.transform.scale(start_button_image, (350, 150))
    start_button_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\start_colbutton.png")
    start_button_press_surface = pygame.transform.scale(start_button_press_image, (350, 150))

    start_button = Button(start_button_surface, start_button_press_surface, WIDTH/2, 250)

    options_button_image = pygame.image.load("menubutton\largebuttons\largebuttons\options_button.png")
    options_button_surface = pygame.transform.scale(options_button_image, (350, 150))
    options_button_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\options_colbutton.png")
    options_button_press_surface = pygame.transform.scale(options_button_press_image, (350, 150))

    options_button = Button(options_button_surface, options_button_press_surface, WIDTH/2, 400)

    quit_button_image = pygame.image.load("menubutton\largebuttons\largebuttons\quit_button.png")
    quit_button_surface = pygame.transform.scale(quit_button_image, (350, 150))
    quit_button_press_image = pygame.image.load("menubutton\largebuttons\coloredlargebuttons\quit_colbutton.png")
    quit_button_press_surface = pygame.transform.scale(quit_button_press_image, (350, 150))

    quit_button = Button(quit_button_surface, quit_button_press_surface, WIDTH/2, 550)


    while True:
        screen.fill(WHITE)
        
        mouse_position = pygame.mouse.get_pos()

        title_text = title_font.render("Perguntados", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH/2, 100))
        screen.blit(title_text, title_rect)

        for button in [start_button, options_button, quit_button]:
            button.update()
            button.changeColor(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(mouse_position):
                    play()
                if options_button.checkForInput(mouse_position):
                    play()
                if quit_button.checkForInput(mouse_position):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    initial_screen()