import pygame

pygame.init()
pygame.display.set_caption("JogoPerguntas")
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((300, 250, 50, 50))
clock = pygame.time.Clock()

test_fonts = pygame.font.Font(None, 50)

test_surface = pygame.Surface((800,100))
test_surface.fill('purple')
text_surface = test_fonts.render('Jogo de perguntas', False, 'white')

moving_surface = pygame.Surface((50,50))
msX_position = 750


button_1 = pygame.Surface((100,100))
button_2 = pygame.Surface((100,100))
button_3 = pygame.Surface((100,100))
button_4 = pygame.Surface((100,100))

run = True
while run:

    screen.fill('black')
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    screen.blit(test_surface, (0,0))
    screen.blit(text_surface,(200,20))
    if event.type == pygame.MOUSEBUTTONDOWN:
        msX_position -= 3

    screen.blit(moving_surface, (msX_position, 200))
    moving_surface.fill('white')
    if msX_position < -60:
        msX_position = 800

    pygame.display.update()
    clock.tick(60)

pygame.quit()