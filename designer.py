from random import choice
import pygame

cell_size = 15 #15
weight = 21 * cell_size
height = 37 * cell_size
indent = 7 #3
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
cord = []

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
            if [11 - element + j, i + indent] in cord:
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
        # print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()
            cord.append([pos[0] // cell_size, pos[1] // cell_size])
        if event.type == pygame.QUIT:
            stop = True
            # print(cord)

pygame.quit()
