import pygame 

pygame.init()

WIDTH, HEIGTH = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("kersiie")

running = True
while running:
    screen.fill((255, 255, 255)) # RGB - red, green, blue
    
    for event in pygame.event.get(): # получить все события и выполнить итерацию по ним
        if event.type == pygame.QUIT: # проверьте, является ли какое-либо из этих событий `ЗАВЕРШЕНИЕМ`
            running = False # если обнаружен `ВЫХОД` - установите значение running равным false и завершите цикл
            
    pygame.display.flip()