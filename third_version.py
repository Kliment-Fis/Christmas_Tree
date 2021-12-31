from random import choice
import pygame

cell_size = 15 #15
weight = 21 * cell_size
height = 37 * cell_size
indent = 7 #3
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
cords = [[9, 8], [10, 9], [11, 8], [6, 11], [7, 12], [8, 11], [9, 12], [10, 11], [11, 12], [12, 11], [13, 12], 
[14, 11], [7, 14], [8, 15], [9, 14], [10, 15], [11, 14], [12, 15], [13, 14], [4, 17], [5, 18], [6, 17], [7, 18], 
[8, 17], [9, 18], [10, 17], [11, 18], [12, 17], [13, 18], [14, 17], [15, 18], [16, 17], [6, 20], [7, 21], [8, 20], 
[9, 21], [10, 20], [11, 21], [12, 20], [13, 21], [14, 20], [3, 23], [4, 24], [5, 23], [6, 24], [7, 23], [8, 24], 
[9, 23], [10, 24], [11, 23], [12, 24], [13, 23], [14, 24], [15, 23], [16, 24], [17, 23], [8, 9], [12, 9], [3, 18], 
[17, 18], [5, 21], [15, 21], [18, 24], [2, 24], [5, 12], [15, 12], [6, 15], [14, 15]]

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
            if [11 - element + j, i + indent] in cords:
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
            print(cord)

pygame.quit()
