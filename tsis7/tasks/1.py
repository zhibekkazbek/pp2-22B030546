import pygame
import math
import datetime
pygame.init()

WIDTH, HEIGTH = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Mickey Clock")
mickey = pygame.image.load(r'C:\Users\Сырым\Documents\pp2-22B030546\tsis7\tasks\main-clock.png')
right_hand = pygame.image.load(r'C:\Users\Сырым\Documents\pp2-22B030546\tsis7\tasks\right-hand.png')
left_hand = pygame.image.load(r'C:\Users\Сырым\Documents\pp2-22B030546\tsis7\tasks\left-hand.png')

clock = pygame.transform.scale(mickey, (WIDTH, HEIGTH))
Clock = pygame.time.Clock()
x, y = WIDTH // 2, HEIGTH // 2

running = True
while running:
    screen.blit(clock, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    time = datetime.datetime.now()
    min = time.minute - 13
    sec = time.second
    
    minute_angle = -math.radians((min / 60) * 360)
    minute_hand_rotated = pygame.transform.rotate(right_hand, math.degrees(minute_angle))
    minute_hand_rect = minute_hand_rotated.get_rect(center=(x, y))
    screen.blit(minute_hand_rotated, minute_hand_rect)
    
    second_angle = -math.radians((sec / 60) * 360)
    second_hand_rotated = pygame.transform.rotate(left_hand, math.degrees(second_angle))
    second_hand_rect = second_hand_rotated.get_rect(center=(x, y))
    screen.blit(second_hand_rotated, second_hand_rect)
    
    pygame.display.flip()
    
    Clock.tick(60)