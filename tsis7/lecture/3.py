import pygame 

pygame.init()

WIDTH, HEIGTH = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("kersiie")

radius = 100
start_pos_rect_x = WIDTH // 2 - radius
start_pos_rect_y = HEIGTH // 2 - radius
rf = 100

running = True
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.draw.circle(screen, color=(127, 127, 127), center=(WIDTH // 2, HEIGTH // 2), radius=radius, width=5)
pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, 0), end_pos=(WIDTH, HEIGTH), width=10)
pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, HEIGTH), end_pos=(WIDTH, 0), width=10)
pygame.draw.rect(
    screen,
    color=(0, 0, 255),
    rect=pygame.Rect(
        start_pos_rect_x,
        start_pos_rect_y,
        radius * 2,
        radius * 2,
    ),
    width=5
)
pygame.draw.polygon(
    screen, 
    color=(0, 0, 0),
    points=[
        (start_pos_rect_x, start_pos_rect_y),
        (start_pos_rect_x + 2 * radius, start_pos_rect_y),
        (start_pos_rect_x + radius, start_pos_rect_y - rf),
    ],
    width=10
)

pygame.display.flip()