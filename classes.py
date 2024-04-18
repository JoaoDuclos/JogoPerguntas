import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("butoon!")
main_font = pygame.font.SysFont('comicsans', 50)

class Button():
    def __init__(self, image, press_image, pos_x, pos_y):
        self.image = image
        self.press_image = press_image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
    
    def update(self):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.rigth) and position[1] in range(self.rect.top, self.rect.bottom):
            print('Button press!')
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            screen.blit(self.press_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

button_surface = pygame.image.load("menubutton/largebuttons/largebuttons/Continue Button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button_press_surface = pygame.image.load("menubutton/largebuttons/coloredlargebuttons/Continue  col_Button.png")
button_press_surface = pygame.transform.scale(button_press_surface, (400, 150))

button = Button(button_surface, button_press_surface, 400, 300)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.checkForInput(pygame.mouse.get_pos())

        screen.fill("white")

        button.update()
        button.changeColor(pygame.mouse.get_pos())

        pygame.display.update()

if __name__ == "__main__":
    main()