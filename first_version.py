from random import choice, randint
import pygame

cell_size = 15 #15
weight = 21 * cell_size
height = 37 * cell_size
indent = 7 #3
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]

pygame.init()
display = pygame.display.set_mode((weight, height))
def draw(x, y, color):
    pygame.draw.rect(display, color, (x + 1 , y + 1, cell_size -1, cell_size - 1))

def christmas_tree(x):
    if x == 1:
        return 1
    return 1 + (x - 1) * 2

stop = False
while not stop:

    element = 1
    for i in range(height // cell_size):
        for j in range(christmas_tree(element)):
            if randint(0, 50) == 1:
                draw((11 - element) * cell_size + j * cell_size, (i + indent) * cell_size, choice(colors))
            else:
                draw((11 - element) * cell_size + j * cell_size, (i + indent) * cell_size, (4, 56, 13))
            pygame.display.update()
        element += 1
        if i == 5:
            element = 3
        if i == 12:
            element = 5
        if i >= 18:
            break
    
    for i in range(6):
        for j in range(3):
            draw((9 + j) * cell_size, (i + 19 + indent) * cell_size, (66, 28, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

pygame.quit()
