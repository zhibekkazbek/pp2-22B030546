import pygame 
import os

pygame.init()

pygame.display.set_caption("MP3") 
screen = pygame.display.set_mode((500, 400))

pygame.mixer.init()
Music = r"C:\Users\Сырым\Documents\pp2-22B030546\tsis7\tasks\music"
music_files = os.listdir(Music)
music_files = [os.path.join(Music, file) for file in music_files if file.endswith(".mp3")]

i = 0
pygame.mixer.music.load(music_files[i])

def play_music():
    pygame.mixer.music.play()
    
def stop_music():
    pygame.mixer.music.pause()
    
def next_music():
    global i
    i += 1
    
    if i >= len(music_files):
        i = 0
    
    pygame.mixer.music.load(music_files[i])
    pygame.mixer.music.play()
    
def previous_music():
    global i
    i -= 1
    
    if i < 0:
        i = len(music_files) - 1
        
    pygame.mixer.music.load(music_files[i])
    pygame.mixer.music.play()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play_music()
            elif event.key == pygame.K_DOWN:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                previous_music()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()